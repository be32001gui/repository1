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
from PyQt5.uic import loadUi

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
        self.Run.setStyleSheet("QPushButton{border-image: url(image/button_off.png)}")##
        # self.Run.setIcon(QtGui.QIcon('image\button_off.png'))###set icon need\ set picture need/
        # self.Run.setIconSize(QtCore.QSize(120,35))##
        
        self.horizontalLayout_3.addWidget(self.Run)
        self.horizontalLayout.addWidget(self.modeBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        
        #main picture
        self.Bioreactor_pic = QtWidgets.QLabel(self.Main)
        self.Bioreactor_pic.setGeometry(QtCore.QRect(200, 170, 950, 580))#50->200 adjust the position
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
        self.acid_button.setMinimumSize(QtCore.QSize(90, 30))##
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.acid_button.setFont(font)
        #self.acid_button.setStyleSheet("background-color:rgba(255,255,255,133);border-color:rgba(0,0,0,255);color: rgba(0, 0, 0,255);border-style:solid;border-width:1px;border-radius:2px;")
        self.acid_button.setCheckable(True)
        self.acid_button.setAutoRepeat(True)
        self.acid_button.setAutoDefault(True)
        self.acid_button.setObjectName("acid_button")
        #button icon set
        self.acid_button.setStyleSheet("QPushButton{border-image: url(image/button_off.png)}")##
        # self.acid_button.setIcon(QtGui.QIcon('image\button_off.png'))###set icon need\ set picture need/
        # self.acid_button.setIconSize(QtCore.QSize(90,25))##
        self.gridLayout_2.addWidget(self.acid_button, 1, 0, 1, 1)
        
        #base button
        self.base_button = QtWidgets.QPushButton(self.AutopHFrame)
        self.base_button.setMinimumSize(QtCore.QSize(90, 30))##
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.base_button.setFont(font)
        #self.base_button.setStyleSheet("background-color:rgba(255,255,255,133);border-color:rgba(0,0,0,255);color: rgba(0, 0, 0,255);border-style:solid;border-width:1px;border-radius:2px;")
        self.base_button.setCheckable(True)
        self.base_button.setAutoRepeat(True)
        self.base_button.setAutoDefault(True)
        self.base_button.setObjectName("base_button")
        #button icon set
        self.base_button.setStyleSheet("QPushButton{border-image: url(image/button_off.png)}")##
        # self.base_button.setIcon(QtGui.QIcon('image\button_off.png'))###set icon need\ set picture need/
        # self.base_button.setIconSize(QtCore.QSize(90,25))##
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
        
#pic comment(acid and base time)
        self.formLayoutWidget = QtWidgets.QWidget(self.Main)
        self.formLayoutWidget.setGeometry(QtCore.QRect(640, 305, 170, 210))##
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
        #space between base and heating
        spacerItem8 = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)##100->85
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
        #spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem9)
        
        #space between heating and cooling
        spacerItem10 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)##
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem10)
        
#pic comment (pH pO2...)        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Main)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1150, 410, 131, 335))##380->410
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
        
        #space between temperature and pressure
        spacerItem13 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)##
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
        
#minmax limit comment        
        self.gridLayoutWidget = QtWidgets.QWidget(self.Main)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 445, 280, 240))##
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
        
        #"Ellie's code here"
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Charts)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1320, 20, 181, 401))
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
        self.widget1 = PlotWidget(self.Charts)
        self.widget1.setGeometry(QtCore.QRect(60, 30, 1201, 651))
        self.widget1.setObjectName("widget")
        self.widget1.setBackground('w')
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.Charts)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(60, 700, 1191, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.pushButton = QtWidgets.QPushButton(self.Charts)
        self.pushButton.setGeometry(QtCore.QRect(1360, 550, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browsefiles)  
        self.pushButton_2 = QtWidgets.QPushButton(self.Charts)
        self.pushButton_2.setGeometry(QtCore.QRect(1360, 630, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cleargraph)  
        self.verticalScrollBar = QtWidgets.QScrollBar(self.Charts)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1280, 30, 20, 641))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        
        
 #manual log tab
        self.Manual_Log = QtWidgets.QWidget()
        self.Manual_Log.setObjectName("Manual_Log")        
        self.tab1.addTab(self.Manual_Log, "")
        #
       #Individual controls
        self.interval = QtWidgets.QLabel(self.centralwidget)
        self.interval.setGeometry(QtCore.QRect(20, 90, 91, 16))
        self.interval.setObjectName("interval")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(20, 110, 141, 24))
        self.spinBox.setObjectName("interval_spinBox")
        
        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(10, 40, 141, 32))
        self.openFileButton.setObjectName("Open_file")
        
        self.openFileButton.clicked.connect(self.browsefiles_1) #open file browser
              
#file saving
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(738, 40, 151, 94))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.File_grid_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.File_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.File_grid_layout.setObjectName("File_grid_layout")
        self.filename = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.filename.setObjectName("filename")
        self.File_grid_layout.addWidget(self.filename, 2, 0, 1, 1)
        self.log = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.log.setObjectName("log")
        self.File_grid_layout.addWidget(self.log, 3, 0, 1, 1)
        self.file_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.file_name.setObjectName("file_name")
        self.File_grid_layout.addWidget(self.file_name, 1, 0, 1, 1)
        
#main section titles
        self.title_grid = QtWidgets.QGridLayout(self.gridLayoutWidget) 
        self.title_grid.setContentsMargins(0, 0, 0, 0)
        self.title_grid.setObjectName("title_grid")
        self.gridLayoutWidget.setStyleSheet("background-color:white;")
        self.do2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.do2.setObjectName("do2")
        self.title_grid.addWidget(self.do2, 2, 4, 1, 1)
        self.test = QtWidgets.QLabel(self.gridLayoutWidget)
        self.test.setObjectName("test")
        self.title_grid.addWidget(self.test, 0, 1, 1, 1)
        self.temperature = QtWidgets.QLabel(self.gridLayoutWidget)
        self.temperature.setObjectName("temperature")
        self.title_grid.addWidget(self.temperature, 2, 1, 1, 1)
        self.pH = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pH.setObjectName("pH")
        self.title_grid.addWidget(self.pH, 2, 3, 1, 1)
        self.co2flow = QtWidgets.QLabel(self.gridLayoutWidget)
        self.co2flow.setObjectName("co2flow")
        self.title_grid.addWidget(self.co2flow, 2, 7, 1, 1)
        self.pressure = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pressure.setObjectName("pressure")
        self.title_grid.addWidget(self.pressure, 2, 2, 1, 1)
        self.date = QtWidgets.QLabel(self.gridLayoutWidget)
        self.date.setObjectName("date")
        self.title_grid.addWidget(self.date, 0, 0, 1, 1)
        self.motor = QtWidgets.QLabel(self.gridLayoutWidget)
        self.motor.setObjectName("motor")
        self.title_grid.addWidget(self.motor, 2, 8, 1, 1)
        self.o2flow = QtWidgets.QLabel(self.gridLayoutWidget)
        self.o2flow.setObjectName("o2flow")
        self.title_grid.addWidget(self.o2flow, 2, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.title_grid.addItem(spacerItem, 1, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.title_grid.addItem(spacerItem1, 1, 7, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.title_grid.addItem(spacerItem2, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.title_grid.addItem(spacerItem3, 1, 5, 1, 1)
        self.group = QtWidgets.QLabel(self.gridLayoutWidget)
        self.group.setObjectName("group")
        self.title_grid.addWidget(self.group, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.title_grid.addItem(spacerItem4, 1, 8, 1, 1)
        self.datetime = QtWidgets.QLabel(self.gridLayoutWidget)
        self.datetime.setObjectName("datetime")
        self.title_grid.addWidget(self.datetime, 2, 0, 1, 1)
        self.airflow = QtWidgets.QLabel(self.gridLayoutWidget)
        self.airflow.setObjectName("airflow")
        self.title_grid.addWidget(self.airflow, 2, 5, 1, 1)
        self.operator_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.operator_2.setObjectName("operator_2")
        self.title_grid.addWidget(self.operator_2, 0, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setMinimumSize(QtCore.QSize(141, 0))
        self.dateEdit.setObjectName("dateEdit")
        self.title_grid.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(81, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(81, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.title_grid.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(81, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.title_grid.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(81, 16777215))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.title_grid.addWidget(self.lineEdit_4, 1, 3, 1, 1)
        
        #scroll area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(18, 248, 875, 350))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 871, 470))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 871, 434))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setStyleSheet("background-color:white;")
        
        #text boxes
        self.lineEdit_27 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout.addWidget(self.lineEdit_27, 2, 3, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout.addWidget(self.lineEdit_28, 3, 3, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout.addWidget(self.lineEdit_18, 11, 1, 1, 1)
        self.lineEdit_83 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_83.setObjectName("lineEdit_83")
        self.gridLayout.addWidget(self.lineEdit_83, 10, 8, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout.addWidget(self.lineEdit_26, 1, 3, 1, 1)
        self.lineEdit_59 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.gridLayout.addWidget(self.lineEdit_59, 7, 7, 1, 1)
        self.lineEdit_93 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_93.setObjectName("lineEdit_93")
        self.gridLayout.addWidget(self.lineEdit_93, 8, 2, 1, 1)
        self.lineEdit_64 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.gridLayout.addWidget(self.lineEdit_64, 4, 8, 1, 1)
        self.lineEdit_89 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_89.setObjectName("lineEdit_89")
        self.gridLayout.addWidget(self.lineEdit_89, 9, 6, 1, 1)
        self.lineEdit_68 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.gridLayout.addWidget(self.lineEdit_68, 12, 1, 1, 1)
        self.lineEdit_65 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.gridLayout.addWidget(self.lineEdit_65, 6, 8, 1, 1)
        self.lineEdit_96 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_96.setObjectName("lineEdit_96")
        self.gridLayout.addWidget(self.lineEdit_96, 8, 5, 1, 1)
        self.lineEdit_87 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_87.setObjectName("lineEdit_87")
        self.gridLayout.addWidget(self.lineEdit_87, 9, 4, 1, 1)
        self.lineEdit_69 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.gridLayout.addWidget(self.lineEdit_69, 12, 2, 1, 1)
        self.lineEdit_91 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_91.setObjectName("lineEdit_91")
        self.gridLayout.addWidget(self.lineEdit_91, 9, 8, 1, 1)
        self.lineEdit_85 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_85.setObjectName("lineEdit_85")
        self.gridLayout.addWidget(self.lineEdit_85, 9, 2, 1, 1)
        self.lineEdit_76 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.gridLayout.addWidget(self.lineEdit_76, 10, 1, 1, 1)
        self.lineEdit_74 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.gridLayout.addWidget(self.lineEdit_74, 12, 7, 1, 1)
        self.lineEdit_86 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_86.setObjectName("lineEdit_86")
        self.gridLayout.addWidget(self.lineEdit_86, 9, 3, 1, 1)
        self.lineEdit_88 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_88.setObjectName("lineEdit_88")
        self.gridLayout.addWidget(self.lineEdit_88, 9, 5, 1, 1)
        self.lineEdit_43 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.gridLayout.addWidget(self.lineEdit_43, 4, 5, 1, 1)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout.addWidget(self.lineEdit_38, 7, 4, 1, 1)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout.addWidget(self.lineEdit_36, 4, 4, 1, 1)
        self.lineEdit_44 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.gridLayout.addWidget(self.lineEdit_44, 6, 5, 1, 1)
        self.lineEdit_46 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.gridLayout.addWidget(self.lineEdit_46, 11, 5, 1, 1)
        self.lineEdit_45 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.gridLayout.addWidget(self.lineEdit_45, 7, 5, 1, 1)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.gridLayout.addWidget(self.lineEdit_39, 11, 4, 1, 1)
        self.lineEdit_53 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.gridLayout.addWidget(self.lineEdit_53, 11, 6, 1, 1)
        self.lineEdit_92 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_92.setObjectName("lineEdit_92")
        self.gridLayout.addWidget(self.lineEdit_92, 8, 1, 1, 1)
        self.lineEdit_41 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.gridLayout.addWidget(self.lineEdit_41, 2, 5, 1, 1)
        self.lineEdit_56 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.gridLayout.addWidget(self.lineEdit_56, 3, 7, 1, 1)
        self.lineEdit_60 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.gridLayout.addWidget(self.lineEdit_60, 11, 7, 1, 1)
        self.lineEdit_50 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.gridLayout.addWidget(self.lineEdit_50, 4, 6, 1, 1)
        self.lineEdit_67 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.gridLayout.addWidget(self.lineEdit_67, 11, 8, 1, 1)
        self.lineEdit_77 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.gridLayout.addWidget(self.lineEdit_77, 10, 2, 1, 1)
        self.lineEdit_84 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_84.setObjectName("lineEdit_84")
        self.gridLayout.addWidget(self.lineEdit_84, 9, 1, 1, 1)
        self.lineEdit_90 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_90.setObjectName("lineEdit_90")
        self.gridLayout.addWidget(self.lineEdit_90, 9, 7, 1, 1)
        self.lineEdit_98 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_98.setObjectName("lineEdit_98")
        self.gridLayout.addWidget(self.lineEdit_98, 8, 7, 1, 1)
        self.lineEdit_49 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.gridLayout.addWidget(self.lineEdit_49, 3, 6, 1, 1)
        self.lineEdit_72 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.gridLayout.addWidget(self.lineEdit_72, 12, 5, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout.addWidget(self.lineEdit_34, 2, 4, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout.addWidget(self.lineEdit_19, 7, 2, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout.addWidget(self.lineEdit_35, 3, 4, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout.addWidget(self.lineEdit_20, 1, 2, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout.addWidget(self.lineEdit_17, 7, 1, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout.addWidget(self.lineEdit_31, 7, 3, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 6, 1, 1, 1)
        self.lineEdit_58 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.gridLayout.addWidget(self.lineEdit_58, 6, 7, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout.addWidget(self.lineEdit_29, 4, 3, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout.addWidget(self.lineEdit_32, 11, 3, 1, 1)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout.addWidget(self.lineEdit_37, 6, 4, 1, 1)
        self.lineEdit_99 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_99.setObjectName("lineEdit_99")
        self.gridLayout.addWidget(self.lineEdit_99, 8, 8, 1, 1)
        self.lineEdit_75 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.gridLayout.addWidget(self.lineEdit_75, 12, 8, 1, 1)
        self.lineEdit_54 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.gridLayout.addWidget(self.lineEdit_54, 1, 7, 1, 1)
        self.lineEdit_81 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_81.setObjectName("lineEdit_81")
        self.gridLayout.addWidget(self.lineEdit_81, 10, 6, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout.addWidget(self.lineEdit_30, 6, 3, 1, 1)
        self.lineEdit_52 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.gridLayout.addWidget(self.lineEdit_52, 7, 6, 1, 1)
        self.lineEdit_73 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.gridLayout.addWidget(self.lineEdit_73, 12, 6, 1, 1)
        self.lineEdit_42 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.gridLayout.addWidget(self.lineEdit_42, 3, 5, 1, 1)
        self.lineEdit_78 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.gridLayout.addWidget(self.lineEdit_78, 10, 3, 1, 1)
        self.lineEdit_48 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.gridLayout.addWidget(self.lineEdit_48, 2, 6, 1, 1)
        self.lineEdit_82 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_82.setObjectName("lineEdit_82")
        self.gridLayout.addWidget(self.lineEdit_82, 10, 7, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 1, 1, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout.addWidget(self.lineEdit_25, 11, 2, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 4, 1, 1, 1)
        self.lineEdit_51 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.gridLayout.addWidget(self.lineEdit_51, 6, 6, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout.addWidget(self.lineEdit_21, 2, 2, 1, 1)
        self.lineEdit_95 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_95.setObjectName("lineEdit_95")
        self.gridLayout.addWidget(self.lineEdit_95, 8, 4, 1, 1)
        self.lineEdit_55 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.gridLayout.addWidget(self.lineEdit_55, 2, 7, 1, 1)
        self.lineEdit_80 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_80.setObjectName("lineEdit_80")
        self.gridLayout.addWidget(self.lineEdit_80, 10, 5, 1, 1)
        self.lineEdit_57 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.gridLayout.addWidget(self.lineEdit_57, 4, 7, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout.addWidget(self.lineEdit_23, 4, 2, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout.addWidget(self.lineEdit_22, 3, 2, 1, 1)
        self.lineEdit_62 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.gridLayout.addWidget(self.lineEdit_62, 2, 8, 1, 1)
        self.lineEdit_63 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.gridLayout.addWidget(self.lineEdit_63, 3, 8, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 2, 1, 1, 1)
        self.lineEdit_79 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_79.setObjectName("lineEdit_79")
        self.gridLayout.addWidget(self.lineEdit_79, 10, 4, 1, 1)
        self.lineEdit_70 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.gridLayout.addWidget(self.lineEdit_70, 12, 3, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout.addWidget(self.lineEdit_33, 1, 4, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 3, 1, 1, 1)
        self.lineEdit_47 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.gridLayout.addWidget(self.lineEdit_47, 1, 6, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout.addWidget(self.lineEdit_24, 6, 2, 1, 1)
        self.lineEdit_66 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.gridLayout.addWidget(self.lineEdit_66, 7, 8, 1, 1)
        self.lineEdit_40 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.gridLayout.addWidget(self.lineEdit_40, 1, 5, 1, 1)
        self.lineEdit_61 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.gridLayout.addWidget(self.lineEdit_61, 1, 8, 1, 1)
        self.lineEdit_71 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.gridLayout.addWidget(self.lineEdit_71, 12, 4, 1, 1)
        self.lineEdit_94 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_94.setObjectName("lineEdit_94")
        self.gridLayout.addWidget(self.lineEdit_94, 8, 3, 1, 1)
        self.lineEdit_97 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_97.setObjectName("lineEdit_97")
        self.gridLayout.addWidget(self.lineEdit_97, 8, 6, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 0, 7, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 0, 3, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 0, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 0, 4, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 0, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 0, 8, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 0, 6, 1, 1)
        self.lineEdit_100 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_100.setObjectName("lineEdit_100")
        self.gridLayout.addWidget(self.lineEdit_100, 5, 1, 1, 1)
        self.lineEdit_101 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_101.setObjectName("lineEdit_101")
        self.gridLayout.addWidget(self.lineEdit_101, 5, 2, 1, 1)
        self.lineEdit_102 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_102.setObjectName("lineEdit_102")
        self.gridLayout.addWidget(self.lineEdit_102, 5, 3, 1, 1)
        self.lineEdit_103 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_103.setObjectName("lineEdit_103")
        self.gridLayout.addWidget(self.lineEdit_103, 5, 4, 1, 1)
        self.lineEdit_104 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_104.setObjectName("lineEdit_104")
        self.gridLayout.addWidget(self.lineEdit_104, 5, 5, 1, 1)
        self.lineEdit_105 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_105.setObjectName("lineEdit_105")
        self.gridLayout.addWidget(self.lineEdit_105, 5, 6, 1, 1)
        self.lineEdit_106 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_106.setObjectName("lineEdit_106")
        self.gridLayout.addWidget(self.lineEdit_106, 5, 7, 1, 1)
        self.lineEdit_107 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_107.setObjectName("lineEdit_107")
        self.gridLayout.addWidget(self.lineEdit_107, 5, 8, 1, 1)
        self.lineEdit_108 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_108.setObjectName("lineEdit_108")
        self.gridLayout.addWidget(self.lineEdit_108, 13, 1, 1, 1)
        self.lineEdit_109 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_109.setObjectName("lineEdit_109")
        self.gridLayout.addWidget(self.lineEdit_109, 13, 2, 1, 1)
        self.lineEdit_110 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_110.setObjectName("lineEdit_110")
        self.gridLayout.addWidget(self.lineEdit_110, 13, 3, 1, 1)
        self.lineEdit_111 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_111.setObjectName("lineEdit_111")
        self.gridLayout.addWidget(self.lineEdit_111, 13, 4, 1, 1)
        self.lineEdit_112 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_112.setObjectName("lineEdit_112")
        self.gridLayout.addWidget(self.lineEdit_112, 13, 5, 1, 1)
        self.lineEdit_113 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_113.setObjectName("lineEdit_113")
        self.gridLayout.addWidget(self.lineEdit_113, 13, 6, 1, 1)
        self.lineEdit_114 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_114.setObjectName("lineEdit_114")
        self.gridLayout.addWidget(self.lineEdit_114, 13, 7, 1, 1)
        self.lineEdit_115 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_115.setObjectName("lineEdit_115")
        self.gridLayout.addWidget(self.lineEdit_115, 13, 8, 1, 1)
        self.lineEdit_116 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_116.setObjectName("lineEdit_116")
        self.gridLayout.addWidget(self.lineEdit_116, 13, 1, 1, 1)
        self.lineEdit_117 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_117.setObjectName("lineEdit_117")
        self.gridLayout.addWidget(self.lineEdit_117, 13, 2, 1, 1)
        self.lineEdit_118 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_118.setObjectName("lineEdit_118")
        self.gridLayout.addWidget(self.lineEdit_118, 13, 3, 1, 1)
        self.lineEdit_119 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_119.setObjectName("lineEdit_119")
        self.gridLayout.addWidget(self.lineEdit_119, 13, 4, 1, 1)
        self.lineEdit_120 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_120.setObjectName("lineEdit_120")
        self.gridLayout.addWidget(self.lineEdit_120, 13, 5, 1, 1)
        self.lineEdit_121 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_121.setObjectName("lineEdit_121")
        self.gridLayout.addWidget(self.lineEdit_121, 13, 6, 1, 1)
        self.lineEdit_122 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_122.setObjectName("lineEdit_122")
        self.gridLayout.addWidget(self.lineEdit_122, 13, 7, 1, 1)
        self.lineEdit_123 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_123.setObjectName("lineEdit_123")
        self.gridLayout.addWidget(self.lineEdit_123, 13, 8, 1, 1)
        
        #date time boxes
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 0, 0, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout.addWidget(self.dateTimeEdit_2, 1, 0, 1, 1)
        self.dateTimeEdit_4 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_4.setObjectName("dateTimeEdit_4")
        self.gridLayout.addWidget(self.dateTimeEdit_4, 2, 0, 1, 1)
        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.gridLayout.addWidget(self.dateTimeEdit_3, 3, 0, 1, 1)
        self.dateTimeEdit_6 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_6.setObjectName("dateTimeEdit_6")
        self.gridLayout.addWidget(self.dateTimeEdit_6, 4, 0, 1, 1)
        self.dateTimeEdit_11 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_11.setObjectName("dateTimeEdit_11")
        self.gridLayout.addWidget(self.dateTimeEdit_11, 5, 0, 1, 1)
        self.dateTimeEdit_5 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_5.setObjectName("dateTimeEdit_5")
        self.gridLayout.addWidget(self.dateTimeEdit_5, 6, 0, 1, 1)
        self.dateTimeEdit_13 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_13.setObjectName("dateTimeEdit_13")
        self.gridLayout.addWidget(self.dateTimeEdit_13, 7, 0, 1, 1)
        self.dateTimeEdit_10 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_10.setObjectName("dateTimeEdit_10")
        self.gridLayout.addWidget(self.dateTimeEdit_10, 8, 0, 1, 1)
        self.dateTimeEdit_9 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_9.setObjectName("dateTimeEdit_9")
        self.gridLayout.addWidget(self.dateTimeEdit_9, 9, 0, 1, 1)
        self.dateTimeEdit_8 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_8.setObjectName("dateTimeEdit_8")
        self.gridLayout.addWidget(self.dateTimeEdit_8, 10, 0, 1, 1)
        self.dateTimeEdit_14 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_14.setObjectName("dateTimeEdit_14")
        self.gridLayout.addWidget(self.dateTimeEdit_14, 11, 0, 1, 1)
        self.dateTimeEdit_7 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_7.setObjectName("dateTimeEdit_7")
        self.gridLayout.addWidget(self.dateTimeEdit_7, 12, 0, 1, 1)
        self.dateTimeEdit_15 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_15.setObjectName("dateTimeEdit_15")
        self.gridLayout.addWidget(self.dateTimeEdit_15, 13, 0, 1, 1)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        
        #set point controls
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(910, 40, 139, 541))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.setpoint_grid_layout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.setpoint_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.setpoint_grid_layout.setObjectName("setpoint_grid_layout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.setpoint_grid_layout.addItem(spacerItem5, 12, 0, 1, 1)
        self.O2_flow = QtWidgets.QLabel(self.formLayoutWidget)
        self.O2_flow.setObjectName("O2_flow")
        self.setpoint_grid_layout.addWidget(self.O2_flow, 13, 0, 1, 1)
        self.feedpump_control = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.feedpump_control.setObjectName("feedpump_control")
        self.setpoint_grid_layout.addWidget(self.feedpump_control, 8, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.setpoint_grid_layout.addItem(spacerItem6, 5, 0, 1, 1)
        self.airflow_control = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.airflow_control.setObjectName("airflow_control")
        self.setpoint_grid_layout.addWidget(self.airflow_control, 18, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.setpoint_grid_layout.addItem(spacerItem7, 16, 0, 1, 1)
        self.airflow_num = QtWidgets.QLCDNumber(self.formLayoutWidget)
        self.airflow_num.setStyleSheet("QLCDNumber{\n"
"    background-color: rgb(96, 95, 97);\n"
"}")
        self.airflow_num.setObjectName("airflow_num")
        self.setpoint_grid_layout.addWidget(self.airflow_num, 19, 0, 1, 1)
        self.feed_pump = QtWidgets.QPushButton(self.formLayoutWidget)
        self.feed_pump.setObjectName("feed_pump")
        self.setpoint_grid_layout.addWidget(self.feed_pump, 6, 0, 1, 1)
        self.Mode = QtWidgets.QLabel(self.formLayoutWidget)
        self.Mode.setObjectName("Mode")
        self.setpoint_grid_layout.addWidget(self.Mode, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Temperature = QtWidgets.QLabel(self.formLayoutWidget)
        self.Temperature.setObjectName("Temperature")
        self.setpoint_grid_layout.addWidget(self.Temperature, 10, 0, 1, 1)
        self.Airflow = QtWidgets.QLabel(self.formLayoutWidget)
        self.Airflow.setObjectName("Airflow")
        self.setpoint_grid_layout.addWidget(self.Airflow, 17, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.O2flow_control = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.O2flow_control.setObjectName("O2flow_control")
        self.setpoint_grid_layout.addWidget(self.O2flow_control, 14, 0, 1, 1)
        self.O2flow_num = QtWidgets.QLCDNumber(self.formLayoutWidget)
        self.O2flow_num.setStyleSheet("QLCDNumber{\n"
"    background-color: rgb(96, 95, 97);\n"
"}")
        self.O2flow_num.setObjectName("O2flow_num")
        self.setpoint_grid_layout.addWidget(self.O2flow_num, 15, 0, 1, 1)
        self.mode = QtWidgets.QComboBox(self.formLayoutWidget)
        self.mode.setObjectName("mode")
        self.mode.addItem("")
        self.mode.addItem("")
        self.setpoint_grid_layout.addWidget(self.mode, 3, 0, 1, 1)
        self.temperature_control = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.temperature_control.setObjectName("temperature_control")
        self.setpoint_grid_layout.addWidget(self.temperature_control, 11, 0, 1, 1)
        self.feed_pump_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.feed_pump_2.setObjectName("feed_pump_2")
        self.setpoint_grid_layout.addWidget(self.feed_pump_2, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.setpoint_grid_layout.addItem(spacerItem8, 9, 0, 1, 1)
        self.run = QtWidgets.QPushButton(self.formLayoutWidget)
        self.run.setObjectName("run")
        self.setpoint_grid_layout.addWidget(self.run, 4, 0, 1, 1)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
       
        self.checkBoxTemp.setText(_translate("Cellexus_CellMaker", "Temperature - Red"))
        self.checkBoxPres.setText(_translate("Cellexus_CellMaker", "Pressure - Orange"))
        self.checkBoxPH.setText(_translate("Cellexus_CellMaker", "pH - Yellow"))
        self.checkBoxDO2.setText(_translate("Cellexus_CellMaker", "dO2 - Green"))
        self.checkBoxAIR.setText(_translate("Cellexus_CellMaker", "Airflow - Blue"))
        self.checkBoxO2.setText(_translate("Cellexus_CellMaker", "O2 Flow - Purple"))
        self.checkBoxCO2.setText(_translate("Cellexus_CellMaker", "CO2 Flow - Pink"))
        self.pushButton.setText(_translate("Cellexus_CellMaker", "Export"))
        self.pushButton_2.setText(_translate("Cellexus_CellMaker", "Clear"))
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Cellexus_Cellmaker", "Cellexus_Cellmaker"))
        self.do2.setText(_translate("Cellexus_Cellmaker", "dO2"))
        self.test.setText(_translate("Cellexus_Cellmaker", "Test"))
        self.temperature.setText(_translate("Cellexus_Cellmaker", "Temperature"))
        self.pH.setText(_translate("Cellexus_Cellmaker", "pH"))
        self.co2flow.setText(_translate("Cellexus_Cellmaker", "CO2 Flow"))
        self.pressure.setText(_translate("Cellexus_Cellmaker", "Pressure"))
        self.date.setText(_translate("Cellexus_Cellmaker", "Date"))
        self.motor.setText(_translate("Cellexus_Cellmaker", "Motor"))
        self.o2flow.setText(_translate("Cellexus_Cellmaker", "O2 Flow"))
        self.group.setText(_translate("Cellexus_Cellmaker", "Group"))
        self.datetime.setText(_translate("Cellexus_Cellmaker", "Date/Time"))
        self.airflow.setText(_translate("Cellexus_Cellmaker", "Air Flow"))
        self.operator_2.setText(_translate("Cellexus_Cellmaker", "Operator"))
        self.filename.setText(_translate("Cellexus_Cellmaker", "Manual Log"))
        self.log.setText(_translate("Cellexus_Cellmaker", "Log"))
        self.file_name.setText(_translate("Cellexus_Cellmaker", "Manual Log File Name "))
        self.interval.setText(_translate("Cellexus_Cellmaker", "Interval (s)"))
        self.O2_flow.setText(_translate("Cellexus_Cellmaker", "O2 Flow (lpm) SP"))
        self.feed_pump.setText(_translate("Cellexus_Cellmaker", "Feed Pump ON"))
        self.Mode.setText(_translate("Cellexus_Cellmaker", "Mode"))
        self.Temperature.setText(_translate("Cellexus_Cellmaker", "Temperature (ºC) SP"))
        self.Airflow.setText(_translate("Cellexus_Cellmaker", "Air Flow (lpm) SP"))
        self.mode.setItemText(0, _translate("Cellexus_Cellmaker", "Setpoint"))
        self.mode.setItemText(1, _translate("Cellexus_Cellmaker", "Recipe"))
        self.feed_pump_2.setText(_translate("Cellexus_Cellmaker", "Feed Pump RPM"))
        self.run.setText(_translate("Cellexus_Cellmaker", "RUN"))
        self.openFileButton.setText(_translate("Cellexus_Cellmaker", "Open file"))
        self.tab1.setTabText(self.tab1.indexOf(self.Manual_Log), _translate("Cellexus_CellMaker", "Manual Log"))

    def buttonon(self):
        #on picture when cilcked it
        button=self.sender()##sender() is used to judge which button was clicked
        button.setStyleSheet("QPushButton{border-image: url(image/button_on.png)}")##
       
    def buttonoff(self):
        #off picture when clicked it again
        button=self.sender()
        button.setStyleSheet("QPushButton{border-image: url(image/button_off.png)}")##
        
               
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

    def browsefiles_1(self):
        fname = QFileDialog.getSaveFileName(self, 'Open File', 'D:\Documents')  
        
    def cleargraph(self):
        
        if self.checkBoxTemp.isChecked():
            self.checkBoxTemp.setCheckState(0)
            self.widget1.clear()
            
        if self.checkBoxPres.isChecked():
            self.checkBoxPres.setCheckState(0)
            self.widget1.clear()
            
        if self.checkBoxPH.isChecked():
            self.checkBoxPH.setCheckState(0)
            self.widget1.clear()
            
        if self.checkBoxDO2.isChecked():
            self.checkBoxDO2.setCheckState(0) 
            self.widget1.clear()
            
        if self.checkBoxAIR.isChecked():
            self.checkBoxAIR.setCheckState(0)
            self.widget1.clear()
            
        if self.checkBoxO2.isChecked():
            self.checkBoxO2.setCheckState(0)  
            self.widget1.clear()
            
        if self.checkBoxCO2.isChecked():
            self.checkBoxCO2.setCheckState(0)
            self.widget1.clear()
            
    def checked_item(self):
        if self.checkBoxTemp.isChecked():
            x=[1,2,3]
            y=[2,3,4]
            pen = pg.mkPen(color=(255, 0, 0), width=3)
            self.widget1.plot(x, y, pen=pen)
            
        if self.checkBoxPres.isChecked():
            x=[2,3,4]
            y=[2,3,4]
            pen = pg.mkPen(color=(255, 155, 55), width=3)
            self.widget1.plot(x, y, pen=pen)
            
        if self.checkBoxPH.isChecked():
            x=[3,4,5]
            y=[2,3,4]
            pen = pg.mkPen(color=(255, 255, 0), width=3)
            self.widget1.plot(x, y, pen=pen) 
            
        if self.checkBoxDO2.isChecked():
            x=[4,5,6]
            y=[2,3,4]
            pen = pg.mkPen(color=(100, 200, 50), width=3)
            self.widget1.plot(x, y, pen=pen)    
         
        if self.checkBoxAIR.isChecked():
            x=[5,6,7]
            y=[2,3,4]
            pen = pg.mkPen(color=(0, 0, 255), width=3)
            self.widget1.plot(x, y, pen=pen) 
            
        if self.checkBoxO2.isChecked():
            x=[6,7,8]
            y=[2,3,4]
            pen = pg.mkPen(color=(200, 0, 255), width=3)
            self.widget1.plot(x, y, pen=pen) 
            
        if self.checkBoxCO2.isChecked():
            x=[7,8,9]
            y=[2,3,4]
            pen = pg.mkPen(color=(248, 24, 148), width=3)
            self.widget1.plot(x, y, pen=pen)
            
        #manual log tab browse files     
        def browsefiles(self):
            fname = QFileDialog.getOpenFileName(self, 'Open File', 'D:\Documents')


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
