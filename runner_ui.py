# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runner.ui'
#
# Created: Thu Jun 26 19:57:51 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_runner(object):
    def setupUi(self, runner):
        runner.setObjectName("runner")
        runner.resize(544, 268)
        runner.setStyleSheet("#linkButton_1 {\n"
"    border:none;\n"
"    height: 30px;\n"
"    border-bottom: 1px solid black;\n"
"    padding-bottom: 10px;\n"
"}")
        self.centralwidget = QtGui.QWidget(runner)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 80, 291, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(303, 0, 241, 295))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.titleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleLabel.setStyleSheet("color: rgb(85, 85, 255);\n"
"font-size: 14px;\n"
"font-family: Arial;\n"
"font-weight: bold;")
        self.titleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.linkButton_1 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.linkButton_1.setStyleSheet("#linkButton_1 {\n"
"    border:none;\n"
"    height: 30px;\n"
"    border-bottom: 1px solid black;\n"
"    margin-top: -10px;\n"
"}")
        self.linkButton_1.setObjectName("linkButton_1")
        self.verticalLayout.addWidget(self.linkButton_1)
        self.linkButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.linkButton_2.setStyleSheet("#linkButton_2 {\n"
"    border:none;\n"
"    height: 30px;\n"
"    border-bottom: 1px solid black;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 10px;\n"
"}")
        self.linkButton_2.setObjectName("linkButton_2")
        self.verticalLayout.addWidget(self.linkButton_2)
        self.linkButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.linkButton_3.setStyleSheet("#linkButton_3 {\n"
"    border:none;\n"
"    height: 30px;\n"
"    border-bottom: 1px solid black;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 10px;\n"
"}")
        self.linkButton_3.setObjectName("linkButton_3")
        self.verticalLayout.addWidget(self.linkButton_3)
        self.linkButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.linkButton_4.setStyleSheet("#linkButton_4 {\n"
"    border:none;\n"
"    height: 30px;\n"
"    border-bottom: 1px solid black;\n"
"    padding-bottom: 10px;\n"
"    padding-top: 5px;\n"
"}")
        self.linkButton_4.setObjectName("linkButton_4")
        self.verticalLayout.addWidget(self.linkButton_4)
        self.linkButton_5 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.linkButton_5.setStyleSheet("#linkButton_5 {\n"
"    border:none;\n"
"    height: 30px;\n"
"    padding-bottom: 35px;\n"
"}")
        self.linkButton_5.setObjectName("linkButton_5")
        self.verticalLayout.addWidget(self.linkButton_5)
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setEnabled(False)
        self.startButton.setGeometry(QtCore.QRect(0, 130, 75, 23))
        self.startButton.setObjectName("startButton")
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 30, 291, 48))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nickEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.nickEdit.setObjectName("nickEdit")
        self.verticalLayout_2.addWidget(self.nickEdit)
        self.hostEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.hostEdit.setObjectName("hostEdit")
        self.verticalLayout_2.addWidget(self.hostEdit)
        runner.setCentralWidget(self.centralwidget)

        self.retranslateUi(runner)
        QtCore.QMetaObject.connectSlotsByName(runner)

    def retranslateUi(self, runner):
        runner.setWindowTitle(QtGui.QApplication.translate("runner", "Runner", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setText(QtGui.QApplication.translate("runner", "Otwórz", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("runner", "Otwórz plik samp.exe", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("runner", "Najnowsze tematy na Pawno.pl", None, QtGui.QApplication.UnicodeUTF8))
        self.linkButton_1.setText(QtGui.QApplication.translate("runner", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.linkButton_2.setText(QtGui.QApplication.translate("runner", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.linkButton_3.setText(QtGui.QApplication.translate("runner", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.linkButton_4.setText(QtGui.QApplication.translate("runner", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.linkButton_5.setText(QtGui.QApplication.translate("runner", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("runner", "START!", None, QtGui.QApplication.UnicodeUTF8))
        self.nickEdit.setPlaceholderText(QtGui.QApplication.translate("runner", "Wprowadź swój nick", None, QtGui.QApplication.UnicodeUTF8))
        self.hostEdit.setPlaceholderText(QtGui.QApplication.translate("runner", "Wprowadź IP oraz PORT serwera", None, QtGui.QApplication.UnicodeUTF8))

