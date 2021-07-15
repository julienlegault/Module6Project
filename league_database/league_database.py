import os
import pickle
import csv

from league.league import League
from team.team import Team
from team_member.team_member import TeamMember


class LeagueDatabase:
    _sole_instance = None

    def __new__(cls):
        cls.leagues = []
        cls._last_oid = 0
        cls.file_name = None
        if cls._sole_instance is None:
            cls._sole_instance = super(LeagueDatabase, cls).__new__(cls)
        return cls._sole_instance

    def instance(self):
        if self._sole_instance:
            return self._sole_instance
        else:
            self._sole_instance = super(LeagueDatabase, self).__new__(self)

    def load(self, file_name):
        try:
            tempfile = open(file_name, 'rb')
        except:
            print('File not found, loading backup...')
            try:
                tempfile = open(file_name + '.backup', 'rb')
            except:
                print('Backup file not found')
                return
        self.leagues = pickle.load(tempfile)
        self.file_name = file_name
        tempfile.close()

    def add_league(self, league):
        self.leagues.append(league)

    def next_oid(self):
        self._last_oid = self._last_oid + 1
        pass

    def save(self, file_name):
        if os.path.isfile(file_name):
            os.rename(file_name, file_name + '.backup')
        tempfile = open(file_name, 'wb')
        pickle.dump(self.leagues, tempfile)
        tempfile.close()
        pass

    def import_league(self, league_name, file_name):
        templeague = League(self.next_oid(), league_name)
        try:
            with open(file_name, 'r') as csv_file:
                csvtoread = csv.reader(csv_file)
                next(csvtoread)
                members = {}
                for row in csvtoread:
                    try:
                        members[row[0]].append(TeamMember(self.next_oid(), row[1], row[2]))
                    except:
                        print('There was an error importing your data')
                for item in members:
                    tempteam = Team(self.next_oid(), item.key())
                    for teammate in members.get(item):
                        try:
                            tempteam.addMember(teammate)
                        except:
                            print('Unable to add a singular member to the team.')
                    templeague.add_team(tempteam)
        except:
            print('There was an error reading your file')

    def export_league(self, league, file_name):
        try:
            with open(file_name, 'w') as csv_file:
                csvtowrite = csv.writer(csv_file)
                csvtowrite.writerow(['Team name', 'Member name', 'Member email'])
                for team in league.teams:
                    for member in team.members:
                        csvtowrite.writerow([team.name, member.name, member.email])
        except:
            print('There was an error writing your league to the file')