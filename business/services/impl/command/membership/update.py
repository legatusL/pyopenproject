import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand
from model.membership import Membership


class Update(MembershipCommand):

    def __init__(self, connection, membership):
        super(connection)
        self.membership = membership

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{self.membership.id}",
                                    json=json.dumps(self.membership.__dict__)).execute()
            return Membership(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating membership by id: {self.membership.id}") from re
