from .exceptions import NotFoundError


# Future: Complex logic to determine what queries are available can be contained here
# Future: Theoretically, this could be used in a hierarchical relationship as the
#       further down the hierarchy, the more the universe could be filtered.
# Refactor: Maybe universes should be responsible for telling the routers that they need
#       a session and what kind? Look for some kind of pattern that fits this.
#       - A simple way to handle this might be to define a static get_session function
#         that the router can depend on however it pleases.
class SQLAlchemyUniverse:
    def filter(self, session):
        """Return the objects relating to all rows in the table."""
        return session.query(self.model_cls)

    def list(self, *, session):
        """Return the objects relating to all rows within the universe."""
        return self.filter(session=session).all()

    def create(self, body, *, session):
        """Insert a new row into the table and return the object related to it."""
        new_obj = self._pydantic_to_sql(body)

        session.add(new_obj)
        session.commit()

        return new_obj

    def retrieve(self, id: int, *, session):
        """Select a row by its primary key and return the object related to it."""
        existing_obj = self.filter(session).get(id)

        if existing_obj is None:
            raise NotFoundError()

        return existing_obj

    # TODO: Should update be renamed to "replace"?
    def update(self, id: int, body, *, session):
        """
        Replace a row with the given primary key by a row corresponding to the given
        object, and then return an object related to the replaced row.
        """
        existing_obj = self.retrieve(id, session=session)

        new_obj = self._pydantic_to_sql(body)
        new_obj.id = existing_obj.id

        # We can have the new query replace the one with the same id by using
        # session.merge
        session.merge(new_obj, load=True)
        session.commit()

        return new_obj

    def destroy(self, id: int, *, session):
        """
        Delete the row with the given primary key and return the object that was related
        to it.
        """
        existing_obj = self.retrieve(id, session=session)

        session.delete(existing_obj)
        session.commit()

        return existing_obj

    def _pydantic_to_sql(self, pydantic_model):
        return self.model_cls(**pydantic_model.dict())
