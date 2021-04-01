from PyQt5 import QtWidgets, QtCore
from calc_ui import Ui_Dialog
from mathlib import *
import sys

def minus():
    ui.pushButton_minus.setText("AHOJ")
def plus():
    ui.lcdNumber.display(42)
    
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

ui.pushButton_minus.clicked.connect(minus)
ui.pushButton_plus.clicked.connect(plus)
Dialog.show()
sys.exit(app.exec_())
