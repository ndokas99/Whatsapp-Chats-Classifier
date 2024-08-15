from os import remove
from re import findall, search
from sqlite3 import connect, OperationalError
from sys import argv, exit as exit_
from time import localtime, strftime

from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject, QSize, Qt, QProcess
from PyQt5.QtGui import QIcon, QColor, QBrush, QCursor, QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTabWidget, QFileDialog, QStatusBar, \
    QAction, QMenu, QMenuBar, QDialog, QProgressBar, QLabel, QPushButton, QTextBrowser, QListWidget, QListWidgetItem, \
    QLineEdit


class MainWindow(object):
    def __init__(self):
        self.centralWidget = QWidget(mainWindow)
        self.statusbar = QStatusBar(mainWindow)
        self.tabWidget = QTabWidget(self.centralWidget)
        self.Learning = QWidget(self.centralWidget)
        self.display0 = QWebEngineView(self.Learning)
        self.Advert = QWidget(self.centralWidget)
        self.display1 = QWebEngineView(self.Advert)
        self.Comps = QWidget(self.centralWidget)
        self.display2 = QWebEngineView(self.Comps)
        self.Politics = QWidget(self.centralWidget)
        self.display3 = QWebEngineView(self.Politics)
        self.Religion = QWidget(self.centralWidget)
        self.display4 = QWebEngineView(self.Religion)
        self.Science = QWidget(self.centralWidget)
        self.display5 = QWebEngineView(self.Science)
        self.Sports = QWidget(self.centralWidget)
        self.display6 = QWebEngineView(self.Sports)

        self.menubar = QMenuBar(mainWindow)
        self.menuFile = QMenu(self.menubar)
        self.menuHelp = QMenu(self.menubar)
        self.menuAbout = QMenu(self.menubar)
        self.menuView = QMenu(self.menubar)

        self.actionOpen = QAction(mainWindow)
        self.actionSave = QAction(mainWindow)
        self.actionQuit = QAction(mainWindow)
        self.actionManage_Saved = QAction(mainWindow)
        self.actionPosition_tabs_at_top = QAction(mainWindow)
        self.actionPosition_tabs_at_bottom = QAction(mainWindow)
        self.actionAbout_WhatappFilter = QAction(mainWindow)
        self.actionAbout_Creators = QAction(mainWindow)
        self.actionInterface_Help = QAction(mainWindow)
        self.actionFunctionality = QAction(mainWindow)

        self.loading = QDialog(mainWindow)
        self.loadingLabel = QLabel(self.loading)
        self.progressBar = QProgressBar(self.loading)

        self.writingProgress = QDialog(mainWindow)
        self._learn = QLabel(self.writingProgress)
        self._learnProg = QProgressBar(self.writingProgress)
        self._advert = QLabel(self.writingProgress)
        self._advertProg = QProgressBar(self.writingProgress)
        self._comps = QLabel(self.writingProgress)
        self._compsProg = QProgressBar(self.writingProgress)
        self._politics = QLabel(self.writingProgress)
        self._politicsProg = QProgressBar(self.writingProgress)
        self._religion = QLabel(self.writingProgress)
        self._religionProg = QProgressBar(self.writingProgress)
        self._science = QLabel(self.writingProgress)
        self._scienceProg = QProgressBar(self.writingProgress)
        self._sports = QLabel(self.writingProgress)
        self._sportsProg = QProgressBar(self.writingProgress)

        self.saveDialog = QDialog(mainWindow)
        self.saveLabel = QLabel(self.saveDialog)
        self.saveEdit = QLineEdit(self.saveDialog)
        self.warning = QLabel(self.saveDialog)
        self.saveButton = QPushButton(self.saveDialog)

        self.manageDialog = QDialog(mainWindow)
        self.savedLoad = QPushButton(self.manageDialog)
        self.savedDelete = QPushButton(self.manageDialog)
        self.savedList = QListWidget(self.manageDialog)
        self.manageLabel1 = QLabel(self.manageDialog)
        self.manageLabel2 = QLabel(self.manageDialog)
        self.saveName = QLabel(self.manageDialog)
        self.saveDate = QLabel(self.manageDialog)

        self.about1 = QDialog(mainWindow)
        self.browser1 = QTextBrowser(self.about1)
        self.okButton1 = QPushButton(self.about1)

        self.about2 = QDialog(mainWindow)
        self.browser2 = QTextBrowser(self.about2)
        self.okButton2 = QPushButton(self.about2)

        self.interHelp = QDialog(mainWindow)
        self.selection = QListWidget(self.interHelp)
        self.view = QTextBrowser(self.interHelp)
        self.interButton = QPushButton(self.interHelp)

        self.funcHelp = QDialog(mainWindow)
        self.funcView = QTextBrowser(self.funcHelp)
        self.funcButton = QPushButton(self.funcHelp)

        self.saves = connect("databases/saves.db")
        try:
            self.saves.execute("create table Dates (tableName text, datetime text);")
            self.saves.commit()
        except OperationalError:
            pass

        self.texts = connect("databases/textData.db")
        self.about = self.texts.execute("select html from About;").fetchall()
        self.help = self.texts.execute("select html from Help;").fetchall()
        self.labels = self.texts.execute("select html from Labels;").fetchall()
        self.tabs = self.texts.execute("select html from Display;").fetchall()
        self.saved = self.texts.execute("select html from Saves;").fetchall()

        self.msgs = [[] for _ in range(7)]
        self.displays = [self.display0, self.display1, self.display2, self.display3, self.display4,
                         self.display5, self.display6]
        self.bars = [self._learnProg, self._advertProg, self._compsProg, self._politicsProg,
                     self._religionProg, self._scienceProg, self._sportsProg]

        self.count = 0
        self.index = 0
        self.tableName = None
        self.next = None
        self.preprocessor = None
        self.tabWriter = None
        self.classifier = None
        self.input_data = None

    def setupUi(self, mainWin):
        mainWin.setObjectName("mainWindow")
        mainWin.resize(692, 634)
        mainWin.setMinimumSize(QSize(692, 634))
        mainWin.setMaximumSize(QSize(692, 634))
        mainWin.setWindowIcon(QIcon("media/Icon.png"))
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 691, 591))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.Learning.setObjectName("Learning")
        self.display0.setGeometry(QRect(0, 0, 681, 571))
        self.display0.setObjectName("display0")
        self.tabWidget.addTab(self.Learning, "")
        self.Advert.setObjectName("Advert")
        self.display1.setGeometry(QRect(0, 0, 681, 571))
        self.display1.setObjectName("display1")
        self.tabWidget.addTab(self.Advert, "")
        self.Comps.setObjectName("Comps")
        self.display2.setGeometry(QRect(0, 0, 691, 571))
        self.display2.setObjectName("display2")
        self.tabWidget.addTab(self.Comps, "")
        self.Politics.setObjectName("Politics")
        self.display3.setGeometry(QRect(0, 0, 681, 571))
        self.display3.setObjectName("display3")
        self.tabWidget.addTab(self.Politics, "")
        self.Religion.setObjectName("Religion")
        self.display4.setGeometry(QRect(0, 0, 691, 571))
        self.display4.setObjectName("display4")
        self.tabWidget.addTab(self.Religion, "")
        self.Science.setObjectName("Science")
        self.display5.setGeometry(QRect(0, 0, 681, 571))
        self.display5.setObjectName("display5")
        self.tabWidget.addTab(self.Science, "")
        self.Sports.setObjectName("Sports")
        self.display6.setGeometry(QRect(0, 0, 681, 571))
        self.display6.setObjectName("display6")
        self.tabWidget.addTab(self.Sports, "")
        mainWin.setCentralWidget(self.centralWidget)

        self.menubar.setGeometry(QRect(0, 0, 692, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile.setObjectName("menuFile")
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout.setObjectName("menuAbout")
        self.menuView.setObjectName("menuView")
        mainWin.setMenuBar(self.menubar)

        self.statusbar.setObjectName("statusbar")
        mainWin.setStatusBar(self.statusbar)

        self.actionAbout_WhatappFilter.setObjectName("actionAbout_WhatappFilter")
        self.actionAbout_Creators.setObjectName("actionAbout_Creator")
        self.actionInterface_Help.setObjectName("actionInterface_Help")
        self.actionFunctionality.setObjectName("actionFunctionality")
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave.setObjectName("actionSave")
        self.actionQuit.setObjectName("actionQuit")
        self.actionManage_Saved.setObjectName("actionManage_Saved")
        self.actionPosition_tabs_at_top.setCheckable(True)
        self.actionPosition_tabs_at_top.setChecked(True)
        self.actionPosition_tabs_at_top.setObjectName("actionPosition_tabs_at_top")
        self.actionPosition_tabs_at_bottom.setCheckable(True)
        self.actionPosition_tabs_at_bottom.setObjectName("actionPosition_tabs_at_bottom")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionManage_Saved)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionInterface_Help)
        self.menuHelp.addAction(self.actionFunctionality)
        self.menuAbout.addAction(self.actionAbout_WhatappFilter)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_Creators)
        self.menuView.addAction(self.actionPosition_tabs_at_top)
        self.menuView.addAction(self.actionPosition_tabs_at_bottom)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.loading.setObjectName("loading")
        self.loading.resize(419, 79)
        self.loading.setModal(True)
        self.loading.setMinimumSize(QSize(419, 79))
        self.loading.setMaximumSize(QSize(419, 79))
        self.loadingLabel.setGeometry(QRect(6, 0, 411, 41))
        self.loadingLabel.setObjectName("loadinglabel")
        self.progressBar.setGeometry(QRect(10, 40, 401, 23))
        self.progressBar.setObjectName("progressBar")

        self.writingProgress.setObjectName("writingProgress")
        self.writingProgress.resize(410, 299)
        self.writingProgress.setModal(True)
        self.writingProgress.setWindowIcon(QIcon("media/write.png"))
        self.writingProgress.setMinimumSize(QSize(410, 299))
        self.writingProgress.setMaximumSize(QSize(410, 299))
        self._learn.setGeometry(QRect(-4, 0, 421, 31))
        self._learn.setObjectName("_learn")
        self._learnProg.setGeometry(QRect(10, 25, 401, 16))
        self._learnProg.setProperty("value", 0)
        self._learnProg.setObjectName("_learnProg")
        self._advert.setGeometry(QRect(-4, 35, 421, 41))
        self._advert.setObjectName("_advert")
        self._advertProg.setGeometry(QRect(10, 65, 401, 16))
        self._advertProg.setProperty("value", 0)
        self._advertProg.setObjectName("_advertProg")
        self._comps.setGeometry(QRect(-4, 65, 421, 61))
        self._comps.setObjectName("_comps")
        self._compsProg.setGeometry(QRect(10, 106, 401, 16))
        self._compsProg.setProperty("value", 0)
        self._compsProg.setObjectName("_compsProg")
        self._politics.setGeometry(QRect(-10, 120, 431, 31))
        self._politics.setObjectName("_politics")
        self._politicsProg.setGeometry(QRect(10, 145, 401, 16))
        self._politicsProg.setProperty("value", 0)
        self._politicsProg.setObjectName("_politicsProg")
        self._religion.setGeometry(QRect(-10, 160, 431, 31))
        self._religion.setObjectName("_religion")
        self._religionProg.setGeometry(QRect(10, 186, 401, 16))
        self._religionProg.setProperty("value", 0)
        self._religionProg.setObjectName("_religionProg")
        self._science.setGeometry(QRect(0, 210, 411, 21))
        self._science.setObjectName("_science")
        self._scienceProg.setGeometry(QRect(10, 231, 401, 16))
        self._scienceProg.setProperty("value", 0)
        self._scienceProg.setObjectName("_scienceProg")
        self._sports.setGeometry(QRect(-4, 225, 421, 81))
        self._sports.setObjectName("_sports")
        self._sportsProg.setGeometry(QRect(10, 275, 401, 16))
        self._sportsProg.setProperty("value", 0)
        self._sportsProg.setObjectName("_sportsProg")

        self.saveDialog.setObjectName("saveDialog")
        self.saveDialog.resize(265, 118)
        self.saveDialog.setMinimumSize(QSize(265, 118))
        self.saveDialog.setMaximumSize(QSize(265, 118))
        self.saveLabel.setGeometry(QRect(70, 0, 121, 31))
        self.saveLabel.setObjectName("saveLabel")
        self.saveEdit.setGeometry(QRect(10, 30, 241, 31))
        self.saveEdit.setObjectName("saveEdit")
        self.warning.setGeometry(QRect(70, 59, 131, 31))
        self.warning.setStyleSheet("color: red;")
        self.warning.setObjectName("warning")
        self.saveButton.setGeometry(QRect(95, 92, 75, 21))
        self.saveButton.setObjectName("saveButton")

        self.manageDialog.setObjectName("manageDialog")
        self.manageDialog.resize(440, 241)
        self.manageDialog.setMinimumSize(QSize(440, 241))
        self.manageDialog.setMaximumSize(QSize(440, 241))
        self.manageDialog.setModal(True)
        self.savedLoad.setGeometry(QRect(80, 200, 91, 31))
        self.savedLoad.setObjectName("savedLoad")
        self.savedDelete.setGeometry(QRect(310, 200, 91, 31))
        self.savedDelete.setObjectName("savedDelete")
        self.savedList.setGeometry(QRect(10, 10, 231, 181))
        self.savedList.setObjectName("listWidget")
        self.manageLabel1.setGeometry(QRect(250, 10, 181, 31))
        self.manageLabel1.setObjectName("manageLabel1")
        self.manageLabel2.setGeometry(QRect(250, 100, 181, 31))
        self.manageLabel2.setObjectName("manageLabel2")
        self.saveName.setGeometry(QRect(250, 50, 181, 21))
        self.saveName.setText("")
        self.saveName.setObjectName("saveName")
        self.saveDate.setGeometry(QRect(250, 140, 181, 21))
        self.saveDate.setText("")
        self.saveDate.setObjectName("saveDate")

        self.about1.setObjectName("AboutApp")
        self.about1.resize(391, 339)
        self.about1.setMinimumSize(QSize(391, 339))
        self.about1.setMaximumSize(QSize(391, 339))
        self.about1.setModal(True)
        self.browser1.setGeometry(QRect(0, 0, 391, 291))
        self.browser1.setObjectName("browser1")
        self.okButton1.setGeometry(QRect(160, 300, 61, 31))
        self.okButton1.setObjectName("okButton1")

        self.about2.setObjectName("AboutCreator")
        self.about2.resize(391, 288)
        self.about2.setMinimumSize(QSize(391, 288))
        self.about2.setMaximumSize(QSize(391, 288))
        self.about2.setModal(True)
        self.browser2.setGeometry(QRect(0, 0, 391, 241))
        self.browser2.setObjectName("browser2")
        self.okButton2.setGeometry(QRect(160, 250, 61, 31))
        self.okButton2.setObjectName("okButton2")

        self.interHelp.setObjectName("interHelp")
        self.interHelp.resize(546, 430)
        self.interHelp.setMinimumSize(QSize(546, 430))
        self.interHelp.setMaximumSize(QSize(546, 430))
        self.interHelp.setModal(True)
        self.selection.setGeometry(QRect(10, 10, 171, 291))
        self.selection.setObjectName("selection")
        item = QListWidgetItem()
        item.setFlags(Qt.NoItemFlags)
        self.selection.addItem(item)
        for _ in range(3):
            item = QListWidgetItem()
            self.selection.addItem(item)
        item = QListWidgetItem()
        brush = QBrush(QColor(195, 195, 195))
        brush.setStyle(Qt.Dense4Pattern)
        item.setBackground(brush)
        item.setFlags(Qt.NoItemFlags)
        self.selection.addItem(item)
        item = QListWidgetItem()
        item.setFlags(Qt.NoItemFlags)
        self.selection.addItem(item)
        for _ in range(2):
            item = QListWidgetItem()
            self.selection.addItem(item)
        item = QListWidgetItem()
        brush = QBrush(QColor(195, 195, 195))
        brush.setStyle(Qt.Dense4Pattern)
        item.setBackground(brush)
        item.setFlags(Qt.NoItemFlags)
        self.selection.addItem(item)
        item = QListWidgetItem()
        item.setFlags(Qt.NoItemFlags)
        self.selection.addItem(item)
        for _ in range(2):
            item = QListWidgetItem()
            self.selection.addItem(item)
        item = QListWidgetItem()
        brush = QBrush(QColor(195, 195, 195))
        brush.setStyle(Qt.Dense4Pattern)
        item.setBackground(brush)
        item.setFlags(Qt.NoItemFlags)
        self.selection.addItem(item)
        item = QListWidgetItem()
        item.setFlags(Qt.NoItemFlags)
        self.selection.addItem(item)
        for _ in range(2):
            item = QListWidgetItem()
            self.selection.addItem(item)
        self.view.setGeometry(QRect(190, 10, 351, 411))
        self.view.setObjectName("view")
        self.interButton.setGeometry(QRect(60, 350, 75, 31))
        self.interButton.setObjectName("interButton")

        self.funcHelp.setObjectName("funcHelp")
        self.funcHelp.resize(538, 470)
        self.funcHelp.setMinimumSize(QSize(546, 430))
        self.funcHelp.setMaximumSize(QSize(546, 430))
        self.funcHelp.setModal(True)
        self.funcView.setGeometry(QRect(0, 10, 541, 411))
        self.funcView.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.funcView.setObjectName("funcView")
        self.funcButton.setGeometry(QRect(230, 430, 75, 31))
        self.funcButton.setObjectName("funcButton")

        self.retranslateUi(mainWin)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(mainWin)

    def retranslateUi(self, mainWin):
        _translate = QCoreApplication.translate
        mainWin.setWindowTitle(_translate("mainWindow", "Whatsapp Filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Learning), _translate("mainWindow", "School Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Advert), _translate("mainWindow", "Advertisement"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Comps),
                                  _translate("mainWindow", "Computers and Tech"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Politics), _translate("mainWindow", "Politics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Religion), _translate("mainWindow", "Religion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Science),
                                  _translate("mainWindow", "Science"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sports), _translate("mainWindow", "Sports"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))
        self.menuAbout.setTitle(_translate("mainWindow", "About"))
        self.menuView.setTitle(_translate("mainWindow", "View"))

        self.actionAbout_WhatappFilter.setText(_translate("mainWindow", "About WhatappFilter"))
        self.actionAbout_WhatappFilter.setStatusTip(_translate("mainWindow", "View information about application"))
        self.actionAbout_WhatappFilter.triggered.connect(self.about1.show)

        self.actionAbout_Creators.setText(_translate("mainWindow", "About Creator"))
        self.actionAbout_Creators.setStatusTip(_translate("mainWindow", "View information about the application\'s "
                                                                        "creator"))
        self.actionAbout_Creators.triggered.connect(self.about2.show)

        self.actionInterface_Help.setText(_translate("mainWindow", "Interface Help"))
        self.actionInterface_Help.setStatusTip(_translate("mainWindow", "View help about user interface"))
        self.actionInterface_Help.triggered.connect(self.interHelp.show)

        self.actionFunctionality.setText(_translate("mainWindow", "Functionality Help"))
        self.actionFunctionality.setStatusTip(_translate("mainWindow", "View help about how application works"))
        self.actionFunctionality.triggered.connect(self.funcHelp.show)

        self.actionOpen.setText(_translate("mainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("mainWindow", "Open new chat"))
        self.actionOpen.triggered.connect(self.open)

        self.actionSave.setText(_translate("mainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("mainWindow", "Save results to database"))
        self.actionSave.triggered.connect(self.saveDialog.show)
        self.actionSave.setEnabled(False)

        self.actionManage_Saved.setText(_translate("mainWindow", "Manage Saved"))
        self.actionManage_Saved.setStatusTip(_translate("mainWindow", "View and Delete saved results"))
        self.actionManage_Saved.triggered.connect(self.manageDialog.show)

        self.actionQuit.setText(_translate("mainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("mainWindow", "Close the application"))
        self.actionQuit.triggered.connect(exit_)

        self.actionPosition_tabs_at_top.setText(_translate("mainWindow", "Position tabs at top"))
        self.actionPosition_tabs_at_top.setStatusTip(_translate("mainWindow", "Position tabs at top"))
        self.actionPosition_tabs_at_top.triggered.connect(self.switchTop)

        self.actionPosition_tabs_at_bottom.setText(_translate("mainWindow", "Position tabs at bottom"))
        self.actionPosition_tabs_at_bottom.setStatusTip(_translate("mainWindow", "Position tabs at bottom"))
        self.actionPosition_tabs_at_bottom.triggered.connect(self.switchBottom)

        self.next = _translate("loading", self.labels[2][0])

        self.saveDialog.setWindowTitle(_translate("saveDialog", "SaveAs"))
        self.saveLabel.setText(_translate("saveDialog", self.labels[0][0]))
        self.saveButton.setText(_translate("saveDialog", "Save"))
        self.saveButton.clicked.connect(self.save)

        self.manageDialog.setWindowTitle(_translate("manageDialog", "Manage Saves"))
        self.savedLoad.setText(_translate("manageDialog", "LOAD"))
        self.savedLoad.clicked.connect(self.load)
        self.savedDelete.setText(_translate("manageDialog", "DELETE"))
        self.savedDelete.clicked.connect(lambda: self.delete(_translate))
        self.savedList.setSortingEnabled(True)
        self.savedList.itemClicked.connect(lambda: self.showDetails(_translate))
        self.manageLabel1.setText(_translate("manageDialog", self.saved[0][0]))
        self.manageLabel2.setText(_translate("manageDialog", self.saved[1][0]))
        self.insert(_translate)

        self.about1.setWindowTitle(_translate("AboutApp", "About Whatsapp Filter"))
        self.browser1.setHtml(_translate("AboutApp", self.about[0][0]))
        self.okButton1.setText(_translate("AboutApp", "OK"))
        self.okButton1.clicked.connect(self.about1.close)

        self.about2.setWindowTitle(_translate("AboutCreators", "About Creator"))
        self.browser2.setHtml(_translate("AboutCreators", self.about[1][0]))
        self.okButton2.setText(_translate("AboutCreators", "OK"))
        self.okButton2.clicked.connect(self.about2.close)

        self.funcHelp.setWindowTitle(_translate("funcHelp", "Functionality Help"))
        self.funcView.setHtml(_translate("funcHelp", self.help[-1][0]))
        self.funcButton.setText(_translate("funcHelp", "OK"))

        self.interHelp.setWindowTitle(_translate("interHelp", "Interface Help"))
        __sortingEnabled = self.selection.isSortingEnabled()
        self.selection.setSortingEnabled(False)
        item = self.selection.item(0)
        item.setText(_translate("interHelp", "File"))
        item = self.selection.item(1)
        item.setText(_translate("interHelp", "     Open"))
        item = self.selection.item(2)
        item.setText(_translate("interHelp", "     Save"))
        item = self.selection.item(3)
        item.setText(_translate("interHelp", "     Manage Saved"))
        item = self.selection.item(5)
        item.setText(_translate("interHelp", "View"))
        item = self.selection.item(6)
        item.setText(_translate("interHelp", "     Position tabs at top"))
        item = self.selection.item(7)
        item.setText(_translate("interHelp", "     Position tabs at bottom"))
        item = self.selection.item(9)
        item.setText(_translate("interHelp", "Help"))
        item = self.selection.item(10)
        item.setText(_translate("interHelp", "     Functionality Help"))
        item = self.selection.item(11)
        item.setText(_translate("interHelp", "     Interface Help"))
        item = self.selection.item(13)
        item.setText(_translate("interHelp", "About"))
        item = self.selection.item(14)
        item.setText(_translate("interHelp", "     About Whatsapp Filter"))
        item = self.selection.item(15)
        item.setText(_translate("interHelp", "     About Creator"))
        self.selection.setSortingEnabled(__sortingEnabled)
        self.view.setHtml(_translate("interHelp", self.help[0][0]))
        self.interButton.setText(_translate("interHelp", "OK"))
        self.interButton.clicked.connect(self.interHelp.close)
        self.selection.itemClicked.connect(lambda: self.interfaceClick(_translate))

        self.writingProgress.setWindowTitle(_translate("writingProgress", "Writing content..."))
        self._learn.setText(_translate("writingProgress", self.labels[3][0]))
        self._advert.setText(_translate("writingProgress", self.labels[4][0]))
        self._comps.setText(_translate("writingProgress", self.labels[5][0]))
        self._politics.setText(_translate("writingProgress", self.labels[6][0]))
        self._religion.setText(_translate("writingProgress", self.labels[7][0]))
        self._science.setText(_translate("writingProgress", self.labels[8][0]))
        self._sports.setText(_translate("writingProgress", self.labels[9][0]))

    def switchTop(self):
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.actionPosition_tabs_at_top.setChecked(True)
        self.actionPosition_tabs_at_bottom.setChecked(False)

    def switchBottom(self):
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.actionPosition_tabs_at_top.setChecked(False)
        self.actionPosition_tabs_at_bottom.setChecked(True)

    def interfaceClick(self, trans):
        current = self.selection.currentItem().text()
        for i in range(1, 4):
            if current == self.selection.item(i).text():
                self.view.setHtml(trans("interHelp", self.help[i - 1][0]))
                app.processEvents()
                return
        for i in range(6, 8):
            if current == self.selection.item(i).text():
                self.view.setHtml(trans("interHelp", self.help[i - 3][0]))
                app.processEvents()
                return
        for i in range(10, 12):
            if current == self.selection.item(i).text():
                self.view.setHtml(trans("interHelp", self.help[i - 5][0]))
                app.processEvents()
                return
        for i in range(14, 16):
            if current == self.selection.item(i).text():
                self.view.setHtml(trans("interHelp", self.help[i - 7][0]))
                app.processEvents()
                return

    def reset(self):
        self.msgs = [[] for _ in range(7)]
        self.count = 0
        self.index = 0

    def LoadingWin(self):
        _translate = QCoreApplication.translate
        self.loading.setWindowIcon(QIcon("media/convert.png"))
        self.loadingLabel.setText(_translate("loading", self.labels[1][0]))
        self.loading.setWindowTitle(_translate("loading", "Please Wait..."))
        self.progressBar.setValue(0)
        self.loading.show()
        app.processEvents()

    def open(self):
        file = QFileDialog.getOpenFileName(mainWindow, "Open File", filter="*.txt")

        if file != ("", ""):
            array = findall(r"\d{1,2}/\d{1,2}/\d{1,4}, \d{1,2}:\d{1,2}",
                            open(file[0], "r", encoding="utf-8").read(10000))

            if len(array) < 5:
                msg = "This file may not produce desired results as system does not recognize it as a Whatsapp chat " \
                      "log.\nDo you wish to proceed? "
                message = QMessageBox.warning(mainWindow, "Processing Issues", msg, QMessageBox.Yes | QMessageBox.No)
                if message == QMessageBox.Yes:
                    pass
                else:
                    return

            self.reset()
            self.LoadingWin()
            self.preprocessor = QProcess()
            self.preprocessor.readyReadStandardOutput.connect(self.increment)
            self.preprocessor.readyReadStandardError.connect(self.config)
            self.preprocessor.finished.connect(lambda: self.runModel(file))
            self.preprocessor.start("python", ["components/preprocessor.py", file[0]])
            #  self.preprocessor.start("bin/preprocessor.exe", [file[0]])

    def config(self):
        data = self.preprocessor.readAllStandardError()
        value = bytes(data).decode("utf-8")
        try:
            self.progressBar.setMaximum(int(value))
        except ValueError:
            with open("logs/Preprocessor Errors.log", "w") as e:
                e.write(f"{value}\n")
        app.processEvents()

    def increment(self):
        self.count += 1
        self.progressBar.setValue(self.count)
        app.processEvents()

    def runModel(self, file):
        self.preprocessor.close()
        self.loading.setWindowIcon(QIcon("media/model.png"))
        self.loadingLabel.setText(self.next)
        self.progressBar.setValue(0)
        app.processEvents()

        self.input_data = open("temp/processed.txt", "r", encoding="utf-8").read().split(":~:")
        self.progressBar.setMaximum(len(self.input_data))
        self.classifier = QProcess()
        self.classifier.readyReadStandardOutput.connect(self.classify)
        self.classifier.finished.connect(lambda: self.write(file))
        self.classifier.start("python", ["components/classifier.py"])
        #  self.classifier.start("bin/classifier.exe")

    def classify(self):
        data = self.classifier.readAllStandardOutput()
        value = int(bytes(data).decode("utf-8")[0])
        self.msgs[value].append(self.input_data[self.index])
        self.progressBar.setValue(self.index + 1)
        self.index += 1
        app.processEvents()

    def write(self, file):
        self.classifier.close()
        start = self.tabs[0][0]
        end = self.tabs[1][0]
        for (i, bar) in zip(range(7), self.bars):
            bar.setMaximum(len(self.msgs[i]))
            bar.setValue(0)
            app.processEvents()

        self.loading.close()
        with open("temp/state", "w", encoding="utf-8") as state:
            state.write(f"{start}:<arg>:{end}:<arg>:{file[0]}:<arg>:{self.msgs}")
        self.writingProgress.show()
        app.processEvents()

        self.tabWriter = QProcess()
        self.tabWriter.readyReadStandardOutput.connect(self.increaseBars)
        self.tabWriter.readyReadStandardError.connect(self.diagnose)
        self.tabWriter.finished.connect(self.ended)
        self.tabWriter.start("python", ["components/tabWriter.py"])
        #  self.tabWriter.start("bin/tabWriter.exe")

    def increaseBars(self):
        data = self.tabWriter.readAllStandardOutput()
        value = bytes(data).decode("utf-8")
        try:
            index, val = value.split(" ")
        except ValueError:
            return
        index, val = int(index), int(val)
        self.bars[index].setValue(val)
        app.processEvents()

    def diagnose(self):
        data = self.tabWriter.readAllStandardError()
        value = bytes(data).decode("utf-8")
        with open("logs/Writer Errors.log", "w") as e:
            e.write(f"{value}\n")

    def ended(self):
        self.tabWriter.close()
        remove("temp/state")
        for i in range(7):
            html = open(f"temp/{i}", "r", encoding="utf-8").read()
            self.displays[i].setHtml(html)
            remove(f"temp/{i}")
        self.actionSave.setEnabled(True)
        self.writingProgress.close()

    def save(self):
        self.tableName = self.saveEdit.text()
        if search(r"^(\s*)$", self.tableName):
            self.warning.setText("Name should not be blank")
            self.warning.setVisible(True)
        else:
            try:
                self.saves.execute(f"create table \"{self.tableName}\"(html text);")
                date = strftime("%a, %d %b %Y %H:%M:%S", localtime())
                self.saves.execute(f"insert into Dates values (?,?);", (self.tableName, date))
                jsScript = 'document.getElementsByTagName("html")[0].outerHTML'
                for i in range(7):
                    self.displays[i].page().runJavaScript(jsScript, self.writeSave)
                self.warning.setVisible(False)
                self.reinsert()
                self.saveDialog.close()
            except OperationalError:
                self.warning.setText("Name already exists.")
                self.warning.setVisible(True)

    def writeSave(self, html):
        self.saves.execute(f"insert into \"{self.tableName}\" values (?);", (html,))
        self.saves.commit()

    def insert(self, trans):
        command = "select name from sqlite_master where type=='table' and name!='Dates';"
        saves = [x[0] for x in self.saves.execute(command).fetchall()]
        for name in saves:
            item = QListWidgetItem()
            item.setText(trans("manageDialog", name))
            font = QFont()
            font.setFamily("Tahoma")
            item.setFont(font)
            self.savedList.addItem(item)

    def reinsert(self):
        self.savedList.reset()
        _translate = QCoreApplication.translate
        self.insert(_translate)

    def showDetails(self, trans):
        name = self.savedList.currentItem().text()
        date = self.saves.execute("select datetime from Dates where tableName==?", (name,)).fetchall()[0][0]
        self.saveName.setText(trans("manageDialog", self.saved[2][0] + name + self.saved[3][0]))
        self.saveDate.setText(trans("manageDialog", self.saved[2][0] + date + self.saved[3][0]))

    def load(self):
        try:
            name = self.savedList.currentItem().text()
            command = f"select html from \"{name}\";"
            content = [x[0] for x in self.saves.execute(command).fetchall()]
            for i in range(7):
                self.displays[i].setHtml(content[i])
            self.actionSave.setEnabled(True)
            self.manageDialog.close()
            app.processEvents()
        except AttributeError:
            pass

    def delete(self, trans):
        try:
            deleted = self.savedList.currentItem().text()
            identity = self.savedList.currentRow()
            self.savedList.takeItem(identity)
            self.saves.execute(f"drop table \"{deleted}\";")
            self.saves.commit()
            self.saves.execute(f"delete from Dates where tableName==\"{deleted}\";")
            self.saves.commit()
            self.saves.execute("vacuum;")
            self.saves.commit()
            try:
                name = self.savedList.currentItem().text()
                date = self.saves.execute("select datetime from Dates where tableName==?;", (name,)).fetchall()[0][0]
                self.saveName.setText(trans("manageDialog", self.saved[2][0] + name + self.saved[3][0]))
                self.saveDate.setText(trans("manageDialog", self.saved[2][0] + date + self.saved[3][0]))
            except AttributeError:
                self.saveName.setText("")
                self.saveDate.setText("")
            finally:
                app.processEvents()
        except AttributeError:
            pass
        finally:
            app.processEvents()


if __name__ == "__main__":
    app = QApplication(argv)
    mainWindow = QMainWindow()
    ui = MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    exit_(app.exec_())
