from IdentifiedObject.IdentifiedObject import IdentifiedObject


class Competition(IdentifiedObject):

    def __init__(self, oid, teams, location, datetime):
        super().__init__(oid)
        self.teams_competing = teams
        self.location = location
        self.date_time = datetime

    def send_email(self, emailer, subject, message):
        recipients = []
        for i in range(len(self.teams_competing)):
            for j in range(len(self.teams_competing[i].members)):
                recipients.append(self.teams_competing[i].members[j].email)

        return emailer.send_plain_email(recipients, subject, message)

    def __str__(self):
        if self.date_time is not None:
            return "Competition at " + self.location + " on " + str(self.date_time) + " with " + str(
                len(self.teams_competing)) + " teams"
        else:
            return "Competition at " + self.location + " with " + str(len(self.teams_competing)) + " teams"
