# -*- coding: utf-8 -*-

import sys
import urllib
import subprocess
import webbrowser
import logging
import traceback
from bs4 import BeautifulSoup
from PySide.QtCore import *
from PySide.QtGui import *
from runner_ui import Ui_runner


logging.basicConfig(filename="runner.log",
                    format="%(asctime)-15s: %(name)-18s - %(levelname)-8s - %(module)-15s - %(funcName)-20s - %(lineno)-6d - %(message)s",
                    level=logging.DEBUG)

logger = logging.getLogger(name="main-gui")

class Runner(QMainWindow, Ui_runner):
    def __init__(self, parent=None):
        super(Runner, self).__init__( parent)
        self.setupUi(self)

        logger.debug("Application initialized")

        self.settings = QSettings("settings.ini", QSettings.IniFormat)

        self.load_thread = LinksThread()
        self.load_thread.start()
        self.load_thread.finished.connect(self.setLinks)

        self.lineEdit.setText(QDir.toNativeSeparators(self.settings.value("sampPath")))
        self.ipEdit.setText(self.settings.value("IP"))
        self.portEdit.setText(self.settings.value("Port"))
        self.check()

        self.ipEdit.editingFinished.connect(self.check)
        self.ipEdit.returnPressed.connect(self.check)
        self.portEdit.editingFinished.connect(self.check)
        self.portEdit.returnPressed.connect(self.check)

        self.openButton.clicked.connect(self.open)

        self.startButton.clicked.connect(self.openSamp)

        self.linkButton_1.clicked.connect(self.url_1)
        self.linkButton_2.clicked.connect(self.url_2)
        self.linkButton_3.clicked.connect(self.url_3)
        self.linkButton_4.clicked.connect(self.url_4)
        self.linkButton_5.clicked.connect(self.url_5)

    def check(self):
        if self.lineEdit.text()[-8:] == "samp.exe":
            if self.ipEdit.text() == "":
                self.label.setText(u"Wprowadź IP serwera!")
            elif self.portEdit.text() == "":
                self.label.setText(u"Wprowadź PORT serwera!")
            else:
                self.settings.setValue("sampPath", self.lineEdit.text())
                self.settings.setValue("IP", self.ipEdit.text())
                self.settings.setValue("Port", self.portEdit.text())
                self.label.setText(u"SAMP został załadowany poprawnie,\nwciśnij START, aby połączyć się z serwerem.")
                self.startButton.setEnabled(True)
        else:
            self.label.setText(u"Zła ścieżka do pliku samp.exe.\nPodaj poprawną!")

    def url_1(self):
        webbrowser.open(self.load_thread.topics[0][0])
    def url_2(self):
        webbrowser.open(self.load_thread.topics[1][0])
    def url_3(self):
        webbrowser.open(self.load_thread.topics[2][0])
    def url_4(self):
        webbrowser.open(self.load_thread.topics[3][0])
    def url_5(self):
        webbrowser.open(self.load_thread.topics[4][0])

    def setLinks(self):
        self.linkButton_1.setText(self.load_thread.topics[0][1])
        self.linkButton_2.setText(self.load_thread.topics[1][1])
        self.linkButton_3.setText(self.load_thread.topics[2][1])
        self.linkButton_4.setText(self.load_thread.topics[3][1])
        self.linkButton_5.setText(self.load_thread.topics[4][1])

    def open(self):
        file_path = QFileDialog.getOpenFileName()
        self.lineEdit.setText(QDir.toNativeSeparators(file_path[0]))
        self.lineEdit.setReadOnly(True)

        self.label.setText(file_path[0])
        self.check()

    def openSamp(self):
        samp_exe = self.lineEdit.text()
        ip = self.ipEdit.text()
        port = self.portEdit.text()
        subprocess.call(samp_exe + " " + ip + ":" + port)

class LinksThread(QThread):

    topics = []

    def __init__(self):
        super(LinksThread, self).__init__()

    def run(self):
        page = urllib.urlopen('http://pawno.pl/')
        soup = BeautifulSoup(page.read())
        data = []

        for item in soup.find_all('ul', class_='ipsList_withminiphoto'):
            if len(item['class']) == 1:
                data.append(item)

        links = BeautifulSoup(str(data).decode('utf-8'))

        for l in links.find_all('a', class_='ipsType_small'):
            self.topics.append([l['href'], l.text])

        return self.topics

def unhandled_exception(type, value, exp_traceback):
    exception = "".join(traceback.format_exception(type, value, exp_traceback))
    logger.critical(str(exception))
    sys.exit(1)

if __name__ == '__main__':
    QCoreApplication.setApplicationName("Runner")
    QCoreApplication.setApplicationVersion("0.1 Alpha")
    QCoreApplication.setOrganizationName("KrainaBantu")
    QCoreApplication.setOrganizationDomain("krainabantu.blogspot.com")

    sys.excepthook = unhandled_exception

    app = QApplication(sys.argv)
    myapp = Runner()
    myapp.show()
    sys.exit(app.exec_())