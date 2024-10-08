from Views.login import *
from Controllers.UserController import *

import sys
app = QtWidgets.QApplication(sys.argv)
login = QtWidgets.QMainWindow()
ui = Ui_login()
ui.setupUi(login)
login.show()
sys.exit(app.exec_())
