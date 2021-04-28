# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 15:59:24 2021

@author: ellie
"""
    
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog 
import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt 
from pyqtgraph import PlotWidget

class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 611, 381))
        self.widget.setObjectName("widget")
        self.widget.setBackground('w')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 430, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browsefiles)                  #click function
        self.buttonclear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonclear.setGeometry(QtCore.QRect(500, 450, 112, 34))
        self.buttonclear.setObjectName("clearbutton")
        self.buttonclear.clicked.connect(self.cleargraph)                  #click function
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(10, 430, 621, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(640, 40, 20, 381))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(689, 19, 181, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxTemp = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxTemp.setEnabled(True)
        self.checkBoxTemp.setObjectName("checkBoxTemp")
        self.checkBoxTemp.stateChanged.connect(self.checked_item)
        self.verticalLayout.addWidget(self.checkBoxTemp)
        self.checkBoxPres = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxPres.setObjectName("checkBoxPres")
        self.checkBoxPres.stateChanged.connect(self.checked_item)
        self.verticalLayout.addWidget(self.checkBoxPres)
        self.checkBoxPH = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxPH.setObjectName("checkBoxPH")
        self.checkBoxPH.stateChanged.connect(self.checked_item)
        self.verticalLayout.addWidget(self.checkBoxPH)
        self.checkBoxDO2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxDO2.setObjectName("checkBoxDO2")
        self.checkBoxDO2.stateChanged.connect(self.checked_item)
        self.verticalLayout.addWidget(self.checkBoxDO2)
        self.checkBoxAIR = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxAIR.setObjectName("checkBoxAIR")
        self.checkBoxAIR.stateChanged.connect(self.checked_item)
        self.verticalLayout.addWidget(self.checkBoxAIR)
        self.checkBoxO2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxO2.setObjectName("checkBoxO2")
        self.checkBoxO2.stateChanged.connect(self.checked_item)
        self.verticalLayout.addWidget(self.checkBoxO2)
        self.checkBoxCO2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxCO2.setObjectName("checkBoxCO2")
        self.checkBoxCO2.stateChanged.connect(self.checked_item)
        self.verticalLayout.addWidget(self.checkBoxCO2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 31))
        self.menubar.setObjectName("menubar")
        self.menuCharts = QtWidgets.QMenu(self.menubar)
        self.menuCharts.setObjectName("menuCharts")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCharts.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Export"))
        self.buttonclear.setText(_translate("MainWindow", "Clear"))
        self.checkBoxTemp.setText(_translate("MainWindow", "Temperature - Red"))
        self.checkBoxPres.setText(_translate("MainWindow", "Pressure - Orange"))
        self.checkBoxPH.setText(_translate("MainWindow", "pH - Yellow"))
        self.checkBoxDO2.setText(_translate("MainWindow", "dO2 - Green"))
        self.checkBoxAIR.setText(_translate("MainWindow", "Airflow - Blue"))
        self.checkBoxO2.setText(_translate("MainWindow", "O2 Flow - Purple"))
        self.checkBoxCO2.setText(_translate("MainWindow", "CO2 Flow - Pink"))
        self.menuCharts.setTitle(_translate("MainWindow", "Charts"))
        
    def browsefiles(self):
        fname = QFileDialog.getSaveFileName(self, 'Open File', 'D:\Documents')  
        
    def cleargraph(self):
        
        if self.checkBoxTemp.isChecked():
            self.checkBoxTemp.setCheckState(0)
            self.widget.clear()
            
        if self.checkBoxPres.isChecked():
            self.checkBoxPres.setCheckState(0)
            self.widget.clear()
            
        if self.checkBoxPH.isChecked():
            self.checkBoxPH.setCheckState(0)
            self.widget.clear()
            
        if self.checkBoxDO2.isChecked():
            self.checkBoxDO2.setCheckState(0) 
            self.widget.clear()
            
        if self.checkBoxAIR.isChecked():
            self.checkBoxAIR.setCheckState(0)
            self.widget.clear()
            
        if self.checkBoxO2.isChecked():
            self.checkBoxO2.setCheckState(0)  
            self.widget.clear()
            
        if self.checkBoxCO2.isChecked():
            self.checkBoxCO2.setCheckState(0)
            self.widget.clear()
            
    def checked_item(self):
        if self.checkBoxTemp.isChecked():
            x=[1,2,3]
            y=[2,3,4]
            pen = pg.mkPen(color=(255, 0, 0), width=3)
            self.widget.plot(x, y, pen=pen)
            
        if self.checkBoxPres.isChecked():
            x=[2,3,4]
            y=[2,3,4]
            pen = pg.mkPen(color=(255, 155, 55), width=3)
            self.widget.plot(x, y, pen=pen)
            
        if self.checkBoxPH.isChecked():
            x=[3,4,5]
            y=[2,3,4]
            pen = pg.mkPen(color=(255, 255, 0), width=3)
            self.widget.plot(x, y, pen=pen) 
            
        if self.checkBoxDO2.isChecked():
            x=[4,5,6]
            y=[2,3,4]
            pen = pg.mkPen(color=(100, 200, 50), width=3)
            self.widget.plot(x, y, pen=pen)    
         
        if self.checkBoxAIR.isChecked():
            x=[5,6,7]
            y=[2,3,4]
            pen = pg.mkPen(color=(0, 0, 255), width=3)
            self.widget.plot(x, y, pen=pen) 
            
        if self.checkBoxO2.isChecked():
            x=[6,7,8]
            y=[2,3,4]
            pen = pg.mkPen(color=(200, 0, 255), width=3)
            self.widget.plot(x, y, pen=pen) 
            
        if self.checkBoxCO2.isChecked():
            x=[7,8,9]
            y=[2,3,4]
            pen = pg.mkPen(color=(248, 24, 148), width=3)
            self.widget.plot(x, y, pen=pen)
            
          
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
