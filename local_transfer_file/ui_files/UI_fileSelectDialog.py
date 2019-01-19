# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileSelectDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-image: url(:/img/background.jpeg);\n"
"\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 12, 741, 531))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fileMode = QtWidgets.QRadioButton(self.widget)
        self.fileMode.setStyleSheet("font:24pt \"Microsoft YaHei UI\";\n"
"color:rgba(55,152,251,1);\n"
"font-size:24px;\n"
"line-height:67px;")
        self.fileMode.setChecked(True)
        self.fileMode.setObjectName("fileMode")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.fileMode)
        self.horizontalLayout_3.addWidget(self.fileMode)
        self.directorMode = QtWidgets.QRadioButton(self.widget)
        self.directorMode.setStyleSheet("font:24pt \"Microsoft YaHei UI\";\n"
"color:rgba(55,152,251,1);\n"
"font-size:24px;\n"
"line-height:67px;")
        self.directorMode.setObjectName("directorMode")
        self.buttonGroup.addButton(self.directorMode)
        self.horizontalLayout_3.addWidget(self.directorMode)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font:24pt \"Microsoft YaHei UI\";\n"
"color:rgba(55,152,251,1);\n"
"font-size:24px;\n"
"line-height:67px;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.showFilePath = QtWidgets.QLineEdit(self.widget)
        self.showFilePath.setObjectName("showFilePath")
        self.horizontalLayout.addWidget(self.showFilePath)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setStyleSheet("font:24px \"Microsoft YaHei UI\";\n"
"background-color:#3385ff;\n"
"color:rgba(255,255,255,1);\n"
"background:rgba(78,162,255,1);\n"
"border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.showUrlText = QtWidgets.QTextEdit(self.widget)
        self.showUrlText.setObjectName("showUrlText")
        self.verticalLayout.addWidget(self.showUrlText)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("font:36px \"Microsoft YaHei UI\";\n"
"background-color:#3385ff;\n"
"color:rgba(255,255,255,1);\n"
"background:rgba(78,162,255,1);\n"
"border-radius:15px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton_3.setStyleSheet("font:36px \"Microsoft YaHei UI\";\n"
"background-color:#3385ff;\n"
"color:rgba(255,255,255,1);\n"
"background:rgba(78,162,255,1);\n"
"border-radius:15px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.selectFilePath)
        self.pushButton_2.clicked.connect(MainWindow.generateQRCode)
        self.pushButton_3.clicked.connect(MainWindow.closeWindow)
        self.buttonGroup.buttonClicked['QAbstractButton*'].connect(MainWindow.selectFileMode)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件传输"))
        self.fileMode.setText(_translate("MainWindow", "文件"))
        self.directorMode.setText(_translate("MainWindow", "文件夹"))
        self.label.setText(_translate("MainWindow", "文件（夹）路径:"))
        self.pushButton.setText(_translate("MainWindow", "选择"))
        self.pushButton_2.setText(_translate("MainWindow", "生成二维码"))
        self.pushButton_3.setText(_translate("MainWindow", "取消"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "软件说明"))
        self.action_2.setText(_translate("MainWindow", "软件版本"))
        self.action_3.setText(_translate("MainWindow", "关于"))

from local_transfer_file import resource_rc
