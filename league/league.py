from IdentifiedObject.IdentifiedObject import IdentifiedObject


class League(IdentifiedObject):

    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self.teams = []
        self.competitions = []

    def add_team(self, team):
        self.teams.append(team)

    def add_competition(self, competition):
        self.competitions.append(competition)

    def teams_for_member(self, member):
        return [x for x in self.teams if member in x.members]

    def competitions_for_team(self, team):
        return [x for x in self.competitions if team in x.teams_competing]

    def competitions_for_member(self, member):
        result = []
        for i in range(len(self.competitions)):
            for j in range(len(self.competitions[i].teams_competing)):
                if member in self.competitions[i].teams_competing[j].members:
                    result.append(self.competitions[i])
        return result

    def __str__(self):
        return self.name + ": " + len(self.teams) + " teams, " + len(self.competitions) + " competitions"
