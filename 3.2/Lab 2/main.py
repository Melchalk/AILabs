import sys
from PyQt5 import QtWidgets
from mywindow import MyWindow

app = QtWidgets.QApplication([])

application = MyWindow()
application.show()

sys.exit(app.exec())