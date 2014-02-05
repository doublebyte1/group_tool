# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainfrm.ui'
#
# Created: Tue Feb  4 12:53:07 2014
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
        MainWindow.resize(1121, 615)
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
        self.label_3 = QtGui.QLabel(self.groupPreview)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupPreview)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupPreview)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupPreview)
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.treeView = QtGui.QTreeView(self.groupPreview)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 1)
        self.listBiomass = QtGui.QListView(self.groupPreview)
        self.listBiomass.setObjectName(_fromUtf8("listBiomass"))
        self.gridLayout.addWidget(self.listBiomass, 1, 1, 1, 1)
        self.listGeom = QtGui.QListView(self.groupPreview)
        self.listGeom.setObjectName(_fromUtf8("listGeom"))
        self.gridLayout.addWidget(self.listGeom, 1, 2, 1, 1)
        self.listImages = QtGui.QListView(self.groupPreview)
        self.listImages.setObjectName(_fromUtf8("listImages"))
        self.gridLayout.addWidget(self.listImages, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupPreview)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.lineName)
        self.label_2.setBuddy(self.timestamp)
        self.label_3.setBuddy(self.treeView)
        self.label_4.setBuddy(self.listBiomass)
        self.label_5.setBuddy(self.listGeom)
        self.label_6.setBuddy(self.listImages)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.treeView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), MainWindow.adjustPreview)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Group Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Operator", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Timestamp", None, QtGui.QApplication.UnicodeUTF8))
        self.groupPreview.setTitle(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Survey List", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Biomass Calculation (*.xls)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Geometry (*.bna,*.mrg)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Images (*.png, *.jpg, etc)", None, QtGui.QApplication.UnicodeUTF8))

