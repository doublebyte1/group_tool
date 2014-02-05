'''
Created on Feb 4, 2014

@author: joana
'''
    
from PyQt4 import QtGui
from mainfrm import Ui_MainWindow
from group_dialog import groupDialog
 

if __name__ == '__main__':
    import sys
 
    app = QtGui.QApplication(sys.argv)
 
    aWidget = groupDialog()
    aWidget.show()
 
    sys.exit(app.exec_())