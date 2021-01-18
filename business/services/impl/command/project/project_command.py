from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class ProjectCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/projects"

    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def execute(self): raise NotImplementedError
