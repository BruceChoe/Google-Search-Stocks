from typing import List
from types import SimpleNamespace

from fastapi import APIRouter, Depends, Request, HTTPException, Response

from .dependencies import get_session
from .exceptions import NotFoundError


# TODO: Have convenience utilities defined with mix-ins.
class DustyRouter(APIRouter):
    def __init__(
        self,
        *args,
        doc_path="/docs#",
        rel,
        prefix=None,
        tags=None,
        schemas,
        universe,
        **kwargs,
    ):
        self.doc_path = doc_path
        self.rel = rel
        self.prefix = prefix or f"/{rel}"
        self.tags = tags or [rel]
        self.universe = universe
        self.schemas = schemas

        self._supported_actions = set([])

        super().__init__(*args, prefix=self.prefix, tags=self.tags, **kwargs)

    def list(
        self,
        path="/",
        *args,
        response_model=None,
        response_model_exclude_none=True,
        **kwargs,
    ):
        self._add_support("LIST")

        response_model = response_model or self.schemas["singleton"]

        def list_func(request: Request, session=Depends(get_session)):
            models = self.universe.list(session=session)

            #  return self._pre_validate(
            #      models, request=request, response_model=response_model
            #  )
            return models

        kwargs["response_model"] = List[response_model]
        kwargs["response_model_exclude_none"] = response_model_exclude_none

        return self._decorate(list_func, super().get, path, **kwargs)

    def _decorate(self, method_func, router_method, *args, **kwargs):
        def decorator(func):
            fixed_func = self._fix_doc(method_func, func)

            return router_method(
                *args,
                **kwargs,
            )(fixed_func)

        return decorator

    def create(
        self,
        path="/",
        *args,
        status_code=201,
        response_model=None,
        response_model_exclude_none=True,
        **kwargs,
    ):
        self._add_support("CREATE")

        response_model = response_model or self.schemas["singleton"]

        def decorator(func):
            def create_func(
                body: self.schemas["input"], request: Request, session=Depends(get_session)
            ):
                created_model = self.universe.create(body, session=session)

                # TODO: Look into whether there are good rules for the ordering of
                #       parameters and whether python has any good practices about when
                #       to use mandatory keyword parameters.
                #  return self._pre_validate(
                #      created_model, request=request, response_model=response_model
                #  )

                return created_model

            create_func = self._fix_doc(create_func, func)

            return super(DustyRouter, self).post(
                path,
                *args,
                status_code=status_code,
                response_model=response_model,
                response_model_exclude_none=response_model_exclude_none,
                **kwargs,
            )(create_func)

        return decorator

    def retrieve(
        self,
        path="/{id}",
        *args,
        response_model=None,
        response_model_exclude_none=True,
        **kwargs,
    ):
        self._add_support("RETRIEVE")

        # TODO: All things that link to list do so unconditionally, even if list isn't
        #       supported.
        response_model = response_model or self.schemas["singleton"]

        def decorator(func):
            # TODO: For descriptions, we could try to override this functions doc
            #       string with the doc string of the function passed in.
            def retrieve_func(
                id: int,
                request: Request,
                session=Depends(get_session),
            ):
                try:
                    retrieved_model = self.universe.retrieve(id, session=session)
                except NotFoundError:
                    raise HTTPException(status_code=404, detail="Not found")

                #  return self._pre_validate(
                #      retrieved_model, request=request, response_model=response_model
                #  )

                return retrieved_model

            # Cursed
            retrieve_func.__name__ = func.__name__

            return super(DustyRouter, self).get(
                path,
                *args,
                response_model=response_model,
                response_model_exclude_none=response_model_exclude_none,
                **kwargs,
            )(retrieve_func)

        return decorator

    def update(
        self,
        path="/{id}",
        *args,
        response_model=None,
        response_model_exclude_none=True,
        **kwargs,
    ):
        self._add_support("UPDATE")

        response_model = response_model or self.schemas["singleton"]

        def decorator(func):
            def update_func(
                id: int,
                body: self.schemas["input"],
                request: Request,
                session=Depends(get_session),
            ):
                try:
                    updated_model = self.universe.update(id, body, session=session)
                except NotFoundError:
                    raise HTTPException(status_code=404, detail="Not found")

                #  return self._pre_validate(
                #      updated_model, request=request, response_model=response_model
                #  )

                return updated_model

            update_func.__name__ = func.__name__

            return super(DustyRouter, self).put(
                path,
                *args,
                response_model=response_model,
                response_model_exclude_none=response_model_exclude_none,
                **kwargs,
            )(update_func)

        return decorator

    # TODO: Just take args and kwargs and use functions to set default arguments, so
    #       these default values can be shared.
    def destroy(
        self,
        path="/{id}",
        *args,
        response_model=None,
        response_model_exclude_none=True,
        **kwargs,
    ):
        # TODO: Hrmm I think this should be DESTROY
        self._add_support("DELETE")

        response_model = response_model or self.schemas["singleton"]

        def decorator(func):
            def destroy_func(
                id: int,
                request: Request,
                response: Response,
                session=Depends(get_session),
            ):
                try:
                    destroyed_model = self.universe.destroy(id, session=session)
                except NotFoundError:
                    pass

                #  return self._pre_validate(
                #      SimpleNamespace(), request=request, response_model=response_model
                #  )

                return destroyed_model

            destroy_func = self._fix_doc(destroy_func, func)

            return super(DustyRouter, self).delete(
                path,
                *args,
                response_model=response_model,
                response_model_exclude_none=response_model_exclude_none,
                **kwargs,
            )(destroy_func)

        return decorator

    def _add_support(self, supported_action):
        # TODO: Case statement is a code smell
        self._supported_actions.add(supported_action)

    @staticmethod
    def _fix_doc(broken_func, real_func):
        broken_func.__name__ = real_func.__name__

        return broken_func

    def get_router_context(self, request):
        url = request.url
        host_origin = f"{url.scheme}://{url.hostname}:{url.port}"

        return SimpleNamespace(
            host_origin=host_origin,
            doc_path=self.doc_path,
            rel=self.rel,
            path=self.prefix,
            supported_actions=self._supported_actions,
            input_schema=self.schema.Input,
        )

    def _pre_validate(self, obj, *, request, response_model):
        router_context = self.get_router_context(request)

        obj = response_model.pre_validate(router_context, obj)

        return obj
