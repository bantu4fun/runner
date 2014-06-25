# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runner.ui'
#
# Created: Wed Jun 25 16:13:39 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_runner(object):
    def setupUi(self, runner):
        runner.setObjectName("runner")
        runner.resize(544, 268)
        self.centralwidget = QtGui.QWidget(runner)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 31))
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
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 90, 321, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 0, 224, 261))
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
"    border: none;\n"
"}")
        self.linkButton_1.setObjectName("linkButton_1")
        self.verticalLayout.addWidget(self.linkButton_1)
        self.link_1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.link_1.setEnabled(True)
        self.link_1.setObjectName("link_1")
        self.verticalLayout.addWidget(self.link_1)
        self.linkButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.linkButton_2.setStyleSheet("#linkButton_2 {\n"
"    border: none;\n"
"}")
        self.linkButton_2.setObjectName("linkButton_2")
        self.verticalLayout.addWidget(self.linkButton_2)
        self.link_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.link_2.setEnabled(True)
        self.link_2.setObjectName("link_2")
        self.verticalLayout.addWidget(self.link_2)
        self.linkButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.linkButton_3.setStyleSheet("#linkButton_3 {\n"
"    border: none;\n"
"}")
        self.linkButton_3.setObjectName("linkButton_3")
        self.verticalLayout.addWidget(self.linkButton_3)
        self.link_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.link_3.setEnabled(True)
        self.link_3.setObjectName("link_3")
        self.verticalLayout.addWidget(self.link_3)
        self.linkButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.linkButton_4.setStyleSheet("#linkButton_4 {\n"
"    border: none;\n"
"}")
        self.linkButton_4.setObjectName("linkButton_4")
        self.verticalLayout.addWidget(self.linkButton_4)
        self.link_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.link_4.setEnabled(True)
        self.link_4.setObjectName("link_4")
        self.verticalLayout.addWidget(self.link_4)
        self.linkButton_5 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.linkButton_5.setStyleSheet("#linkButton_5 {\n"
"    border: none;\n"
"}")
        self.linkButton_5.setObjectName("linkButton_5")
        self.verticalLayout.addWidget(self.linkButton_5)
        self.link_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.link_5.setEnabled(True)
        self.link_5.setObjectName("link_5")
        self.verticalLayout.addWidget(self.link_5)
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setEnabled(False)
        self.startButton.setGeometry(QtCore.QRect(0, 140, 75, 23))
        self.startButton.setObjectName("startButton")
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 30, 321, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ipEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.ipEdit.setObjectName("ipEdit")
        self.verticalLayout_2.addWidget(self.ipEdit)
        self.portEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.portEdit.setObjectName("portEdit")
        self.verticalLayout_2.addWidget(self.portEdit)
        runner.setCentralWidget(self.centralwidget)

        self.retranslateUi(runner)
        QtCore.QMetaObject.connectSlotsByName(runner)

    def retranslateUi(self, runner):
        runner.setWindowTitle(QtGui.QApplication.translate("runner", "Runner", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setText(QtGui.QApplication.translate("runner", "Otwórz", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("runner", "Najnowsze tematy na Pawno.pl", None, QtGui.QApplication.UnicodeUTF8))
        self.linkButton_1.setText(QtGui.QApplication.translate("runner", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.link_1.setText(QtGui.QApplication.translate("runner", "_____________________________________", None, QtGui.QApplication.UnicodeUTF8))
        self.linkButton_2.setText(QtGui.QApplication.translate("runner", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.link_2.setText(QtGui.QApplication.translate("runner", "_____________________________________", None, QtGui.QApplication.UnicodeUTF8))
        self.linkButton_3.setText(QtGui.QApplication.translate("runner", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.link_3.setText(QtGui.QApplication.translate("runner", "_____________________________________", None, QtGui.QApplication.UnicodeUTF8))
        self.linkButton_4.setText(QtGui.QApplication.translate("runner", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.link_4.setText(QtGui.QApplication.translate("runner", "_____________________________________", None, QtGui.QApplication.UnicodeUTF8))
        self.linkButton_5.setText(QtGui.QApplication.translate("runner", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.link_5.setText(QtGui.QApplication.translate("runner", "_____________________________________", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("runner", "START!", None, QtGui.QApplication.UnicodeUTF8))
        self.ipEdit.setPlaceholderText(QtGui.QApplication.translate("runner", "Ustaw IP serwera", None, QtGui.QApplication.UnicodeUTF8))
        self.portEdit.setPlaceholderText(QtGui.QApplication.translate("runner", "Ustaw port serwera", None, QtGui.QApplication.UnicodeUTF8))

