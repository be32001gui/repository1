# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\BE32001\pythonProject\alarm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import os.path

#不知道为什么反正加了这几行图片才能显示
CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
red = os.path.join(CURRENT_DIRECTORY, "image/red.jpg")
grey = os.path.join(CURRENT_DIRECTORY, "image/grey.jpg")


class Ui_Cellexus_CellMaker(object):
    def setupUi(self, Cellexus_CellMaker):
        Cellexus_CellMaker.setObjectName("Cellexus_CellMaker")
        Cellexus_CellMaker.resize(1124, 650)
        self.centralwidget = QtWidgets.QWidget(Cellexus_CellMaker)
        self.centralwidget.setObjectName("centralwidget")
        #tab
        self.tab1 = QtWidgets.QTabWidget(self.centralwidget)
        self.tab1.setGeometry(QtCore.QRect(10, 10, 1100, 610))
        self.tab1.setObjectName("tab1")
        #tab main
        self.Main = QtWidgets.QWidget()
        self.Main.setObjectName("Main")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 893, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        #alarm button
        self.O2flow_alarm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.O2flow_alarm.setObjectName("O2flow_alarm")
        self.gridLayout_3.addWidget(self.O2flow_alarm, 1, 2, 1, 1)
        
        self.Temp_alarm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Temp_alarm.setMouseTracking(False)
        self.Temp_alarm.setObjectName("Temp_alarm")
        self.gridLayout_3.addWidget(self.Temp_alarm, 1, 0, 1, 1)
        
        self.Airflow_alarm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Airflow_alarm.setObjectName("Airflow_alarm")
        self.gridLayout_3.addWidget(self.Airflow_alarm, 1, 3, 1, 1)
        
        self.Press_alarm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Press_alarm.setObjectName("Press_alarm")
        self.gridLayout_3.addWidget(self.Press_alarm, 1, 1, 1, 1)
        
        self.pO2_alarm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pO2_alarm.setObjectName("pO2_alarm")
        self.gridLayout_3.addWidget(self.pO2_alarm, 1, 5, 1, 1)
        
        self.pH_alarm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pH_alarm.setObjectName("pH_alarm")
        self.gridLayout_3.addWidget(self.pH_alarm, 1, 4, 1, 1)
        
        #alarm led
        self.Temp_led = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Temp_led.setObjectName("Temp_led")
        #self.Temp_led.setGeometry(QtCore.QRect(0, 0, 10, 10))
        self.gridLayout_3.addWidget(self.Temp_led, 0, 0, 1, 1)
        
        
        self.Press_led = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Press_led.setObjectName("Press_led")
        self.gridLayout_3.addWidget(self.Press_led, 0, 1, 1, 1)
        
        self.O2flow_led = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.O2flow_led.setObjectName("O2flow_led")
        self.gridLayout_3.addWidget(self.O2flow_led, 0, 2, 1, 1)
        
        self.Airflow_led = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Airflow_led.setObjectName("Airflow_led")
        self.gridLayout_3.addWidget(self.Airflow_led, 0, 3, 1, 1)
        
        self.pH_led = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pH_led.setObjectName("pH_led")
        self.gridLayout_3.addWidget(self.pH_led, 0, 4, 1, 1)
        
        self.pO2_led = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pO2_led.setObjectName("pO2_led")
        self.gridLayout_3.addWidget(self.pO2_led, 0, 5, 1, 1)
        
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        #Mode and Run button
        self.Mode = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Mode.setObjectName("Mode")
        self.verticalLayout.addWidget(self.Mode, 0, QtCore.Qt.AlignHCenter)# make “mode” on the center
        self.mode_choice = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.mode_choice.setObjectName("mode_choice")
        self.verticalLayout.addWidget(self.mode_choice)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.Run = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Run.setObjectName("Run")
        self.horizontalLayout_2.addWidget(self.Run)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.mode_choice.setGeometry(QtCore.QRect(390, 280, 121, 31))
        self.mode_choice.setMinimumSize(QtCore.QSize(121, 31))
        self.mode_choice.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mode_choice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mode_choice.setAutoFillBackground(True)
        self.mode_choice.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.mode_choice.addItem("")
        self.mode_choice.addItem("")
        self.mode_choice.addItem("")
        self.mode_choice.addItem("")
        
        #bio picture
        self.Bioreactor_pic = QtWidgets.QLabel(self.Main)
        self.Bioreactor_pic.setGeometry(QtCore.QRect(310, 120, 900, 450))
        self.Bioreactor_pic.setObjectName("Bioreactor_pic")
        
        self.tab1.addTab(self.Main, "")
        self.Charts = QtWidgets.QWidget()
        self.Charts.setObjectName("Charts")
        self.tab1.addTab(self.Charts, "")
        self.Manual_Log = QtWidgets.QWidget()
        self.Manual_Log.setObjectName("Manual_Log")
        self.tab1.addTab(self.Manual_Log, "")
        self.Auto_Log = QtWidgets.QWidget()
        self.Auto_Log.setObjectName("Auto_Log")
        self.tab1.addTab(self.Auto_Log, "")
        self.Events = QtWidgets.QWidget()
        self.Events.setObjectName("Events")
        self.tab1.addTab(self.Events, "")
        self.Comments = QtWidgets.QWidget()
        self.Comments.setObjectName("Comments")
        self.tab1.addTab(self.Comments, "")
        self.Recipe = QtWidgets.QWidget()
        self.Recipe.setObjectName("Recipe")
        self.tab1.addTab(self.Recipe, "")
        Cellexus_CellMaker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Cellexus_CellMaker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuControl = QtWidgets.QMenu(self.menubar)
        self.menuControl.setObjectName("menuControl")
        self.menuAlarms = QtWidgets.QMenu(self.menubar)
        self.menuAlarms.setObjectName("menuAlarms")
        self.menuSecurity = QtWidgets.QMenu(self.menubar)
        self.menuSecurity.setObjectName("menuSecurity")
        self.menuEngineering = QtWidgets.QMenu(self.menubar)
        self.menuEngineering.setObjectName("menuEngineering")
        Cellexus_CellMaker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Cellexus_CellMaker)
        self.statusbar.setObjectName("statusbar")
        Cellexus_CellMaker.setStatusBar(self.statusbar)
        self.actionsecurity = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionsecurity.setObjectName("actionsecurity")
        self.actionPressure = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionPressure.setObjectName("actionPressure")
        self.actionpH = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionpH.setObjectName("actionpH")
        self.actionpO2 = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionpO2.setObjectName("actionpO2")
        self.actionO2 = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionO2.setObjectName("actionO2")
        self.actionO2_Flow = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionO2_Flow.setObjectName("actionO2_Flow")
        self.actionAir_FLOW = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionAir_FLOW.setObjectName("actionAir_FLOW")
        self.menuAlarms.addAction(self.actionsecurity)
        self.menuAlarms.addAction(self.actionPressure)
        self.menuAlarms.addAction(self.actionpH)
        self.menuAlarms.addAction(self.actionpO2)
        self.menuAlarms.addAction(self.actionO2)
        self.menuAlarms.addAction(self.actionO2_Flow)
        self.menuAlarms.addAction(self.actionAir_FLOW)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuControl.menuAction())
        self.menubar.addAction(self.menuAlarms.menuAction())
        self.menubar.addAction(self.menuSecurity.menuAction())
        self.menubar.addAction(self.menuEngineering.menuAction())

        self.retranslateUi(Cellexus_CellMaker)
        self.tab1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Cellexus_CellMaker)

    def retranslateUi(self, Cellexus_CellMaker):
        _translate = QtCore.QCoreApplication.translate
        Cellexus_CellMaker.setWindowTitle(_translate("Cellexus_CellMaker", "Cellexus CellMaker"))
        self.O2flow_alarm.setText(_translate("Cellexus_CellMaker", "O2 Flow"))
        self.Temp_alarm.setText(_translate("Cellexus_CellMaker", "Temperature"))
        self.Airflow_alarm.setText(_translate("Cellexus_CellMaker", "Air Flow"))
        self.Press_alarm.setText(_translate("Cellexus_CellMaker", "Pressure"))
        self.pO2_alarm.setText(_translate("Cellexus_CellMaker", "pO2"))
        self.pH_alarm.setText(_translate("Cellexus_CellMaker", "pH"))
        self.Temp_led.setText(_translate("Cellexus_CellMaker", "Temp_led"))
        self.Press_led.setText(_translate("Cellexus_CellMaker", "Press_led"))
        self.O2flow_led.setText(_translate("Cellexus_CellMaker", "O2flow_led"))
        self.Airflow_led.setText(_translate("Cellexus_CellMaker", "Airflow_led"))
        self.pH_led.setText(_translate("Cellexus_CellMaker", "pH_led"))
        self.pO2_led.setText(_translate("Cellexus_CellMaker", "pO2_led"))
        
        #mode part
        self.Mode.setText(_translate("Cellexus_CellMaker", "Mode"))
        self.mode_choice.setItemText(0, _translate("Cellexus_CellMaker", "Setpoint"))
        self.mode_choice.setItemText(1, _translate("Cellexus_CellMaker", "Recipe 1"))
        self.mode_choice.setItemText(2, _translate("Cellexus_CellMaker", "Recipe 2"))
        self.mode_choice.setItemText(3, _translate("Cellexus_CellMaker", "Recipe 3"))
        
        self.Run.setText(_translate("Cellexus_CellMaker", "Run"))
        self.Bioreactor_pic.setText(_translate("Cellexus_CellMaker", "TextLabel"))
        
        #tab part
        self.tab1.setTabText(self.tab1.indexOf(self.Main), _translate("Cellexus_CellMaker", "Main"))
        self.tab1.setTabText(self.tab1.indexOf(self.Charts), _translate("Cellexus_CellMaker", "Charts"))
        self.tab1.setTabText(self.tab1.indexOf(self.Manual_Log), _translate("Cellexus_CellMaker", "Manual Log"))
        self.tab1.setTabText(self.tab1.indexOf(self.Auto_Log), _translate("Cellexus_CellMaker", "Auto Log"))
        self.tab1.setTabText(self.tab1.indexOf(self.Events), _translate("Cellexus_CellMaker", "Events"))
        self.tab1.setTabText(self.tab1.indexOf(self.Comments), _translate("Cellexus_CellMaker", "Comments"))
        self.tab1.setTabText(self.tab1.indexOf(self.Recipe), _translate("Cellexus_CellMaker", "Recipe"))
        self.menuFile.setTitle(_translate("Cellexus_CellMaker", "File"))
        self.menuControl.setTitle(_translate("Cellexus_CellMaker", "Control"))
        self.menuAlarms.setTitle(_translate("Cellexus_CellMaker", "Alarms"))
        self.menuSecurity.setTitle(_translate("Cellexus_CellMaker", "Security"))
        self.menuEngineering.setTitle(_translate("Cellexus_CellMaker", "Engineering"))
        self.actionsecurity.setText(_translate("Cellexus_CellMaker", "Temperature"))
        self.actionPressure.setText(_translate("Cellexus_CellMaker", "Pressure"))
        self.actionpH.setText(_translate("Cellexus_CellMaker", "pH"))
        self.actionpO2.setText(_translate("Cellexus_CellMaker", "pO2"))
        self.actionO2.setText(_translate("Cellexus_CellMaker", "O2"))
        self.actionO2_Flow.setText(_translate("Cellexus_CellMaker", "O2 Flow"))
        self.actionAir_FLOW.setText(_translate("Cellexus_CellMaker", "Air FLOW"))
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow() #widget->maindow
    ui = Ui_Cellexus_CellMaker() # CLASS NAME
    ui.setupUi(widget)
    widget.show()
    
    #bioreactor picture
    ui.Bioreactor_pic.setPixmap(QPixmap('image/bio.png'))
    ui.Bioreactor_pic.setScaledContents(True)
    #Setpoint=[Temp_setpoint, Press_setpoint, O2flow_setpoint, Airflow_setpoint, pH_setpoint, pO2_setpoint,]
    
    #alarm function
    #it may too complex and edious, also need to improve and maybe put this function to another py document
    #the led picture seems odd, also need some adjustment
    def ALARM(Temp_setpoint, Temp_measurement, Press_setpoint, Press_measurement, O2flow_setpoint, O2flow_measurement, Airflow_setpoint, Airflow_measurement, pH_setpoint, pH_measurement, pO2_setpoint, pO2_measurement):
        #clear the text
        #ui.Temp_led.setText("")
        red=QPixmap('image/red.jpg')
        grey=QPixmap('image/grey.jpg')
        #decide if it needs a alarm on
        if Temp_measurement > Temp_setpoint :
            ui.Temp_led.setPixmap(red)
            ui.Temp_led.setScaledContents(True)
        else :
            ui.Temp_led.setPixmap(grey)
            ui.Temp_led.setScaledContents(True)
        if Press_measurement > Press_setpoint :
            ui.Press_led.setPixmap(red)
            ui.Press_led.setScaledContents(True)
        else :
            ui.Press_led.setPixmap(grey)
            ui.Press_led.setScaledContents(True)
        if O2flow_measurement > O2flow_setpoint :
            ui.O2flow_led.setPixmap(red)
            ui.O2flow_led.setScaledContents(True)
        else :
            ui.O2flow_led.setPixmap(grey)
            ui.O2flow_led.setScaledContents(True)
        if Airflow_measurement > Airflow_setpoint :
            ui.Airflow_led.setPixmap(red)
            ui.Airflow_led.setScaledContents(True)
        else :
            ui.Airflow_led.setPixmap(grey)
            ui.Airflow_led.setScaledContents(True)
        if pH_measurement > pH_setpoint :
            ui.pH_led.setPixmap(red)
            ui.pH_led.setScaledContents(True)
        else :
            ui.pH_led.setPixmap(grey)
            ui.pH_led.setScaledContents(True)
        if pO2_measurement > pO2_setpoint :
            ui.pO2_led.setPixmap(red)
            ui.pO2_led.setScaledContents(True)
        else :
            ui.pO2_led.setPixmap(grey)
            ui.pO2_led.setScaledContents(True)
        
            
    ALARM(38,39,1,0,1,0,1,0,1,0,1,0)
    
    sys.exit(app.exec_())