# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainfrm.ui'
#
# Created: Thu Mar 13 14:00:45 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1121, 704)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineName = QtGui.QLineEdit(self.centralwidget)
        self.lineName.setObjectName(_fromUtf8("lineName"))
        self.horizontalLayout.addWidget(self.lineName)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.timestamp = QtGui.QDateTimeEdit(self.centralwidget)
        self.timestamp.setObjectName(_fromUtf8("timestamp"))
        self.horizontalLayout.addWidget(self.timestamp)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupPreview = QtGui.QGroupBox(self.centralwidget)
        self.groupPreview.setObjectName(_fromUtf8("groupPreview"))
        self.gridLayout = QtGui.QGridLayout(self.groupPreview)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableBiomass = QtGui.QTableView(self.groupPreview)
        self.tableBiomass.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableBiomass.setAlternatingRowColors(True)
        self.tableBiomass.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableBiomass.setSortingEnabled(True)
        self.tableBiomass.setObjectName(_fromUtf8("tableBiomass"))
        self.tableBiomass.horizontalHeader().setVisible(False)
        self.tableBiomass.horizontalHeader().setCascadingSectionResizes(True)
        self.tableBiomass.horizontalHeader().setStretchLastSection(True)
        self.tableBiomass.verticalHeader().setCascadingSectionResizes(True)
        self.tableBiomass.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableBiomass, 4, 1, 1, 1)
        self.checkReports = QtGui.QCheckBox(self.groupPreview)
        self.checkReports.setChecked(True)
        self.checkReports.setObjectName(_fromUtf8("checkReports"))
        self.gridLayout.addWidget(self.checkReports, 3, 4, 1, 1)
        self.tableImages = QtGui.QTableView(self.groupPreview)
        self.tableImages.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableImages.setAlternatingRowColors(True)
        self.tableImages.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableImages.setObjectName(_fromUtf8("tableImages"))
        self.tableImages.horizontalHeader().setVisible(False)
        self.tableImages.horizontalHeader().setCascadingSectionResizes(True)
        self.tableImages.horizontalHeader().setStretchLastSection(True)
        self.tableImages.verticalHeader().setVisible(True)
        self.tableImages.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.tableImages, 4, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupPreview)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 2, 1)
        self.tableReports = QtGui.QTableView(self.groupPreview)
        self.tableReports.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableReports.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableReports.setObjectName(_fromUtf8("tableReports"))
        self.tableReports.horizontalHeader().setVisible(False)
        self.tableReports.horizontalHeader().setCascadingSectionResizes(True)
        self.tableReports.horizontalHeader().setStretchLastSection(True)
        self.tableReports.verticalHeader().setVisible(True)
        self.tableReports.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.tableReports, 4, 4, 1, 1)
        self.checkBiomass = QtGui.QCheckBox(self.groupPreview)
        self.checkBiomass.setChecked(True)
        self.checkBiomass.setObjectName(_fromUtf8("checkBiomass"))
        self.gridLayout.addWidget(self.checkBiomass, 3, 1, 1, 1)
        self.checkGeom = QtGui.QCheckBox(self.groupPreview)
        self.checkGeom.setChecked(True)
        self.checkGeom.setObjectName(_fromUtf8("checkGeom"))
        self.gridLayout.addWidget(self.checkGeom, 3, 2, 1, 1)
        self.checkImages = QtGui.QCheckBox(self.groupPreview)
        self.checkImages.setChecked(True)
        self.checkImages.setObjectName(_fromUtf8("checkImages"))
        self.gridLayout.addWidget(self.checkImages, 3, 3, 1, 1)
        self.tableGeom = QtGui.QTableView(self.groupPreview)
        self.tableGeom.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableGeom.setAlternatingRowColors(True)
        self.tableGeom.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableGeom.setObjectName(_fromUtf8("tableGeom"))
        self.tableGeom.horizontalHeader().setVisible(False)
        self.tableGeom.horizontalHeader().setCascadingSectionResizes(True)
        self.tableGeom.horizontalHeader().setStretchLastSection(True)
        self.tableGeom.verticalHeader().setVisible(True)
        self.tableGeom.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.tableGeom, 4, 2, 1, 1)
        self.treeView = QtGui.QTreeView(self.groupPreview)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAnimated(True)
        self.treeView.setWordWrap(True)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout.addWidget(self.treeView, 4, 0, 1, 1)
        self.lbCurPath = QtGui.QLabel(self.groupPreview)
        self.lbCurPath.setObjectName(_fromUtf8("lbCurPath"))
        self.gridLayout.addWidget(self.lbCurPath, 5, 0, 1, 1)
        self.lbBiomass = QtGui.QLabel(self.groupPreview)
        self.lbBiomass.setObjectName(_fromUtf8("lbBiomass"))
        self.gridLayout.addWidget(self.lbBiomass, 5, 1, 1, 1)
        self.lbImages = QtGui.QLabel(self.groupPreview)
        self.lbImages.setObjectName(_fromUtf8("lbImages"))
        self.gridLayout.addWidget(self.lbImages, 5, 3, 1, 1)
        self.lbGeometry = QtGui.QLabel(self.groupPreview)
        self.lbGeometry.setObjectName(_fromUtf8("lbGeometry"))
        self.gridLayout.addWidget(self.lbGeometry, 5, 2, 1, 1)
        self.lbText = QtGui.QLabel(self.groupPreview)
        self.lbText.setObjectName(_fromUtf8("lbText"))
        self.gridLayout.addWidget(self.lbText, 5, 4, 1, 1)
        self.lbTotal = QtGui.QLabel(self.groupPreview)
        self.lbTotal.setObjectName(_fromUtf8("lbTotal"))
        self.gridLayout.addWidget(self.lbTotal, 6, 0, 1, 1)
        self.pushGo = QtGui.QPushButton(self.groupPreview)
        self.pushGo.setObjectName(_fromUtf8("pushGo"))
        self.gridLayout.addWidget(self.pushGo, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupPreview)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionChoose_Root_Directory = QtGui.QAction(MainWindow)
        self.actionChoose_Root_Directory.setObjectName(_fromUtf8("actionChoose_Root_Directory"))
        self.menubar.addAction(self.menuFile.menuAction())
        self.label.setBuddy(self.lineName)
        self.label_2.setBuddy(self.timestamp)
        self.label_3.setBuddy(self.treeView)
        self.lbCurPath.setBuddy(self.treeView)
        self.lbBiomass.setBuddy(self.tableBiomass)
        self.lbImages.setBuddy(self.tableImages)
        self.lbGeometry.setBuddy(self.tableGeom)
        self.lbText.setBuddy(self.tableReports)
        self.lbTotal.setBuddy(self.treeView)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.checkBiomass, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.tableBiomass.setVisible)
        QtCore.QObject.connect(self.checkGeom, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.tableGeom.setVisible)
        QtCore.QObject.connect(self.checkImages, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.tableImages.setVisible)
        QtCore.QObject.connect(self.checkReports, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.tableReports.setVisible)
        QtCore.QObject.connect(self.tableReports, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), MainWindow.tryOpenFile)
        QtCore.QObject.connect(self.tableBiomass, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), MainWindow.tryOpenFile)
        QtCore.QObject.connect(self.tableGeom, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), MainWindow.tryOpenFile)
        QtCore.QObject.connect(self.tableImages, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), MainWindow.tryOpenFile)
        QtCore.QObject.connect(self.pushGo, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.go)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Group Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Operator", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Timestamp", None, QtGui.QApplication.UnicodeUTF8))
        self.groupPreview.setTitle(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.checkReports.setText(QtGui.QApplication.translate("MainWindow", "Reports(*.doc,*.txt)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Survey List", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBiomass.setText(QtGui.QApplication.translate("MainWindow", "Biomass Calculation (*.xls)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkGeom.setText(QtGui.QApplication.translate("MainWindow", "Geometry (*.bna,*.mrg)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkImages.setText(QtGui.QApplication.translate("MainWindow", "Images (*.png, *.jpg)", None, QtGui.QApplication.UnicodeUTF8))
        self.lbCurPath.setText(QtGui.QApplication.translate("MainWindow", "CURRENT PATH", None, QtGui.QApplication.UnicodeUTF8))
        self.lbBiomass.setText(QtGui.QApplication.translate("MainWindow", "BIOMASS FILES", None, QtGui.QApplication.UnicodeUTF8))
        self.lbImages.setText(QtGui.QApplication.translate("MainWindow", "IMAGE FILES", None, QtGui.QApplication.UnicodeUTF8))
        self.lbGeometry.setText(QtGui.QApplication.translate("MainWindow", "GEOM FILES", None, QtGui.QApplication.UnicodeUTF8))
        self.lbText.setText(QtGui.QApplication.translate("MainWindow", "TEXT FILES", None, QtGui.QApplication.UnicodeUTF8))
        self.lbTotal.setText(QtGui.QApplication.translate("MainWindow", "TOTAL", None, QtGui.QApplication.UnicodeUTF8))
        self.pushGo.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChoose_Root_Directory.setText(QtGui.QApplication.translate("MainWindow", "Choose Root Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChoose_Root_Directory.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))

