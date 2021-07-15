from IdentifiedObject.IdentifiedObject import IdentifiedObject
from DuplicateChecks.DuplicateChecks import DuplicateEmail


class Team(IdentifiedObject):

    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self.members = []

    def add_member(self, member):
        if member.email in [x.email for x in self.members]:
            raise DuplicateEmail
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def send_email(self, emailer, subject, message):
        return emailer.send_plain_email([x.email for x in self.members], subject, message)

    def __str__(self):
        return self.name + ": " + str(len(self.members)) + " members"
