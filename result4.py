# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\BE32001\pythonProject\alarm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import os.path
import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt 
import pyqtgraph as pg
from pyqtgraph import PlotWidget

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
red = os.path.join(CURRENT_DIRECTORY, "image/red.jpg")
grey = os.path.join(CURRENT_DIRECTORY, "image/grey.jpg")

class Ui_Cellexus_CellMaker(QDialog):#obiject->dialog
    def setupUi(self, Cellexus_CellMaker):
        Cellexus_CellMaker.setObjectName("Cellexus_CellMaker")
        Cellexus_CellMaker.resize(1600, 900)
        Cellexus_CellMaker.setMaximumSize(QtCore.QSize(1600, 900))
        font = QtGui.QFont()
        font.setFamily("Arial")
        Cellexus_CellMaker.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Cellexus_CellMaker)
        self.centralwidget.setObjectName("centralwidget")
        self.tab1 = QtWidgets.QTabWidget(self.centralwidget)
        self.tab1.setGeometry(QtCore.QRect(10, 10, 1575, 850))
        self.tab1.setMaximumSize(QtCore.QSize(1575, 850))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab1.setFont(font)
        #self.tab1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tab1.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab1.setObjectName("tab1")
        self.Main = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Main.setFont(font)
        self.Main.setObjectName("Main")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1031, 103))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.alarmbox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.alarmbox.setMinimumSize(QtCore.QSize(590, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.alarmbox.setFont(font)
        #self.alarmbox.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.alarmbox.setObjectName("alarmbox")
        self.layoutWidget = QtWidgets.QWidget(self.alarmbox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 577, 69))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Press_led = QtWidgets.QLabel(self.layoutWidget)
        self.Press_led.setMinimumSize(QtCore.QSize(0, 0))
        self.Press_led.setMaximumSize(QtCore.QSize(30, 30))
        self.Press_led.setObjectName("Press_led")
        self.gridLayout_3.addWidget(self.Press_led, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pO2_alarm = QtWidgets.QLabel(self.layoutWidget)
        self.pO2_alarm.setMinimumSize(QtCore.QSize(90, 0))
        self.pO2_alarm.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pO2_alarm.setFont(font)
        self.pO2_alarm.setAlignment(QtCore.Qt.AlignCenter)
        self.pO2_alarm.setObjectName("pO2_alarm")
        self.gridLayout_3.addWidget(self.pO2_alarm, 1, 5, 1, 1)
        self.Press_alarm = QtWidgets.QLabel(self.layoutWidget)
        self.Press_alarm.setMinimumSize(QtCore.QSize(90, 0))
        self.Press_alarm.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Press_alarm.setFont(font)
        self.Press_alarm.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Press_alarm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Press_alarm.setTextFormat(QtCore.Qt.AutoText)
        self.Press_alarm.setAlignment(QtCore.Qt.AlignCenter)
        self.Press_alarm.setObjectName("Press_alarm")
        self.gridLayout_3.addWidget(self.Press_alarm, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.Temp_led = QtWidgets.QLabel(self.layoutWidget)
        self.Temp_led.setMaximumSize(QtCore.QSize(30, 30))
        self.Temp_led.setObjectName("Temp_led")
        self.gridLayout_3.addWidget(self.Temp_led, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Airflow_led = QtWidgets.QLabel(self.layoutWidget)
        self.Airflow_led.setMaximumSize(QtCore.QSize(30, 30))
        self.Airflow_led.setObjectName("Airflow_led")
        self.gridLayout_3.addWidget(self.Airflow_led, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.pO2_led = QtWidgets.QLabel(self.layoutWidget)
        self.pO2_led.setMaximumSize(QtCore.QSize(30, 30))
        self.pO2_led.setObjectName("pO2_led")
        self.gridLayout_3.addWidget(self.pO2_led, 0, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.Temp_alarm = QtWidgets.QLabel(self.layoutWidget)
        self.Temp_alarm.setMinimumSize(QtCore.QSize(90, 0))
        self.Temp_alarm.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Temp_alarm.setFont(font)
        self.Temp_alarm.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_alarm.setObjectName("Temp_alarm")
        self.gridLayout_3.addWidget(self.Temp_alarm, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pH_led = QtWidgets.QLabel(self.layoutWidget)
        self.pH_led.setMaximumSize(QtCore.QSize(30, 30))
        self.pH_led.setObjectName("pH_led")
        self.gridLayout_3.addWidget(self.pH_led, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.O2flow_led = QtWidgets.QLabel(self.layoutWidget)
        self.O2flow_led.setMaximumSize(QtCore.QSize(30, 30))
        self.O2flow_led.setObjectName("O2flow_led")
        self.gridLayout_3.addWidget(self.O2flow_led, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.Airflow_alarm = QtWidgets.QLabel(self.layoutWidget)
        self.Airflow_alarm.setMinimumSize(QtCore.QSize(90, 0))
        self.Airflow_alarm.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Airflow_alarm.setFont(font)
        self.Airflow_alarm.setAlignment(QtCore.Qt.AlignCenter)
        self.Airflow_alarm.setObjectName("Airflow_alarm")
        self.gridLayout_3.addWidget(self.Airflow_alarm, 1, 4, 1, 1)
        self.O2flow_alarm = QtWidgets.QLabel(self.layoutWidget)
        self.O2flow_alarm.setMinimumSize(QtCore.QSize(90, 0))
        self.O2flow_alarm.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2flow_alarm.setFont(font)
        self.O2flow_alarm.setAlignment(QtCore.Qt.AlignCenter)
        self.O2flow_alarm.setObjectName("O2flow_alarm")
        self.gridLayout_3.addWidget(self.O2flow_alarm, 1, 2, 1, 1)
        self.pH_alarm = QtWidgets.QLabel(self.layoutWidget)
        self.pH_alarm.setMinimumSize(QtCore.QSize(90, 0))
        self.pH_alarm.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pH_alarm.setFont(font)
        self.pH_alarm.setAlignment(QtCore.Qt.AlignCenter)
        self.pH_alarm.setObjectName("pH_alarm")
        self.gridLayout_3.addWidget(self.pH_alarm, 1, 3, 1, 1)
        self.horizontalLayout.addWidget(self.alarmbox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.modeBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.modeBox.setMinimumSize(QtCore.QSize(320, 100))
        #self.modeBox.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.modeBox.setTitle("")
        self.modeBox.setObjectName("modeBox")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.modeBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 278, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Mode = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Mode.setMinimumSize(QtCore.QSize(120, 30))
        self.Mode.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Mode.setFont(font)
        self.Mode.setAlignment(QtCore.Qt.AlignCenter)
        self.Mode.setObjectName("Mode")
        self.verticalLayout.addWidget(self.Mode, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.mode_choice = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.mode_choice.setMinimumSize(QtCore.QSize(120, 30))
        self.mode_choice.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.mode_choice.setFont(font)
        self.mode_choice.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mode_choice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mode_choice.setAutoFillBackground(False)
        #self.mode_choice.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mode_choice.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.mode_choice.setObjectName("mode_choice")
        self.mode_choice.addItem("")
        self.mode_choice.addItem("")
        self.mode_choice.addItem("")
        self.mode_choice.addItem("")
        self.verticalLayout.addWidget(self.mode_choice, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.Run = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Run.setMinimumSize(QtCore.QSize(120, 35))
        self.Run.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        
        #run button
        self.Run.setFont(font)
        self.Run.setStyleSheet("background-color:rgba(255,255,255,133);border-color:rgba(0,0,0,255);color: rgba(0, 0, 0,255);border-style:solid;border-width:1px;border-radius:2px;")
        self.Run.setCheckable(True)
        self.Run.setAutoRepeat(True)
        self.Run.setAutoDefault(True)
        self.Run.setFlat(True)
        self.Run.setObjectName("Run")
        #button icon set
        self.Run.setIcon(QtGui.QIcon('image\button_off.png'))###set icon need\ set picture need/
        self.Run.setIconSize(QtCore.QSize(90,25))##
        
        self.horizontalLayout_3.addWidget(self.Run)
        self.horizontalLayout.addWidget(self.modeBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        
        #main picture
        self.Bioreactor_pic = QtWidgets.QLabel(self.Main)
        self.Bioreactor_pic.setGeometry(QtCore.QRect(200, 170, 950, 550))#50->250 adjust the position
        self.Bioreactor_pic.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Bioreactor_pic.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Bioreactor_pic.setObjectName("Bioreactor_pic")
        
        self.setpointBox = QtWidgets.QGroupBox(self.Main)
        self.setpointBox.setGeometry(QtCore.QRect(1360, 10, 181, 381))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.setpointBox.setFont(font)
        #self.setpointBox.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.setpointBox.setObjectName("setpointBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.setpointBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 160, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Temp_SP = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Temp_SP.setFont(font)
        self.Temp_SP.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_SP.setObjectName("Temp_SP")
        self.verticalLayout_2.addWidget(self.Temp_SP)
        self.Temp_SPvalue = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.Temp_SPvalue.setMinimumSize(QtCore.QSize(0, 30))
        self.Temp_SPvalue.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Temp_SPvalue.setFont(font)
        self.Temp_SPvalue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Temp_SPvalue.setStyleSheet("QDoubleSpinBox::up-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:left;   \n"
"  width: 22px;\n"
"  height: 20px;  \n"
"  }\n"
"QDoubleSpinBox::down-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:right;\n"
"  width: 22px;\n"
"  height: 20px;    \n"
" }\n"
"background-color: rgb(239, 239, 239);")
        self.Temp_SPvalue.setFrame(True)
        self.Temp_SPvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_SPvalue.setReadOnly(False)
        self.Temp_SPvalue.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.Temp_SPvalue.setAccelerated(False)
        self.Temp_SPvalue.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.Temp_SPvalue.setProperty("showGroupSeparator", False)
        self.Temp_SPvalue.setDecimals(0)
        self.Temp_SPvalue.setObjectName("Temp_SPvalue")
        self.verticalLayout_2.addWidget(self.Temp_SPvalue)
        spacerItem3 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.O2flow_SP = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2flow_SP.setFont(font)
        self.O2flow_SP.setAlignment(QtCore.Qt.AlignCenter)
        self.O2flow_SP.setObjectName("O2flow_SP")
        self.verticalLayout_2.addWidget(self.O2flow_SP)
        self.O2flow_SPvalue = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.O2flow_SPvalue.setMinimumSize(QtCore.QSize(0, 30))
        self.O2flow_SPvalue.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2flow_SPvalue.setFont(font)
        self.O2flow_SPvalue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.O2flow_SPvalue.setStyleSheet("QDoubleSpinBox::up-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:left;   \n"
"  width: 22px;\n"
"  height: 20px;  \n"
"  }\n"
"QDoubleSpinBox::down-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:right;\n"
"  width: 22px;\n"
"  height: 20px;    \n"
" }\n"
"background-color: rgb(239, 239, 239);")
        self.O2flow_SPvalue.setFrame(True)
        self.O2flow_SPvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.O2flow_SPvalue.setReadOnly(False)
        self.O2flow_SPvalue.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.O2flow_SPvalue.setAccelerated(False)
        self.O2flow_SPvalue.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.O2flow_SPvalue.setProperty("showGroupSeparator", False)
        self.O2flow_SPvalue.setDecimals(0)
        self.O2flow_SPvalue.setObjectName("O2flow_SPvalue")
        self.verticalLayout_2.addWidget(self.O2flow_SPvalue)
        self.O2flow_value = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.O2flow_value.setMinimumSize(QtCore.QSize(0, 30))
        self.O2flow_value.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2flow_value.setFont(font)
        self.O2flow_value.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;")
        self.O2flow_value.setAlignment(QtCore.Qt.AlignCenter)
        self.O2flow_value.setReadOnly(True)
        self.O2flow_value.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.O2flow_value.setDecimals(3)
        self.O2flow_value.setObjectName("O2flow_value")
        self.verticalLayout_2.addWidget(self.O2flow_value)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.Airflow_SP = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Airflow_SP.setFont(font)
        self.Airflow_SP.setAlignment(QtCore.Qt.AlignCenter)
        self.Airflow_SP.setObjectName("Airflow_SP")
        self.verticalLayout_2.addWidget(self.Airflow_SP)
        self.Airflow_SPvalue = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.Airflow_SPvalue.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Airflow_SPvalue.setFont(font)
        self.Airflow_SPvalue.setStyleSheet("QDoubleSpinBox::up-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:left;   \n"
"  width: 22px;\n"
"  height: 20px;  \n"
"  }\n"
"QDoubleSpinBox::down-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:right;\n"
"  width: 22px;\n"
"  height: 20px;    \n"
" }\n"
"background-color: rgb(239, 239, 239);")
        self.Airflow_SPvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.Airflow_SPvalue.setDecimals(0)
        self.Airflow_SPvalue.setObjectName("Airflow_SPvalue")
        self.verticalLayout_2.addWidget(self.Airflow_SPvalue)
        self.Airflow_value = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.Airflow_value.setMinimumSize(QtCore.QSize(0, 30))
        self.Airflow_value.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Airflow_value.setFont(font)
        self.Airflow_value.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;")
        self.Airflow_value.setAlignment(QtCore.Qt.AlignCenter)
        self.Airflow_value.setReadOnly(True)
        self.Airflow_value.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Airflow_value.setDecimals(3)
        self.Airflow_value.setObjectName("Airflow_value")
        self.verticalLayout_2.addWidget(self.Airflow_value)
        
        
#automatic pump tool box
        self.Automatic_Pump = QtWidgets.QToolBox(self.Main)
        self.Automatic_Pump.setGeometry(QtCore.QRect(10, 130, 331, 301))##
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Automatic_Pump.setFont(font)
        self.Automatic_Pump.setStyleSheet("")
        self.Automatic_Pump.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Automatic_Pump.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Automatic_Pump.setObjectName("Automatic_Pump")
        self.Automatic_pH = QtWidgets.QWidget()
        self.Automatic_pH.setGeometry(QtCore.QRect(0, 0, 310, 161))##
        self.Automatic_pH.setObjectName("Automatic_pH")
        self.AutopHFrame = QtWidgets.QFrame(self.Automatic_pH)
        self.AutopHFrame.setGeometry(QtCore.QRect(10, 0, 310, 161))##
        self.AutopHFrame.setStyleSheet("")
        self.AutopHFrame.setObjectName("AutopHFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.AutopHFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pHSP_value = QtWidgets.QDoubleSpinBox(self.AutopHFrame)
        self.pHSP_value.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pHSP_value.setFont(font)
        self.pHSP_value.setStyleSheet("QDoubleSpinBox::up-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:left;   \n"
"  width: 22px;\n"
"  height: 20px;  \n"
"  }\n"
"QDoubleSpinBox::down-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:right;\n"
"  width: 22px;\n"
"  height: 20px;    \n"
" }\n"
"")
        self.pHSP_value.setAlignment(QtCore.Qt.AlignCenter)
        self.pHSP_value.setDecimals(1)
        self.pHSP_value.setObjectName("pHSP_value")
        self.gridLayout_2.addWidget(self.pHSP_value, 2, 2, 1, 1)
        
        #acid button
        self.acid_button = QtWidgets.QPushButton(self.AutopHFrame)
        self.acid_button.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.acid_button.setFont(font)
        self.acid_button.setStyleSheet("background-color:rgba(255,255,255,133);border-color:rgba(0,0,0,255);color: rgba(0, 0, 0,255);border-style:solid;border-width:1px;border-radius:2px;")
        self.acid_button.setCheckable(True)
        self.acid_button.setAutoRepeat(True)
        self.acid_button.setAutoDefault(True)
        self.acid_button.setObjectName("acid_button")
        #button icon set
        self.acid_button.setIcon(QtGui.QIcon('image\button_off.png'))###set icon need\ set picture need/
        self.acid_button.setIconSize(QtCore.QSize(90,25))##
        self.gridLayout_2.addWidget(self.acid_button, 1, 0, 1, 1)
        
        #base button
        self.base_button = QtWidgets.QPushButton(self.AutopHFrame)
        self.base_button.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.base_button.setFont(font)
        self.base_button.setStyleSheet("background-color:rgba(255,255,255,133);border-color:rgba(0,0,0,255);color: rgba(0, 0, 0,255);border-style:solid;border-width:1px;border-radius:2px;")
        self.base_button.setCheckable(True)
        self.base_button.setAutoRepeat(True)
        self.base_button.setAutoDefault(True)
        self.base_button.setObjectName("base_button")
        #button icon set
        self.base_button.setIcon(QtGui.QIcon('image\button_off.png'))###set icon need\ set picture need/
        self.base_button.setIconSize(QtCore.QSize(90,25))##
        self.gridLayout_2.addWidget(self.base_button, 2, 0, 1, 1)
        
        
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 1, 1, 1)
        self.pHSP_label = QtWidgets.QLabel(self.AutopHFrame)
        self.pHSP_label.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pHSP_label.setFont(font)
        self.pHSP_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pHSP_label.setObjectName("pHSP_label")
        self.gridLayout_2.addWidget(self.pHSP_label, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
#autopH WINDOW
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 2, 1, 1)
        self.AutopHBox = QtWidgets.QGroupBox(self.AutopHFrame)
        self.AutopHBox.setMinimumSize(QtCore.QSize(240, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutopHBox.setFont(font)
        self.AutopHBox.setAlignment(QtCore.Qt.AlignCenter)
        self.AutopHBox.setObjectName("AutopHBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.AutopHBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 20, 121, 41))##
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.AutopH_switchlabel1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutopH_switchlabel1.setFont(font)
        self.AutopH_switchlabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AutopH_switchlabel1.setObjectName("AutopH_switchlabel1")
        self.horizontalLayout_2.addWidget(self.AutopH_switchlabel1)
        
        #AutopH switch
        self.AutopH_switch = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.AutopH_switch.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutopH_switch.setFont(font)
        self.AutopH_switch.setStyleSheet("QPushButton\n"
"{\n"
"border: none;    \n"
"}\n"
"")
        self.AutopH_switch.setCheckable(True)
        self.AutopH_switch.setAutoRepeat(True)
        self.AutopH_switch.setAutoDefault(True)
        self.AutopH_switch.setFlat(True)
        self.AutopH_switch.setObjectName("AutopH_switch")
        
        #button icon set
        self.AutopH_switch.setIcon(QtGui.QIcon('image\off.png'))###set icon need\ set picture need/
        self.AutopH_switch.setIconSize(QtCore.QSize(50,50))##
        
        self.horizontalLayout_2.addWidget(self.AutopH_switch)
        self.AutopH_switchlabel2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutopH_switchlabel2.setFont(font)
        self.AutopH_switchlabel2.setObjectName("AutopH_switchlabel2")
        self.horizontalLayout_2.addWidget(self.AutopH_switchlabel2)
        self.gridLayout.addWidget(self.AutopHBox, 0, 2, 1, 1)
        self.Automatic_Pump.addItem(self.Automatic_pH, "")
        
#auto DO window
        self.Automatic_DO = QtWidgets.QWidget()
        self.Automatic_DO.setGeometry(QtCore.QRect(0, 0, 310, 161))##
        self.Automatic_DO.setObjectName("Automatic_DO")
        self.AutoDOFrame = QtWidgets.QFrame(self.Automatic_DO)
        self.AutoDOFrame.setGeometry(QtCore.QRect(10, 0, 310, 161))##
        self.AutoDOFrame.setStyleSheet("")
        self.AutoDOFrame.setObjectName("AutoDOFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.AutoDOFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.AutoDOBox = QtWidgets.QGroupBox(self.AutoDOFrame)
        self.AutoDOBox.setMinimumSize(QtCore.QSize(240, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutoDOBox.setFont(font)
        self.AutoDOBox.setAlignment(QtCore.Qt.AlignCenter)
        self.AutoDOBox.setObjectName("AutoDOBox")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.AutoDOBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(80, 20, 121, 41))##
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.AutoDO_switchlabel1 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutoDO_switchlabel1.setFont(font)
        self.AutoDO_switchlabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AutoDO_switchlabel1.setObjectName("AutoDO_switchlabel1")
        self.horizontalLayout_4.addWidget(self.AutoDO_switchlabel1)
        self.AutoDO_switch = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.AutoDO_switch.setMinimumSize(QtCore.QSize(60, 30))
        self.AutoDO_switch.setStyleSheet("QPushButton\n"
"{\n"
"border: none;    \n"
"}\n"
"")
        self.AutoDO_switch.setCheckable(True)
        self.AutoDO_switch.setAutoRepeat(True)
        self.AutoDO_switch.setAutoDefault(True)
        self.AutoDO_switch.setFlat(True)
        self.AutoDO_switch.setObjectName("AutoDO_switch")
        
        #button icon set
        self.AutoDO_switch.setIcon(QtGui.QIcon('image\off.png'))###set icon need\ set picture need/
        self.AutoDO_switch.setIconSize(QtCore.QSize(50,50))##
        
        self.horizontalLayout_4.addWidget(self.AutoDO_switch)
        self.AutoDO_switchlabel2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutoDO_switchlabel2.setFont(font)
        self.AutoDO_switchlabel2.setObjectName("AutoDO_switchlabel2")
        self.horizontalLayout_4.addWidget(self.AutoDO_switchlabel2)
        self.layoutWidget1 = QtWidgets.QWidget(self.AutoDOBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 70, 249, 64))##
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem7, 1, 1, 1, 1)
        self.AutoDO_gaslabel = QtWidgets.QLabel(self.layoutWidget1)
        self.AutoDO_gaslabel.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutoDO_gaslabel.setFont(font)
        self.AutoDO_gaslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AutoDO_gaslabel.setObjectName("AutoDO_gaslabel")
        self.gridLayout_6.addWidget(self.AutoDO_gaslabel, 1, 2, 1, 1)
        self.AutoDO_O2label = QtWidgets.QLabel(self.layoutWidget1)
        self.AutoDO_O2label.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutoDO_O2label.setFont(font)
        self.AutoDO_O2label.setAlignment(QtCore.Qt.AlignCenter)
        self.AutoDO_O2label.setObjectName("AutoDO_O2label")
        self.gridLayout_6.addWidget(self.AutoDO_O2label, 1, 0, 1, 1)
        self.AutoDO_O2value = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.AutoDO_O2value.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutoDO_O2value.setFont(font)
        self.AutoDO_O2value.setStyleSheet("QDoubleSpinBox::up-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:left;   \n"
"  width: 22px;\n"
"  height: 20px;  \n"
"  }\n"
"QDoubleSpinBox::down-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:right;\n"
"  width: 22px;\n"
"  height: 20px;    \n"
" }\n"
"")
        self.AutoDO_O2value.setAlignment(QtCore.Qt.AlignCenter)
        self.AutoDO_O2value.setDecimals(0)
        self.AutoDO_O2value.setObjectName("AutoDO_O2value")
        self.gridLayout_6.addWidget(self.AutoDO_O2value, 2, 0, 1, 1)
        self.AutoDO_gasswitch = QtWidgets.QPushButton(self.layoutWidget1)
        self.AutoDO_gasswitch.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AutoDO_gasswitch.setFont(font)
        self.AutoDO_gasswitch.setStyleSheet("QPushButton\n"
"{\n"
"border: none;    \n"
"}\n"
"")
        self.AutoDO_gasswitch.setCheckable(True)
        self.AutoDO_gasswitch.setAutoRepeat(True)
        self.AutoDO_gasswitch.setAutoDefault(True)
        self.AutoDO_gasswitch.setFlat(True)
        self.AutoDO_gasswitch.setObjectName("AutoDO_gasswitch")
        
        #button icon set
        self.AutoDO_gasswitch.setIcon(QtGui.QIcon('image\off.png'))###set icon need\ set picture need/
        self.AutoDO_gasswitch.setIconSize(QtCore.QSize(50,50))##
        
        self.gridLayout_6.addWidget(self.AutoDO_gasswitch, 2, 2, 1, 1)
        self.gridLayout_5.addWidget(self.AutoDOBox, 0, 1, 1, 1)
        self.Automatic_Pump.addItem(self.Automatic_DO, "")
        
#feed pump window
        self.Feed_Pump = QtWidgets.QWidget()
        self.Feed_Pump.setGeometry(QtCore.QRect(0, 0, 310, 161))##
        self.Feed_Pump.setObjectName("Feed_Pump")
        self.AutoDOFrame_2 = QtWidgets.QFrame(self.Feed_Pump)
        self.AutoDOFrame_2.setGeometry(QtCore.QRect(10, 0, 310, 161))##
        self.AutoDOFrame_2.setStyleSheet("")
        self.AutoDOFrame_2.setObjectName("AutoDOFrame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.AutoDOFrame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.FeedPumpbox = QtWidgets.QGroupBox(self.AutoDOFrame_2)
        self.FeedPumpbox.setMinimumSize(QtCore.QSize(240, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.FeedPumpbox.setFont(font)
        self.FeedPumpbox.setAlignment(QtCore.Qt.AlignCenter)
        self.FeedPumpbox.setObjectName("FeedPumpbox")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.FeedPumpbox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(80, 20, 121, 41))##
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.FeedPump_switchlabel1 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.FeedPump_switchlabel1.setFont(font)
        self.FeedPump_switchlabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FeedPump_switchlabel1.setObjectName("FeedPump_switchlabel1")
        self.horizontalLayout_5.addWidget(self.FeedPump_switchlabel1)
        self.FeedPump_switch = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.FeedPump_switch.setMinimumSize(QtCore.QSize(60, 30))
        self.FeedPump_switch.setStyleSheet("QPushButton\n"
"{\n"
"border: none;    \n"
"}\n"
"")
        self.FeedPump_switch.setCheckable(True)
        self.FeedPump_switch.setAutoRepeat(True)
        self.FeedPump_switch.setAutoDefault(True)
        self.FeedPump_switch.setFlat(True)
        self.FeedPump_switch.setObjectName("FeedPump_switch")
        
        #button icon set
        self.FeedPump_switch.setIcon(QtGui.QIcon('image\off.png'))###set icon need\ set picture need/
        self.FeedPump_switch.setIconSize(QtCore.QSize(50,50))##
        
        self.horizontalLayout_5.addWidget(self.FeedPump_switch)
        self.FeedPump_switchlabel2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.FeedPump_switchlabel2.setFont(font)
        self.FeedPump_switchlabel2.setObjectName("FeedPump_switchlabel2")
        self.horizontalLayout_5.addWidget(self.FeedPump_switchlabel2)
        self.gridLayout_7.addWidget(self.FeedPumpbox, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.RPM_label = QtWidgets.QLabel(self.AutoDOFrame_2)
        self.RPM_label.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.RPM_label.setFont(font)
        self.RPM_label.setAlignment(QtCore.Qt.AlignCenter)
        self.RPM_label.setObjectName("RPM_label")
        self.verticalLayout_3.addWidget(self.RPM_label)
        self.gridLayout_7.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.RPM_value = QtWidgets.QDoubleSpinBox(self.AutoDOFrame_2)
        self.RPM_value.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.RPM_value.setFont(font)
        self.RPM_value.setStyleSheet("QDoubleSpinBox::up-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:left;   \n"
"  width: 22px;\n"
"  height: 20px;  \n"
"  }\n"
"QDoubleSpinBox::down-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:right;\n"
"  width: 22px;\n"
"  height: 20px;    \n"
" }\n"
"")
        self.RPM_value.setAlignment(QtCore.Qt.AlignCenter)
        self.RPM_value.setDecimals(0)
        self.RPM_value.setObjectName("RPM_value")
        self.gridLayout_7.addWidget(self.RPM_value, 2, 1, 1, 1)
        self.Automatic_Pump.addItem(self.Feed_Pump, "")
        
#acid base pump window
        self.Acid_Base_Pump = QtWidgets.QWidget()
        self.Acid_Base_Pump.setGeometry(QtCore.QRect(0, 0, 310, 161))##
        self.Acid_Base_Pump.setObjectName("Acid_Base_Pump")
        self.AutoDOFrame_3 = QtWidgets.QFrame(self.Acid_Base_Pump)
        self.AutoDOFrame_3.setGeometry(QtCore.QRect(10, 0, 310, 161))##
        self.AutoDOFrame_3.setStyleSheet("")
        self.AutoDOFrame_3.setObjectName("AutoDOFrame_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.AutoDOFrame_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.DosingBox = QtWidgets.QGroupBox(self.AutoDOFrame_3)
        self.DosingBox.setMinimumSize(QtCore.QSize(240, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.DosingBox.setFont(font)
        self.DosingBox.setAlignment(QtCore.Qt.AlignCenter)
        self.DosingBox.setObjectName("DosingBox")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.DosingBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(80, 20, 121, 41))##
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Dosing_switchlabel1 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Dosing_switchlabel1.setFont(font)
        self.Dosing_switchlabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Dosing_switchlabel1.setObjectName("Dosing_switchlabel1")
        self.horizontalLayout_6.addWidget(self.Dosing_switchlabel1)
        self.Dosing_switch = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.Dosing_switch.setMinimumSize(QtCore.QSize(60, 30))
        self.Dosing_switch.setStyleSheet("QPushButton\n"
"{\n"
"border: none;    \n"
"}\n"
"")
        self.Dosing_switch.setCheckable(True)
        self.Dosing_switch.setAutoRepeat(True)
        self.Dosing_switch.setAutoDefault(True)
        self.Dosing_switch.setFlat(True)
        self.Dosing_switch.setObjectName("Dosing_switch")
        
        #button icon set
        self.Dosing_switch.setIcon(QtGui.QIcon('image\off.png'))###set icon need\ set picture need/
        self.Dosing_switch.setIconSize(QtCore.QSize(50,50))##
        
        self.horizontalLayout_6.addWidget(self.Dosing_switch)
        self.Dosing_switchlabel2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Dosing_switchlabel2.setFont(font)
        self.Dosing_switchlabel2.setObjectName("Dosing_switchlabel2")
        self.horizontalLayout_6.addWidget(self.Dosing_switchlabel2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.DosingBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(5, 70, 275, 64))##
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.Base_timevalue = QtWidgets.QDoubleSpinBox(self.layoutWidget_3)
        self.Base_timevalue.setMinimumSize(QtCore.QSize(100, 25))##
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Base_timevalue.setFont(font)
        self.Base_timevalue.setStyleSheet("QDoubleSpinBox::up-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:left;   \n"
"  width: 22px;\n"
"  height: 20px;  \n"
"  }\n"
"QDoubleSpinBox::down-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:right;\n"
"  width: 22px;\n"
"  height: 20px;    \n"
" }\n"
"")
        self.Base_timevalue.setAlignment(QtCore.Qt.AlignCenter)
        self.Base_timevalue.setDecimals(0)
        self.Base_timevalue.setObjectName("Base_timevalue")
        self.gridLayout_10.addWidget(self.Base_timevalue, 2, 1, 1, 1)
        self.Acid_timelabel = QtWidgets.QLabel(self.layoutWidget_3)
        self.Acid_timelabel.setMinimumSize(QtCore.QSize(100, 25))##
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Acid_timelabel.setFont(font)
        self.Acid_timelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Acid_timelabel.setObjectName("Acid_timelabel")
        self.gridLayout_10.addWidget(self.Acid_timelabel, 1, 0, 1, 1)
        self.Base_timelabel = QtWidgets.QLabel(self.layoutWidget_3)
        self.Base_timelabel.setMinimumSize(QtCore.QSize(100, 25))##
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Base_timelabel.setFont(font)
        self.Base_timelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Base_timelabel.setObjectName("Base_timelabel")
        self.gridLayout_10.addWidget(self.Base_timelabel, 1, 1, 1, 1)
        self.Acid_timevalue = QtWidgets.QDoubleSpinBox(self.layoutWidget_3)
        self.Acid_timevalue.setMinimumSize(QtCore.QSize(100, 25))##
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Acid_timevalue.setFont(font)
        self.Acid_timevalue.setStyleSheet("QDoubleSpinBox::up-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:left;   \n"
"  width: 22px;\n"
"  height: 20px;  \n"
"  }\n"
"QDoubleSpinBox::down-button\n"
" {subcontrol-origin:border;\n"
"  subcontrol-position:right;\n"
"  width: 22px;\n"
"  height: 20px;    \n"
" }\n"
"")
        self.Acid_timevalue.setAlignment(QtCore.Qt.AlignCenter)
        self.Acid_timevalue.setDecimals(0)
        self.Acid_timevalue.setObjectName("Acid_timevalue")
        self.gridLayout_10.addWidget(self.Acid_timevalue, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.DosingBox, 0, 0, 1, 2)
        self.Automatic_Pump.addItem(self.Acid_Base_Pump, "")
        
#pic comment
        self.formLayoutWidget = QtWidgets.QWidget(self.Main)
        self.formLayoutWidget.setGeometry(QtCore.QRect(540, 250, 190, 291))##
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Bioreactor_pic_acid = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Bioreactor_pic_acid.setFont(font)
        self.Bioreactor_pic_acid.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Bioreactor_pic_acid.setAutoRepeat(True)
        self.Bioreactor_pic_acid.setAutoExclusive(False)
        self.Bioreactor_pic_acid.setObjectName("Bioreactor_pic_acid")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Bioreactor_pic_acid)
        self.acid_time = QtWidgets.QTimeEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.acid_time.setFont(font)
        self.acid_time.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;\n"
"")
        self.acid_time.setAlignment(QtCore.Qt.AlignCenter)
        self.acid_time.setReadOnly(True)
        self.acid_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.acid_time.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.acid_time.setCalendarPopup(False)
        self.acid_time.setObjectName("acid_time")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.acid_time)
        self.Bioreactor_pic_base = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Bioreactor_pic_base.setFont(font)
        self.Bioreactor_pic_base.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Bioreactor_pic_base.setAutoRepeat(True)
        self.Bioreactor_pic_base.setAutoExclusive(False)
        self.Bioreactor_pic_base.setObjectName("Bioreactor_pic_base")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Bioreactor_pic_base)
        spacerItem8 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem8)
        self.Bioreactor_pic_heating = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Bioreactor_pic_heating.setFont(font)
        self.Bioreactor_pic_heating.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Bioreactor_pic_heating.setAutoRepeat(True)
        self.Bioreactor_pic_heating.setAutoExclusive(False)
        self.Bioreactor_pic_heating.setObjectName("Bioreactor_pic_heating")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Bioreactor_pic_heating)
        self.Bioreactor_pic_cooling = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Bioreactor_pic_cooling.setFont(font)
        self.Bioreactor_pic_cooling.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Bioreactor_pic_cooling.setAutoRepeat(True)
        self.Bioreactor_pic_cooling.setAutoExclusive(False)
        self.Bioreactor_pic_cooling.setObjectName("Bioreactor_pic_cooling")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Bioreactor_pic_cooling)
        self.base_time = QtWidgets.QTimeEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.base_time.setFont(font)
        self.base_time.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;")
        self.base_time.setAlignment(QtCore.Qt.AlignCenter)
        self.base_time.setReadOnly(True)
        self.base_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.base_time.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.base_time.setCalendarPopup(False)
        self.base_time.setObjectName("base_time")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.base_time)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem10)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Main)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1150, 380, 131, 271))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.biopic_pHlabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.biopic_pHlabel.setFont(font)
        self.biopic_pHlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.biopic_pHlabel.setObjectName("biopic_pHlabel")
        self.verticalLayout_4.addWidget(self.biopic_pHlabel)
        self.biopic_pHvalue = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.biopic_pHvalue.setFont(font)
        self.biopic_pHvalue.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;")
        self.biopic_pHvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.biopic_pHvalue.setReadOnly(True)
        self.biopic_pHvalue.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.biopic_pHvalue.setDecimals(3)
        self.biopic_pHvalue.setObjectName("biopic_pHvalue")
        self.verticalLayout_4.addWidget(self.biopic_pHvalue)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.biopic_pO2label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.biopic_pO2label.setFont(font)
        self.biopic_pO2label.setAlignment(QtCore.Qt.AlignCenter)
        self.biopic_pO2label.setObjectName("biopic_pO2label")
        self.verticalLayout_4.addWidget(self.biopic_pO2label)
        self.biopic_pO2value = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.biopic_pO2value.setFont(font)
        self.biopic_pO2value.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;")
        self.biopic_pO2value.setAlignment(QtCore.Qt.AlignCenter)
        self.biopic_pO2value.setReadOnly(True)
        self.biopic_pO2value.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.biopic_pO2value.setDecimals(3)
        self.biopic_pO2value.setObjectName("biopic_pO2value")
        self.verticalLayout_4.addWidget(self.biopic_pO2value)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.biopic_templabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.biopic_templabel.setFont(font)
        self.biopic_templabel.setAlignment(QtCore.Qt.AlignCenter)
        self.biopic_templabel.setObjectName("biopic_templabel")
        self.verticalLayout_4.addWidget(self.biopic_templabel)
        self.biopic_tempvalue = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.biopic_tempvalue.setFont(font)
        self.biopic_tempvalue.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;")
        self.biopic_tempvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.biopic_tempvalue.setReadOnly(True)
        self.biopic_tempvalue.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.biopic_tempvalue.setDecimals(3)
        self.biopic_tempvalue.setObjectName("biopic_tempvalue")
        self.verticalLayout_4.addWidget(self.biopic_tempvalue)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.biopic_pressurelabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.biopic_pressurelabel.setFont(font)
        self.biopic_pressurelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.biopic_pressurelabel.setObjectName("biopic_pressurelabel")
        self.verticalLayout_4.addWidget(self.biopic_pressurelabel)
        self.biopic_pressurevalue = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.biopic_pressurevalue.setFont(font)
        self.biopic_pressurevalue.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;")
        self.biopic_pressurevalue.setAlignment(QtCore.Qt.AlignCenter)
        self.biopic_pressurevalue.setReadOnly(True)
        self.biopic_pressurevalue.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.biopic_pressurevalue.setDecimals(3)
        self.biopic_pressurevalue.setObjectName("biopic_pressurevalue")
        self.verticalLayout_4.addWidget(self.biopic_pressurevalue)
        self.device_box = QtWidgets.QComboBox(self.Main)
        self.device_box.setGeometry(QtCore.QRect(1410, 740, 131, 41))
        self.device_box.setMaximumSize(QtCore.QSize(131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.device_box.setFont(font)
        self.device_box.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.device_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.device_box.setAutoFillBackground(True)
        self.device_box.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;\n"
"QComboBox::drop-down\n"
"{\n"
" border-style: none;\n"
"}")
        self.device_box.setEditable(False)
        self.device_box.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.device_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.device_box.setIconSize(QtCore.QSize(20, 20))
        self.device_box.setDuplicatesEnabled(False)
        self.device_box.setObjectName("device_box")
        self.device_box.addItem("")
        self.device_box.addItem("")
        self.device_box.addItem("")
        self.gridLayoutWidget = QtWidgets.QWidget(self.Main)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 460, 411, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.O2minmaxflow_value = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.O2minmaxflow_value.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2minmaxflow_value.setFont(font)
        self.O2minmaxflow_value.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;")
        self.O2minmaxflow_value.setAlignment(QtCore.Qt.AlignCenter)
        self.O2minmaxflow_value.setReadOnly(True)
        self.O2minmaxflow_value.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.O2minmaxflow_value.setDecimals(3)
        self.O2minmaxflow_value.setObjectName("O2minmaxflow_value")
        self.gridLayout_4.addWidget(self.O2minmaxflow_value, 1, 2, 1, 1)
        self.O2limit_button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.O2limit_button_2.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2limit_button_2.setFont(font)
        self.O2limit_button_2.setCheckable(True)
        self.O2limit_button_2.setAutoRepeat(True)
        self.O2limit_button_2.setAutoDefault(True)
        self.O2limit_button_2.setFlat(True)
        self.O2limit_button_2.setObjectName("O2limit_button_2")
        self.gridLayout_4.addWidget(self.O2limit_button_2, 3, 0, 1, 1)
        self.O2limit_button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.O2limit_button_4.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2limit_button_4.setFont(font)
        self.O2limit_button_4.setCheckable(True)
        self.O2limit_button_4.setAutoRepeat(True)
        self.O2limit_button_4.setAutoDefault(True)
        self.O2limit_button_4.setFlat(True)
        self.O2limit_button_4.setObjectName("O2limit_button_4")
        self.gridLayout_4.addWidget(self.O2limit_button_4, 5, 0, 1, 1)
        self.O2limit_button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.O2limit_button_3.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2limit_button_3.setFont(font)
        self.O2limit_button_3.setCheckable(True)
        self.O2limit_button_3.setAutoRepeat(True)
        self.O2limit_button_3.setAutoDefault(True)
        self.O2limit_button_3.setFlat(True)
        self.O2limit_button_3.setObjectName("O2limit_button_3")
        self.gridLayout_4.addWidget(self.O2limit_button_3, 6, 0, 1, 1)
        self.O2flow_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.O2flow_label.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2flow_label.setFont(font)
        self.O2flow_label.setAlignment(QtCore.Qt.AlignCenter)
        self.O2flow_label.setObjectName("O2flow_label")
        self.gridLayout_4.addWidget(self.O2flow_label, 0, 2, 1, 1)
        self.O2limit_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.O2limit_button.setMinimumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2limit_button.setFont(font)
        self.O2limit_button.setCheckable(True)
        self.O2limit_button.setAutoRepeat(True)
        self.O2limit_button.setAutoDefault(True)
        self.O2limit_button.setFlat(True)
        self.O2limit_button.setObjectName("O2limit_button")
        self.gridLayout_4.addWidget(self.O2limit_button, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 2, 1, 1)
        self.O2minmax_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.O2minmax_label.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.O2minmax_label.setFont(font)
        self.O2minmax_label.setAlignment(QtCore.Qt.AlignCenter)
        self.O2minmax_label.setObjectName("O2minmax_label")
        self.gridLayout_4.addWidget(self.O2minmax_label, 0, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem14, 6, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem15, 3, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem16, 1, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem17, 5, 1, 1, 1)
        self.Airminmaxflow_value = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.Airminmaxflow_value.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Airminmaxflow_value.setFont(font)
        self.Airminmaxflow_value.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border-color:rgba(111,111,170,255);\n"
"color: rgba(0, 0, 0,255);\n"
"border-style:double;\n"
"border-width:4px;\n"
"border-radius:8px;")
        self.Airminmaxflow_value.setAlignment(QtCore.Qt.AlignCenter)
        self.Airminmaxflow_value.setReadOnly(True)
        self.Airminmaxflow_value.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Airminmaxflow_value.setDecimals(3)
        self.Airminmaxflow_value.setObjectName("Airminmaxflow_value")
        self.gridLayout_4.addWidget(self.Airminmaxflow_value, 3, 2, 1, 1)
        self.cellexuspic = QtWidgets.QLabel(self.Main)
        self.cellexuspic.setGeometry(QtCore.QRect(10, 690, 511, 111))
        self.cellexuspic.setText("")
        self.cellexuspic.setObjectName("cellexuspic")
        self.Bioreactor_pic.raise_()
        self.horizontalLayoutWidget.raise_()
        self.setpointBox.raise_()
        self.Automatic_Pump.raise_()
        self.formLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.device_box.raise_()
        self.gridLayoutWidget.raise_()
        self.cellexuspic.raise_()
        self.tab1.addTab(self.Main, "")
        
        #charts tab
        self.Charts = QtWidgets.QWidget()
        self.Charts.setObjectName("Charts")
        self.tab1.addTab(self.Charts, "")
        #
        "Ellie's code here"
        #
        
        #manual log tab
        self.Manual_Log = QtWidgets.QWidget()
        self.Manual_Log.setObjectName("Manual_Log")        
        self.tab1.addTab(self.Manual_Log, "")
        #
        "Vicky's code here"
        #
        
        self.Auto_Log = QtWidgets.QWidget()
        self.Auto_Log.setObjectName("Auto_Log")        
        self.tab1.addTab(self.Auto_Log, "")
        
        self.Events = QtWidgets.QWidget()
        self.Events.setObjectName("Events")        
        self.tab1.addTab(self.Events, "")
        
        self.Comments = QtWidgets.QWidget()
        self.Comments.setObjectName("Comments")        
        self.tab1.addTab(self.Comments, "")
        
        #recipe tab
        self.Recipe = QtWidgets.QWidget()
        self.Recipe.setObjectName("Recipe")        
        self.tab1.addTab(self.Recipe, "")
        #
        "Qian's code here"
        #
        
        Cellexus_CellMaker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Cellexus_CellMaker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
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
        self.actionNew = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(Cellexus_CellMaker)
        self.actionExit.setCheckable(False)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
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

        #button change function connect
        self.retranslateUi(Cellexus_CellMaker)
        self.tab1.setCurrentIndex(0)
        self.Automatic_Pump.setCurrentIndex(0)
        #button
        self.Run.clicked[bool].connect(self.bticon)#form->self, link to the change function
        self.acid_button.clicked[bool].connect(self.bticon)#form->self, link to the change function
        self.base_button.clicked[bool].connect(self.bticon)#form->self, link to the change function
        #switch
        self.AutopH_switch.clicked[bool].connect(self.swicon)#form->self, link to the change function
        self.AutoDO_switch.clicked[bool].connect(self.swicon)#form->self, link to the change function
        self.AutoDO_gasswitch.clicked[bool].connect(self.swicon)#form->self, link to the change function
        self.FeedPump_switch.clicked[bool].connect(self.swicon)#form->self, link to the change function
        self.Dosing_switch.clicked[bool].connect(self.swicon)#form->self, link to the change function
        #self.acid_button.clicked.connect(Cellexus_CellMaker.switchit)
        #self.base_button.clicked.connect(Cellexus_CellMaker.switchit)
        QtCore.QMetaObject.connectSlotsByName(Cellexus_CellMaker)
        
        
        #signal and slot function here
        
        
        
        #

    def retranslateUi(self, Cellexus_CellMaker):
        _translate = QtCore.QCoreApplication.translate
        Cellexus_CellMaker.setWindowTitle(_translate("Cellexus_CellMaker", "Cellexus CellMaker"))
        self.alarmbox.setTitle(_translate("Cellexus_CellMaker", "Alarm"))
        self.Press_led.setText(_translate("Cellexus_CellMaker", "Press_led"))
        self.pO2_alarm.setText(_translate("Cellexus_CellMaker", "pO2"))
        self.Press_alarm.setText(_translate("Cellexus_CellMaker", "Pressure"))
        self.Temp_led.setText(_translate("Cellexus_CellMaker", "Temp_led"))
        self.Airflow_led.setText(_translate("Cellexus_CellMaker", "Airflow_led"))
        self.pO2_led.setText(_translate("Cellexus_CellMaker", "pO2_led"))
        self.Temp_alarm.setText(_translate("Cellexus_CellMaker", "Temperature"))
        self.pH_led.setText(_translate("Cellexus_CellMaker", "pH_led"))
        self.O2flow_led.setText(_translate("Cellexus_CellMaker", "O2flow_led"))
        self.Airflow_alarm.setText(_translate("Cellexus_CellMaker", "Air Flow"))
        self.O2flow_alarm.setText(_translate("Cellexus_CellMaker", "O2 Flow"))
        self.pH_alarm.setText(_translate("Cellexus_CellMaker", "pH"))
        self.Mode.setText(_translate("Cellexus_CellMaker", "Mode"))
        self.mode_choice.setItemText(0, _translate("Cellexus_CellMaker", "Setpoint"))
        self.mode_choice.setItemText(1, _translate("Cellexus_CellMaker", "Recipe 1"))
        self.mode_choice.setItemText(2, _translate("Cellexus_CellMaker", "Recipe 2"))
        self.mode_choice.setItemText(3, _translate("Cellexus_CellMaker", "Recipe 3"))
        self.Run.setText(_translate("Cellexus_CellMaker", "Run"))
        self.Bioreactor_pic.setText(_translate("Cellexus_CellMaker", "bio"))
        self.setpointBox.setTitle(_translate("Cellexus_CellMaker", "Setpoint"))
        self.Temp_SP.setText(_translate("Cellexus_CellMaker", "Temperature(℃) SP"))
        self.O2flow_SP.setText(_translate("Cellexus_CellMaker", "O2 Flow (lpm) SP"))
        self.Airflow_SP.setText(_translate("Cellexus_CellMaker", "Air Flow (lpm) SP"))
        self.acid_button.setText(_translate("Cellexus_CellMaker", "ACID"))
        self.base_button.setText(_translate("Cellexus_CellMaker", "BASE"))
        self.pHSP_label.setText(_translate("Cellexus_CellMaker", "pH SP"))
        self.AutopHBox.setTitle(_translate("Cellexus_CellMaker", "Automatic pH"))
        self.AutopH_switchlabel1.setText(_translate("Cellexus_CellMaker", "Off"))
        self.AutopH_switch.setText(_translate("Cellexus_CellMaker", ""))##
        self.AutopH_switchlabel2.setText(_translate("Cellexus_CellMaker", "On"))
        self.Automatic_Pump.setItemText(self.Automatic_Pump.indexOf(self.Automatic_pH), _translate("Cellexus_CellMaker", "Automatic pH"))
        self.AutoDOBox.setTitle(_translate("Cellexus_CellMaker", "Automatic DO"))
        self.AutoDO_switchlabel1.setText(_translate("Cellexus_CellMaker", "Off"))
        self.AutoDO_switch.setText(_translate("Cellexus_CellMaker", ""))##
        self.AutoDO_switchlabel2.setText(_translate("Cellexus_CellMaker", "On"))
        self.AutoDO_gaslabel.setText(_translate("Cellexus_CellMaker", "Gas"))
        self.AutoDO_O2label.setText(_translate("Cellexus_CellMaker", "pO2(%) SP"))
        self.AutoDO_gasswitch.setText(_translate("Cellexus_CellMaker", ""))##
        self.Automatic_Pump.setItemText(self.Automatic_Pump.indexOf(self.Automatic_DO), _translate("Cellexus_CellMaker", "Automatic DO"))
        self.FeedPumpbox.setTitle(_translate("Cellexus_CellMaker", "Feed Pump"))
        self.FeedPump_switchlabel1.setText(_translate("Cellexus_CellMaker", "Off"))
        self.FeedPump_switch.setText(_translate("Cellexus_CellMaker", ""))##
        self.FeedPump_switchlabel2.setText(_translate("Cellexus_CellMaker", "On"))
        self.RPM_label.setText(_translate("Cellexus_CellMaker", "Feed Pump RPM"))
        self.Automatic_Pump.setItemText(self.Automatic_Pump.indexOf(self.Feed_Pump), _translate("Cellexus_CellMaker", "Feed Pump"))
        self.DosingBox.setTitle(_translate("Cellexus_CellMaker", "Dosing Limits"))
        self.Dosing_switchlabel1.setText(_translate("Cellexus_CellMaker", "Off"))
        self.Dosing_switch.setText(_translate("Cellexus_CellMaker", ""))##
        self.Dosing_switchlabel2.setText(_translate("Cellexus_CellMaker", "On"))
        self.Acid_timelabel.setText(_translate("Cellexus_CellMaker", "Acid % cycle time"))
        self.Base_timelabel.setText(_translate("Cellexus_CellMaker", "Base % cycle time"))
        self.Automatic_Pump.setItemText(self.Automatic_Pump.indexOf(self.Acid_Base_Pump), _translate("Cellexus_CellMaker", "Acid\\Base Pumps"))
        self.Bioreactor_pic_acid.setText(_translate("Cellexus_CellMaker", "Acid"))
        self.acid_time.setDisplayFormat(_translate("Cellexus_CellMaker", "H:mm:ss"))
        self.Bioreactor_pic_base.setText(_translate("Cellexus_CellMaker", "Base"))
        self.Bioreactor_pic_heating.setText(_translate("Cellexus_CellMaker", "Heating"))
        self.Bioreactor_pic_cooling.setText(_translate("Cellexus_CellMaker", "Cooling"))
        self.base_time.setDisplayFormat(_translate("Cellexus_CellMaker", "H:mm:ss"))
        self.biopic_pHlabel.setText(_translate("Cellexus_CellMaker", "pH"))
        self.biopic_pO2label.setText(_translate("Cellexus_CellMaker", "pO2 (%air sat)"))
        self.biopic_templabel.setText(_translate("Cellexus_CellMaker", "Temperature(℃) "))
        self.biopic_pressurelabel.setText(_translate("Cellexus_CellMaker", "Pressure(mbar)"))
        self.device_box.setItemText(0, _translate("Cellexus_CellMaker", "Device 1"))
        self.device_box.setItemText(1, _translate("Cellexus_CellMaker", "Device 2"))
        self.device_box.setItemText(2, _translate("Cellexus_CellMaker", "Device 3"))
        self.O2limit_button_2.setText(_translate("Cellexus_CellMaker", "Limits"))
        self.O2limit_button_4.setText(_translate("Cellexus_CellMaker", "Other Gas"))
        self.O2limit_button_3.setText(_translate("Cellexus_CellMaker", "N2"))
        self.O2flow_label.setText(_translate("Cellexus_CellMaker", "O2 Flow (lpm)"))
        self.O2limit_button.setText(_translate("Cellexus_CellMaker", "Limits"))
        self.label_3.setText(_translate("Cellexus_CellMaker", "Air MinMax"))
        self.label_4.setText(_translate("Cellexus_CellMaker", "Air Flow (lpm)"))
        self.O2minmax_label.setText(_translate("Cellexus_CellMaker", "O2 MinMax"))
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
        self.actionNew.setText(_translate("Cellexus_CellMaker", "New"))
        self.actionOpen.setText(_translate("Cellexus_CellMaker", "Open"))
        self.actionSave.setText(_translate("Cellexus_CellMaker", "Save"))
        self.actionExit.setText(_translate("Cellexus_CellMaker", "Exit"))


    def buttonon(self):
        #on picture when cilcked it
        button=self.sender()##sender() is used to judge which button was clicked
        button.setIcon(QtGui.QIcon('image\button_on.png'))##
        button.setIconSize(QtCore.QSize(90,25))##
        
    def buttonoff(self):
        #off picture when clicked it again
        button=self.sender()
        button.setIcon(QtGui.QIcon('image\button_off.png'))##
        button.setIconSize(QtCore.QSize(90,25))##   
               
    def bticon(self,pressed):
        # when push the button
        if pressed:
            self.buttonon()
        else:
            self.buttonoff()
            
    def switchon(self):
        #on picture when cilcked it
        button=self.sender()##sender() is used to judge which button was clicked
        button.setIcon(QtGui.QIcon('image\on.png'))##
        button.setIconSize(QtCore.QSize(50,50))##
        
    def switchoff(self):
        #off picture when clicked it again
        button=self.sender()
        button.setIcon(QtGui.QIcon('image\off.png'))##
        button.setIconSize(QtCore.QSize(50,50))##   
               
    def swicon(self,pressed):
        # when push the button
        if pressed:
            self.switchon()
        else:
            self.switchoff()
            
    # other functions in the class here




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow() #widget->maindow
    ui = Ui_Cellexus_CellMaker() # CLASS NAME
    ui.setupUi(widget)
    widget.show()
    
    #bioreactor picture in main tab
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
        
            
    ALARM(38,39,1,0,1,0,1,2,1,0,1,2)
    
    sys.exit(app.exec_())
