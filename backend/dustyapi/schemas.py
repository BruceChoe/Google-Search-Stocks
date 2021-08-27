from typing import Optional, Dict, Union, List
from types import SimpleNamespace
from abc import ABC, abstractmethod

from pydantic import BaseModel, Field


# TODO: Perhaps Pydantic models should be left for validation and another component
#       should be responsible for adding links, embedded resources, and templates.
# TODO: Properly handle HAL-Forms with the required _templates and the automatic change
#       of content type to HAL if no _templates.
# TODO: Look into the proper way to handle multiple possible validation outputs. Perhaps
#       just make response_model a Union of the different types?


# TODO: Make these inner classes.
class Link(BaseModel):
    # These values come from the HAL draft
    href: str
    templated: Optional[bool]
    type: Optional[str]
    deprecation: Optional[str]
    name: Optional[str]


class Property(BaseModel):
    # Only supporting core property attributes from the HAL-Forms draft for now
    name: str
    prompt: Optional[str]
    readOnly: Optional[bool]
    regex: Optional[str]
    required: Optional[bool]
    templated: Optional[bool]
    value: Optional[str]


class Template(BaseModel):
    # These values come from the HAL-Forms draft
    contentType: Optional[str]
    method: str
    properties: Optional[List[Property]]
    target: Optional[str]
    title: Optional[str]


# class QueryCreate(QueryBase):
#     def to_db(self):
#         return models.Query(color=self.color, breed=self.breed)


class HAL(BaseModel):
    links: Optional[Dict[str, Union[Link, List[Link]]]] = Field(alias="_links")
    # TODO: Can this be more strongly typed than dict?
    embedded: Optional[dict] = Field(alias="_embedded")
    # TODO: Technically, per the HAL forms draft, this should not be optional, but this
    #       would currently add way too much complexity so we're ignoring that for now.
    templates: Optional[Dict[str, Template]] = Field(alias="_templates")


class HALHelper(HAL, ABC):
    @classmethod
    @abstractmethod
    def pre_validate(cls, router_context, obj):
        pass


def define_curies(router_context):
    rel_string = "{rel}"

    return [
        Link(
            name="doc",
            href=f"{router_context.host_origin}{router_context.doc_path}/{rel_string}",
            templated=True,
        )
    ]


def define_list_link(router_context):
    return Link(href=router_context.path)


def define_self_link(router_context, id):
    return Link(href=f"{router_context.path}/{id}")


def link_to_list(router_context):
    curies = define_curies(router_context)
    list_link = define_list_link(router_context)

    return {
        "curies": curies,
        f"doc:{router_context.rel}": list_link,
    }


def link_to_self_and_list(router_context, id):
    curies = define_curies(router_context)
    list_link = define_list_link(router_context)
    self_link = define_self_link(router_context, id)

    if "LIST" not in router_context.supported_actions:
        return {"self": self_link}

    return {
        "curies": curies,
        "self": self_link,
        f"doc:{router_context.rel}": list_link,
    }


class InputTemplate(Template):
    def __init__(self, input_schema, *, previous=None, **kwargs):
        properties = []

        for attr, field in input_schema.__fields__.items():
            if previous is not None:
                value = str(getattr(previous, attr))
            else:
                value = None

            properties.append(Property(name=attr, required=field.required, value=value))

        super().__init__(properties=properties, **kwargs)


class UpdateTemplate(InputTemplate):
    def __init__(self, input_schema, *, previous=None, **kwargs):
        super().__init__(input_schema, previous=previous, method="PUT")


class HALRetrieved(HALHelper):
    @classmethod
    def pre_validate(cls, router_context, obj):
        obj._links = link_to_self_and_list(router_context, obj.id)

        obj._templates = {}

        def default_if_only_action_or(alternative, *, actions):
            if len(actions) == 1:
                return "default"

            return alternative

        if "UPDATE" in router_context.supported_actions:
            key = default_if_only_action_or(
                "update", actions=router_context.supported_actions
            )

            obj._templates[key] = UpdateTemplate(
                router_context.input_schema, previous=obj
            )

        if "DELETE" in router_context.supported_actions:
            key = default_if_only_action_or(
                "delete", actions=router_context.supported_actions
            )

            obj._templates[key] = Template(method="DELETE")

        return obj


class HALList(HALHelper):
    @classmethod
    def pre_validate(cls, router_context, obj_list):
        obj_list = [cls.Header.pre_validate(router_context, obj) for obj in obj_list]
        obj_list = [cls.Header.from_orm(obj) for obj in obj_list]

        curies = define_curies(router_context)
        self_link = Link(href=router_context.path)

        links = {"self": self_link, "curies": curies}

        if "RETRIEVE" in router_context.supported_actions:
            id_string = "{id}"
            links["find"] = Link(
                href=f"{router_context.path}/{id_string}", templated=True
            )

        # TODO: Forgot about create form.

        embedded = {f"doc:{router_context.rel}": obj_list}

        return SimpleNamespace(_links=links, _embedded=embedded)

    class HALHeader(HALHelper):
        @classmethod
        def pre_validate(cls, router_context, obj):
            self_link = Link(href=f"{router_context.path}/{obj.id}")

            obj._links = {"self": self_link}

            return obj


class HALUpdated(HALHelper):
    @classmethod
    def pre_validate(cls, router_context, obj):
        obj._links = link_to_self_and_list(router_context, obj.id)

        return obj


class HALCreated(HALUpdated):
    pass


class HALDestroyed(HALHelper):
    @classmethod
    def pre_validate(cls, router_context, obj):
        obj._links = link_to_list(router_context)

        return obj
