import sys

from PyQt5 import QtWidgets

from commonUI.LeagueManagerUI import Ui_LeagueManager

app = QtWidgets.QApplication(sys.argv)
LeagueManager = QtWidgets.QMainWindow()
ui = Ui_LeagueManager()
ui.setupUi(LeagueManager)
ui.LoadButton.clicked.connect(lambda: ui.loadTeams())
ui.AddButton.clicked.connect(lambda: ui.Add_League_Modal())
LeagueManager.show()
sys.exit(app.exec_())
