from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.status.status_command import StatusCommand
from model.status import Status


class FindByContext(StatusCommand):

    def __init__(self, connection):
        super(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            return Status(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding status by context: {self.CONTEXT}") from re
