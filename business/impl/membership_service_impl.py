from business.impl.command.membership.find_all import FindAll
from business.impl.command.membership.find import Find
from business.impl.command.membership.update import Update
from business.impl.command.membership.create import Create
from business.impl.command.membership.delete import Delete
from business.impl.command.membership.find_schema import FindSchema
from business.impl.command.membership.find_available import FindAvailable

from business.membership_service import MembershipService


class MembershipServiceImpl(MembershipService):

    def find_all(self, filters):
        return FindAll(filters).execute()

    def find(self):
        return Find(self).execute()

    def update_membership(self, membership):
        return Update(self, membership).execute()

    def delete_membership(self, membership):
        Delete(self, membership)

    def new_membership(self, membership):
        return Create(self, membership).execute()

    def membership_schema(self):
        return FindSchema(self).execute()

    def available_memberships(self):
        return FindAvailable(self).execute

    def new_membership_form(self): raise NotImplementedError


    def update_membership_form(self): raise NotImplementedError
