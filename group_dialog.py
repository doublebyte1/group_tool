import sys, os
import tempfile

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainfrm import Ui_MainWindow

#strRoot=QDir.currentPath()
strRoot='/media/IOMEGA HDD/Angola_Surveys/2002/'

class groupDialog(QMainWindow):

    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
                        
        self.initTree()
               
    def chooseDir(self):
        strRoot = QFileDialog.getExistingDirectory(self, 'Open Root Dir')              
        self.ui.lbRootDir.setText('Root directory set to: '  + strRoot)   
        self.model.setRootPath(strRoot)
        self.ui.treeView.setRootIndex(self.model.index(self.model.rootPath()))
               
    def initTree(self):                        
        #Setting model for the treeview (dirs only!)
        self.model=QFileSystemModel()                                                        
        self.ui.treeView.setModel(self.model)        
        #self.model.setFilter(QDir.Dirs | QDir.NoDotAndDotDot)
        self.model.setFilter(QDir.Dirs | QDir.NoDotDot)
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
                        
            QApplication.restoreOverrideCursor()
        