##
# @file calculator.py
# @brief Integration of mathlib and gui
# @author Vojtech Eichler (xeichl01)

from PyQt5 import QtWidgets, QtCore
from calc_ui import Ui_Dialog
from mathlib import *
import sys

first_number = ""
second_number = ""

##
# @brief Function to clear displayed values and stored numbers
#
def clear():
    global first_number
    global second_number
    first_number = ""
    second_number = ""
    ui.lcdNumber.display("")
    ui.lcdNumber_2.display("")
    ui.label.setText("")

##
# @brief Displays an error message
#
def error():
    global second_number
    clear()
    second_number = "error"

##
# @brief Calls function from mathlib according to operation chosen by user.
#
def evaluate():
    global first_number
    global second_number
    operation = ui.label.text()
    try:
        if operation == "+":
            second_number = str(add(float(first_number), float(second_number)))
        elif operation == "-":
            second_number = str(sub(float(first_number), float(second_number)))
        elif operation == "!":
            if float(first_number).is_integer():
                second_number = str(fact(int(float(first_number))))
            else:
                error()
        elif operation == "/":
            second_number = str(div(float(first_number), float(second_number)))
        elif operation == "x":
            second_number = str(mul(float(first_number), float(second_number)))
        elif operation == "^":
            if float(second_number).is_integer():
                second_number = str(prw(float(first_number), int(float(second_number))))
            else:
                error()
        elif operation == "√":
            if float(first_number).is_integer():
                second_number = str(root(float(second_number), int(float(first_number))))
            else:
                error()
        elif operation == "nPr":
            if float(first_number).is_integer() and float(second_number).is_integer():
                second_number = str(comb(int(float(first_number)), int(float(second_number))))
            else:
                error()

    except ValueError:
        error()
    ui.lcdNumber.display(second_number)
    first_number = ""
    ui.lcdNumber_2.display("")
    ui.label.setText("=")

##
# @brief Set operation depending on which button was clicked
#
# @param value Text of clicked button
#
def operation_clicked(value):
    global first_number
    global second_number
    ##
    # If two numbers are already given, evaluate, then insert operation
    #
    if (ui.lcdNumber.value() != 0) and (ui.lcdNumber_2.value() != 0):
        evaluate()
        ui.lcdNumber_2.display(ui.lcdNumber.value())
        ui.lcdNumber.display("")
        first_number = second_number
        second_number = ""
    else:
        first_number = second_number
        second_number = ""
        ui.lcdNumber_2.display(first_number)
        ui.lcdNumber.display(second_number)
        
    ui.label.setText(value)
##
# @brief Appends number to input display
#
# @param value Text of clicked button
#
def number_clicked(value):
    global second_number
    if ui.label.text() == '=':
        second_number = ""
        ui.label.setText("")
    second_number += value
    ui.lcdNumber.display(second_number)

##
# Window initialization
#
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

##
# Button initialization
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
ui.pushButton_equals.clicked.connect(lambda: evaluate())
ui.pushButton_clear.clicked.connect(lambda: clear())

Dialog.show()
sys.exit(app.exec_())
