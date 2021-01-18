from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.custom_action.custom_action_command import CustomActionCommand
from model.custom_action import CustomAction


class Execute(CustomActionCommand):

    def __init__(self, connection, custom_action):
        super(connection)
        self.custom_action = custom_action

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.custom_action._links['self']['href']}/execute",
                                   json=self.custom_action.__dict__).execute()
            return CustomAction(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error executing custom_action:"
                                f" {self.custom_action._links['self']['href']}/execute") from re
