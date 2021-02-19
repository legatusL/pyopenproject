from business.services.impl.command.query.create import Create
from business.services.impl.command.query.create_form import CreateForm
from business.services.impl.command.query.delete import Delete
from business.services.impl.command.query.find import Find
from business.services.impl.command.query.find_all import FindAll
from business.services.impl.command.query.find_by_context import FindByContext
from business.services.impl.command.query.schema import Schema
from business.services.impl.command.query.star import Star
from business.services.impl.command.query.unstar import Unstar
from business.services.impl.command.query.update import Update
from business.services.query_service import QueryService


class QueryServiceImpl(QueryService):

    def find_by_context(self, context):
        raise FindByContext(context).execute()

    def __init__(self, connection):
        super().__init__(connection)

    def update(self, query):
        return Update(self.connection, query).execute()

    def find(self, query, offset=None, page_size=None, filters=None, columns=None, sort_by=None, group_by=None,
             show_sums=None, timeline_visible=None, timeline_labels=None, timeline_zoom_level=None,
             highlighting_mode=None, highlighted_attributes=None, show_hierarchies=None):
        return Find(self.connection, query, offset, page_size, filters, columns, sort_by, group_by,
                    show_sums, timeline_visible, timeline_labels, timeline_zoom_level,
                    highlighting_mode, highlighted_attributes, show_hierarchies).execute()

    def delete(self, query):
        return Delete(self.connection, query).execute()

    def star(self, query):
        return Star(self.connection, query).execute()

    def unstar(self, query):
        return Unstar(self.connection, query).execute()

    def find_all(self, filters=None):
        return list(FindAll(self.connection, filters).execute())

    def create(self, query):
        return Create(self.connection, query).execute()

    def create_form(self, form):
        return CreateForm(self.connection, form).execute()

    def schema(self):
        return Schema(self.connection).execute()
