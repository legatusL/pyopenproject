from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.work_package.work_package_command import WorkPackageCommand
from pyopenproject.model import attachment as att
import os
import json


class AddAttachment(WorkPackageCommand):

    def __init__(self, connection, work_package, filename, description, file_path):
        super().__init__(connection)
        self.work_package = work_package
        self.filename = filename
        self.description = description
        with open(file=file_path, mode='rb') as f:
            self.file_content = f.read()
            self.file_path = os.path.abspath(f.name)
            
    def execute(self):
        try:
            metadata = {"fileName": self.filename, "description": {"raw": self.description}}
            json_obj = PostRequest(connection=self.connection,
                        context=f"{self.CONTEXT}/{self.work_package.id}/attachments",
                                    files={
                                       'file': ('attachment', self.file_content),
                                       'metadata': (None, json.dumps(metadata))
                                   }).execute()
            return att.Attachment(json_obj)

        except RequestError as re:
            raise BusinessError(f"Error adding new attachment: {self.attachment.title}") from re
