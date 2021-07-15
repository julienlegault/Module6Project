import sys

from PyQt5 import QtWidgets

from commonUI.LeagueManagerUI import Ui_LeagueManager

app = QtWidgets.QApplication(sys.argv)
LeagueManager = QtWidgets.QMainWindow()
ui = Ui_LeagueManager()
ui.setupUi(LeagueManager)
ui.LoadButton.clicked.connect(lambda: ui.loadLeague())
ui.AddButton.clicked.connect(lambda: ui.AddLeagueModal())
ui.SaveButton.clicked.connect(lambda: ui.SaveLeagues())
ui.BackButton.setVisible(False)
LeagueManager.show()
sys.exit(app.exec_())
