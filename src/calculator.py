from PyQt5 import QtWidgets, QtCore
from calc_ui import Ui_Dialog
from mathlib import *
import sys

first_number = ""
second_number = ""

def number_clicked(value):
    global first_number
    first_number += value
    ui.lcdNumber.display(first_number)
    
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

#
ui.pushButton_one.clicked.connect(lambda: number_clicked("1"))
ui.pushButton_two.clicked.connect(lambda: number_clicked("2"))
ui.pushButton_three.clicked.connect(lambda: number_clicked("3"))
ui.pushButton_four.clicked.connect(lambda: number_clicked("4"))
ui.pushButton_five.clicked.connect(lambda: number_clicked("5"))
ui.pushButton_six.clicked.connect(lambda: number_clicked("6"))
ui.pushButton_seven.clicked.connect(lambda: number_clicked("7"))
ui.pushButton_eight.clicked.connect(lambda: number_clicked("8"))
ui.pushButton_nine.clicked.connect(lambda: number_clicked("9"))
ui.pushButton_zero.clicked.connect(lambda: number_clicked("0"))
ui.pushButton_dot.clicked.connect(lambda: number_clicked("."))
#
Dialog.show()
sys.exit(app.exec_())
