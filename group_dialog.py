import sys, os
import tempfile

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainfrm import Ui_MainWindow

#strRoot=QDir.currentPath()
strRoot='/'

class groupDialog(QMainWindow):

    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
                        
        self.initTree()
        self.cleanLabels()

    def cleanLabels(self):
        self.ui.lbBiomass.clear()
        self.ui.lbGeometry.clear()
        self.ui.lbImages.clear()
        self.ui.lbText.clear()
        self.ui.lbCurPath.clear()
        self.ui.lbTotal.clear()
                                                                               
    def chooseDir(self):
        strRoot = QFileDialog.getExistingDirectory(self, 'Open Root Dir')              
        self.ui.lbRootDir.setText('Root directory set to: '  + strRoot)   
        self.model.setRootPath(strRoot)
        self.ui.treeView.setRootIndex(self.model.index(self.model.rootPath()))
        #idx=self.model.index(0,0)
        #self.adjustPreview(idx)
               
    def initTree(self):                        
        #Setting model for the treeview (dirs only!)
        self.model=QFileSystemModel()
        self.model.sort(0,Qt.AscendingOrder)                                                        
        self.ui.treeView.setModel(self.model)        
        #self.model.setFilter(QDir.Dirs | QDir.NoDotAndDotDot)
        #self.model.setFilter(QDir.Dirs | QDir.NoDotDot)
        self.model.setFilter(QDir.Dirs | QDir.NoDotDot | QDir.NoDotAndDotDot)
        self.model.setRootPath(strRoot)
        self.ui.treeView.setRootIndex(self.model.index(self.model.rootPath()))
                
        self.model1 = QStandardItemModel()
        self.model2 = QStandardItemModel()
        self.model3 = QStandardItemModel()
        self.model4 = QStandardItemModel()
                    
        self.ui.tableBiomass.setModel(self.model1)
        self.ui.tableGeom.setModel(self.model2)
        self.ui.tableImages.setModel(self.model3)
        self.ui.tableReports.setModel(self.model4)

    def tryOpenFile(self,idx):
        print 'comes here'
        #print self.model1.item(0,0).data()[0]
        #print self.model2.item(0,0).data()
        #print self.model3.item(0,0).data()        
        #print self.model4.item(0,0).data()
        
    def adjustCounters(self,path):
        self.ui.lbCurPath.setText('Current path: ' + path)
        self.ui.lbTotal.setText("Total files: " + QVariant(self.model1.rowCount()+self.model2.rowCount()+self.model3.rowCount()+self.model4.rowCount()).toString())
        self.ui.lbGeometry.setText(QVariant(self.model2.rowCount()).toString()+ " files")
        self.ui.lbImages.setText(QVariant(self.model3.rowCount()).toString()+ " files")
        self.ui.lbText.setText(QVariant(self.model4.rowCount()).toString()+ " files")
        
        #self.ui.lbTotal.clear()        
        
    def adjustPreview(self,idx):
            QApplication.setOverrideCursor(Qt.WaitCursor)
                            
            path=self.model.filePath(idx)
             
            self.model1.clear()   
            self.model2.clear()   
            self.model3.clear()   
            self.model4.clear()   
                                              
            for root, subFolders, files in os.walk(str(path)):                                                            
                for filename in files:
                    list=[]
                    filePath = os.path.join(root, filename)                                                                         
                    item = QStandardItem(filename)
                    list.append(item)
                    item = QStandardItem(filePath)
                    list.append(item)                                    
                    if filename[-3:].lower() == 'xls':                    
                        self.model1.appendRow(list)
                    elif filename[-3:].lower() == 'mrg' or filename[-3:].lower() == 'bna':                    
                        self.model2.appendRow(list)
                    elif filename[-3:].lower() == 'png' or filename[-3:].lower() == 'jpg':
                        self.model3.appendRow(list)                    
                    elif filename[-3:].lower() == 'doc' or filename[-3:].lower() == 'txt':
                        self.model4.appendRow(list)
                        
            self.adjustCounters(path)
                                    
            QApplication.restoreOverrideCursor()
        