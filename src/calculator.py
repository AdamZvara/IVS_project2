from PyQt5 import QtWidgets, QtCore
from calc_ui import Ui_Dialog
from mathlib import *
import sys

first_number = ""
second_number = ""

def evaluate():
    global first_number
    global second_number
    operation = ui.label.text()
    if operation == "+":
        first_number = str(add(float(first_number), float(second_number)))
    elif operation == "-":
        first_number = str(sub(float(first_number), float(second_number)))
    elif operation == "!":
        first_number = str(fact(float(second_number)))
    elif operation == "/":
        first_number = str(div(float(first_number), float(second_number)))
    elif operation == "x":
        first_number = str(mul(float(first_number), float(second_number)))
    elif operation == "^":
        first_number = str(prw(float(first_number), float(second_number)))
    elif operation == "√":
        first_number = str(root(float(second_number), float(first_number)))
    elif operation == "n":
        first_number = str(root(float(second_number), float(first_number)))
    ui.lcdNumber_2.display(first_number)
    second_number = ""
    ui.lcdNumber.display("")

def operation_clicked(value):
    global first_number
    global second_number
    if (ui.lcdNumber.value() != 0) and (ui.lcdNumber_2.value() != 0):
        evaluate()
    else:
        first_number = second_number
        second_number = ""
        ui.lcdNumber_2.display(first_number)
        ui.lcdNumber.display(second_number)
        
    ui.label.setText(value)

def number_clicked(value):
    global second_number
    second_number += value
    ui.lcdNumber.display(second_number)
    
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
ui.pushButton_plus.clicked.connect(lambda: operation_clicked(ui.pushButton_plus.text()))
ui.pushButton_minus.clicked.connect(lambda: operation_clicked(ui.pushButton_minus.text()))
ui.pushButton_times.clicked.connect(lambda: operation_clicked(ui.pushButton_times.text()))
ui.pushButton_power.clicked.connect(lambda: operation_clicked(ui.pushButton_power.text()))
ui.pushButton_root.clicked.connect(lambda: operation_clicked(ui.pushButton_root.text()))
ui.pushButton_combinations.clicked.connect(lambda: operation_clicked(ui.pushButton_combinations.text()))
ui.pushButton_factorial.clicked.connect(lambda: operation_clicked(ui.pushButton_factorial.text()))
ui.pushButton_divide.clicked.connect(lambda: operation_clicked(ui.pushButton_divide.text()))
#
Dialog.show()
sys.exit(app.exec_())
