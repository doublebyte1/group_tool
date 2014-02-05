import sys, os.path
import tempfile

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainfrm import Ui_MainWindow

strRoot='/home/joana/projects/no/test2/'

class groupDialog(QMainWindow):

    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
                        
        self.initTree()
        
        
    def initTree(self):        
                
        self.model=QFileSystemModel()
        self.model1=QFileSystemModel()
        self.model2=QFileSystemModel()
        self.model3=QFileSystemModel()
                        
        #Setting model for the treeview (dirs only!)                        
        self.ui.treeView.setModel(self.model)        
        self.model.setFilter(QDir.Dirs | QDir.NoDotAndDotDot)
        self.model.setRootPath(strRoot)
        self.ui.treeView.setRootIndex(self.model.index(self.model.rootPath()))
        
        #Initializing the lists
        self.ui.listBiomass.setModel(self.model1)
        self.model1.setFilter(QDir.Files | QDir.NoDotAndDotDot)   

        filters1 = []
        filters1.append("*.xls")
        
        self.model1.setNameFilters(filters1);
                                                 
        self.ui.listGeom.setModel(self.model2)
        self.model2.setFilter(QDir.Files | QDir.NoDotAndDotDot)   

        filters2 = []
        filters2.append("*.bna")
        filters2.append("*.mrg")
        
        self.model2.setNameFilters(filters2);

        self.ui.listImages.setModel(self.model3)
        self.model3.setFilter(QDir.Files | QDir.NoDotAndDotDot)   

        filters3 = []
        filters3.append("*.jpg")
        filters3.append("*.png")
        filters3.append("*.bmp")
        
        self.model3.setNameFilters(filters3);

    def adjustPreview(self,idx):
                
            path=self.model.filePath(idx)
            self.model1.setRootPath(path)
            self.model2.setRootPath(path)
            self.model3.setRootPath(path)
                                                
            self.ui.listBiomass.setRootIndex(self.model1.index(self.model1.rootPath()))
            self.ui.listGeom.setRootIndex(self.model2.index(self.model2.rootPath()))
            self.ui.listImages.setRootIndex(self.model3.index(self.model3.rootPath()))
            
                        
            #QMessageBox.Information(self, unicode("Group tool"),
             #     fileName,
              #    QMessageBox.Ok
               #   );