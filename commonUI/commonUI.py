from PyQt5 import QtWidgets, QtGui
from LeagueManagerUI import Ui_LeagueManager
from league_database.league_database import LeagueDatabase


class commonUI:
    _theDatabase = None

    def loadTeams(self, LeagueUI):
        self._theDatabase = LeagueDatabase()
        self._theDatabase.load("./testleague.txt")
        i = 0
        for league in self._theDatabase.leagues:
            LeagueUI.tableView.insertRow(i)
            LeagueUI.tableView.setItem(i, 0, QtGui.QTableWidgetItem(league.name))
            LeagueUI.tableView.setItem(i, 1, QtGui.QTableWidgetItem(league.teams))
            LeagueUI.tableView.setItem(i, 1, QtGui.QTableWidgetItem("Delete or Edit"))

    def setupUI(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        LeagueManager = QtWidgets.QMainWindow()
        ui = Ui_LeagueManager()
        ui.setupUi(LeagueManager)
        LeagueManager.show()
        ui.SaveButton.clicked.connect(lambda: self.loadTeams(ui))
        sys.exit(app.exec_())
