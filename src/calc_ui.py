# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 270)
        Dialog.setMinimumSize(QtCore.QSize(250, 270))
        Dialog.setMaximumSize(QtCore.QSize(300, 270))
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.pushButton_one = QtWidgets.QPushButton(Dialog)
        self.pushButton_one.setGeometry(QtCore.QRect(0, 170, 50, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_one.setPalette(palette)
        self.pushButton_one.setObjectName("pushButton_one")
        self.pushButton_two = QtWidgets.QPushButton(Dialog)
        self.pushButton_two.setGeometry(QtCore.QRect(50, 170, 50, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_two.setPalette(palette)
        self.pushButton_two.setObjectName("pushButton_two")
        self.pushButton_three = QtWidgets.QPushButton(Dialog)
        self.pushButton_three.setGeometry(QtCore.QRect(100, 170, 50, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_three.setPalette(palette)
        self.pushButton_three.setObjectName("pushButton_three")
        self.pushButton_four = QtWidgets.QPushButton(Dialog)
        self.pushButton_four.setGeometry(QtCore.QRect(0, 120, 50, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_four.setPalette(palette)
        self.pushButton_four.setObjectName("pushButton_four")
        self.pushButton_five = QtWidgets.QPushButton(Dialog)
        self.pushButton_five.setGeometry(QtCore.QRect(50, 120, 50, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_five.setPalette(palette)
        self.pushButton_five.setObjectName("pushButton_five")
        self.pushButton_six = QtWidgets.QPushButton(Dialog)
        self.pushButton_six.setGeometry(QtCore.QRect(100, 120, 50, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_six.setPalette(palette)
        self.pushButton_six.setObjectName("pushButton_six")
        self.pushButton_seven = QtWidgets.QPushButton(Dialog)
        self.pushButton_seven.setGeometry(QtCore.QRect(0, 70, 50, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_seven.setPalette(palette)
        self.pushButton_seven.setObjectName("pushButton_seven")
        self.pushButton_eight = QtWidgets.QPushButton(Dialog)
        self.pushButton_eight.setGeometry(QtCore.QRect(50, 70, 50, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.pushButton_eight.setPalette(palette)
        self.pushButton_eight.setObjectName("pushButton_eight")
        self.pushButton_nine = QtWidgets.QPushButton(Dialog)
        self.pushButton_nine.setGeometry(QtCore.QRect(100, 70, 50, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_nine.setPalette(palette)
        self.pushButton_nine.setObjectName("pushButton_nine")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(1, 30, 298, 40))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(15)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(1, 0, 261, 30))
        self.lcdNumber_2.setDigitCount(20)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.pushButton_zero = QtWidgets.QPushButton(Dialog)
        self.pushButton_zero.setGeometry(QtCore.QRect(0, 220, 100, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 92, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_zero.setPalette(palette)
        self.pushButton_zero.setObjectName("pushButton_zero")
        self.pushButton_dot = QtWidgets.QPushButton(Dialog)
        self.pushButton_dot.setGeometry(QtCore.QRect(100, 220, 50, 50))
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_dot.setToolTip("Decimal point\nUsage: x.y")
        self.pushButton_dot.setToolTipDuration(4000)
        self.pushButton_clear = QtWidgets.QPushButton(Dialog)
        self.pushButton_clear.setGeometry(QtCore.QRect(250, 70, 50, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 163, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 163, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 163, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pushButton_clear.setPalette(palette)
        self.pushButton_clear.setToolTip("Clear \nClears all operations and numbers.\nShortcut: c")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_times = QtWidgets.QPushButton(Dialog)
        self.pushButton_times.setGeometry(QtCore.QRect(200, 220, 50, 50))
        self.pushButton_times.setToolTip("Times\nUsage: n x m\nShortcut: *")
        self.pushButton_times.setToolTipDuration(4000)
        self.pushButton_times.setObjectName("pushButton_times")
        self.pushButton_divide = QtWidgets.QPushButton(Dialog)
        self.pushButton_divide.setGeometry(QtCore.QRect(200, 170, 50, 50))
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_divide.setToolTip("Divide\nUsage: x/y\nwhere y != 0")
        self.pushButton_divide.setToolTipDuration(4000)
        self.pushButton_plus = QtWidgets.QPushButton(Dialog)
        self.pushButton_plus.setGeometry(QtCore.QRect(150, 220, 50, 50))
        self.pushButton_plus.setToolTip("Plus\nUsage: x+y")
        self.pushButton_plus.setToolTipDuration(4000)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_minus = QtWidgets.QPushButton(Dialog)
        self.pushButton_minus.setGeometry(QtCore.QRect(150, 170, 50, 50))
        self.pushButton_minus.setToolTip("Minus\nUsage: x-y")
        self.pushButton_minus.setToolTipDuration(4000)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_root = QtWidgets.QPushButton(Dialog)
        self.pushButton_root.setGeometry(QtCore.QRect(150, 70, 50, 50))
        self.pushButton_root.setToolTip("Nth root of x\nUsage: n√x\nShortcut: r")
        self.pushButton_root.setToolTipDuration(4000)
        self.pushButton_root.setText("√")
        self.pushButton_root.setObjectName("pushButton_root")
        self.pushButton_factorial = QtWidgets.QPushButton(Dialog)
        self.pushButton_factorial.setGeometry(QtCore.QRect(200, 120, 50, 50))
        self.pushButton_factorial.setToolTip("Factorial\nUsage: x!")
        self.pushButton_factorial.setToolTipDuration(4000)
        self.pushButton_factorial.setObjectName("pushButton_factorial")
        self.pushButton_combinations = QtWidgets.QPushButton(Dialog)
        self.pushButton_combinations.setGeometry(QtCore.QRect(200, 70, 50, 50))
        self.pushButton_combinations.setToolTip("Combination\nUsage: x nPr y\nWhere x >= y\nShortcut: n")
        self.pushButton_combinations.setToolTipDuration(4000)
        self.pushButton_combinations.setObjectName("pushButton_combinations")
        self.pushButton_equals = QtWidgets.QPushButton(Dialog)
        self.pushButton_equals.setGeometry(QtCore.QRect(250, 170, 50, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 163, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 163, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 163, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pushButton_equals.setPalette(palette)
        self.pushButton_equals.setToolTip("Evaluate the expression")
        self.pushButton_equals.setToolTipDuration(4000)
        self.pushButton_equals.setDefault(False)
        self.pushButton_equals.setFlat(False)
        self.pushButton_equals.setObjectName("pushButton_equals")
        self.pushButton_power = QtWidgets.QPushButton(Dialog)
        self.pushButton_power.setGeometry(QtCore.QRect(150, 120, 50, 50))
        self.pushButton_power.setToolTip("Power\nUsage: x^y")
        self.pushButton_power.setToolTipDuration(4000)
        self.pushButton_power.setObjectName("pushButton_power")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(265, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_one.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_two.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_three.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_four.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_five.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_six.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_seven.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_eight.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_nine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_zero.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_dot.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_plus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_minus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_power.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_root.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_combinations.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_factorial.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_divide.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_times.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_clear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_equals.setFocusPolicy(QtCore.Qt.NoFocus)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.pushButton_one.setText(_translate("Dialog", "1"))
        self.pushButton_one.setShortcut(_translate("Dialog", "1"))
        self.pushButton_two.setText(_translate("Dialog", "2"))
        self.pushButton_two.setShortcut(_translate("Dialog", "2"))
        self.pushButton_three.setText(_translate("Dialog", "3"))
        self.pushButton_three.setShortcut(_translate("Dialog", "3"))
        self.pushButton_four.setText(_translate("Dialog", "4"))
        self.pushButton_four.setShortcut(_translate("Dialog", "4"))
        self.pushButton_five.setText(_translate("Dialog", "5"))
        self.pushButton_five.setShortcut(_translate("Dialog", "5"))
        self.pushButton_six.setText(_translate("Dialog", "6"))
        self.pushButton_six.setShortcut(_translate("Dialog", "6"))
        self.pushButton_seven.setText(_translate("Dialog", "7"))
        self.pushButton_seven.setShortcut(_translate("Dialog", "7"))
        self.pushButton_eight.setText(_translate("Dialog", "8"))
        self.pushButton_eight.setShortcut(_translate("Dialog", "8"))
        self.pushButton_nine.setText(_translate("Dialog", "9"))
        self.pushButton_nine.setShortcut(_translate("Dialog", "9"))
        self.pushButton_zero.setText(_translate("Dialog", "0"))
        self.pushButton_zero.setShortcut(_translate("Dialog", "0"))
        self.pushButton_dot.setText(_translate("Dialog", "."))
        self.pushButton_dot.setShortcut(_translate("Dialog", "."))
        self.pushButton_clear.setText(_translate("Dialog", "C"))
        self.pushButton_clear.setShortcut(_translate("Dialog", "c"))
        self.pushButton_times.setText(_translate("Dialog", "x"))
        self.pushButton_times.setShortcut(_translate("Dialog", "*"))
        self.pushButton_times.setShortcut(_translate("Dialog", "*"))
        self.pushButton_divide.setText(_translate("Dialog", "/"))
        self.pushButton_divide.setShortcut(_translate("Dialog", "/"))
        self.pushButton_plus.setText(_translate("Dialog", "+"))
        self.pushButton_plus.setShortcut(_translate("Dialog", "+"))
        self.pushButton_minus.setText(_translate("Dialog", "-"))
        self.pushButton_minus.setShortcut(_translate("Dialog", "-"))
        self.pushButton_factorial.setText(_translate("Dialog", "!"))
        self.pushButton_factorial.setShortcut(_translate("Dialog", "!"))
        self.pushButton_combinations.setText(_translate("Dialog", "nPr"))
        self.pushButton_combinations.setShortcut(_translate("Dialog", "n"))
        self.pushButton_equals.setText(_translate("Dialog", "="))
        self.pushButton_equals.setShortcut(_translate("Dialog", "="))
        self.pushButton_power.setText(_translate("Dialog", "^"))
        self.pushButton_power.setShortcut(_translate("Dialog", "^"))
        self.pushButton_root.setShortcut(_translate("Dialog", "r"))
        self.label.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
