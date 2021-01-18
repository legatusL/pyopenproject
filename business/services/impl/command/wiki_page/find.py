from model.wiki_page import WikiPage

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.wiki_page.wiki_command import WikiPageCommand


class Find(WikiPageCommand):

    def __init__(self, connection, wiki_page):
        super(connection)
        self.wiki_page = wiki_page

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.wiki_page.id}").execute()
            return WikiPage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding wiki_page by ID: {self.wiki_page.id}") from re
