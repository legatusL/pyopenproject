import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand
from model.membership import Membership


class Create(MembershipCommand):

    def __init__(self, connection, membership):
        super(connection)
        self.membership = membership

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}",
                                   json=json.dumps(self.membership.__dict__)).execute()
            return Membership(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating membership") from re
