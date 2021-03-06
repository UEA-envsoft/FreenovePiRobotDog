# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlexsDogPosToolui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 341, 411))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("spike_legs3.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.leftShoulderInOut = QtWidgets.QLineEdit(self.centralwidget)
        self.leftShoulderInOut.setGeometry(QtCore.QRect(490, 10, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leftShoulderInOut.setFont(font)
        self.leftShoulderInOut.setAlignment(QtCore.Qt.AlignCenter)
        self.leftShoulderInOut.setObjectName("leftShoulderInOut")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 40, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.leftShoulderFB = QtWidgets.QLineEdit(self.centralwidget)
        self.leftShoulderFB.setGeometry(QtCore.QRect(490, 40, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leftShoulderFB.setFont(font)
        self.leftShoulderFB.setAlignment(QtCore.Qt.AlignCenter)
        self.leftShoulderFB.setObjectName("leftShoulderFB")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 70, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.leftElbowFB = QtWidgets.QLineEdit(self.centralwidget)
        self.leftElbowFB.setGeometry(QtCore.QRect(490, 70, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leftElbowFB.setFont(font)
        self.leftElbowFB.setAlignment(QtCore.Qt.AlignCenter)
        self.leftElbowFB.setObjectName("leftElbowFB")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 130, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.leftKneeFB = QtWidgets.QLineEdit(self.centralwidget)
        self.leftKneeFB.setGeometry(QtCore.QRect(490, 160, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leftKneeFB.setFont(font)
        self.leftKneeFB.setAlignment(QtCore.Qt.AlignCenter)
        self.leftKneeFB.setObjectName("leftKneeFB")
        self.leftHipFB = QtWidgets.QLineEdit(self.centralwidget)
        self.leftHipFB.setGeometry(QtCore.QRect(490, 130, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leftHipFB.setFont(font)
        self.leftHipFB.setAlignment(QtCore.Qt.AlignCenter)
        self.leftHipFB.setObjectName("leftHipFB")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 160, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 100, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.leftHipInOut = QtWidgets.QLineEdit(self.centralwidget)
        self.leftHipInOut.setGeometry(QtCore.QRect(490, 100, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leftHipInOut.setFont(font)
        self.leftHipInOut.setAlignment(QtCore.Qt.AlignCenter)
        self.leftHipInOut.setObjectName("leftHipInOut")
        self.rightHipInOut = QtWidgets.QLineEdit(self.centralwidget)
        self.rightHipInOut.setGeometry(QtCore.QRect(490, 190, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rightHipInOut.setFont(font)
        self.rightHipInOut.setAlignment(QtCore.Qt.AlignCenter)
        self.rightHipInOut.setObjectName("rightHipInOut")
        self.rightHipFB = QtWidgets.QLineEdit(self.centralwidget)
        self.rightHipFB.setGeometry(QtCore.QRect(490, 220, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rightHipFB.setFont(font)
        self.rightHipFB.setAlignment(QtCore.Qt.AlignCenter)
        self.rightHipFB.setObjectName("rightHipFB")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 250, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(370, 190, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(370, 220, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.rightKneeFB = QtWidgets.QLineEdit(self.centralwidget)
        self.rightKneeFB.setGeometry(QtCore.QRect(490, 250, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rightKneeFB.setFont(font)
        self.rightKneeFB.setAlignment(QtCore.Qt.AlignCenter)
        self.rightKneeFB.setObjectName("rightKneeFB")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(370, 310, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.rightElbowFB = QtWidgets.QLineEdit(self.centralwidget)
        self.rightElbowFB.setGeometry(QtCore.QRect(490, 340, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rightElbowFB.setFont(font)
        self.rightElbowFB.setAlignment(QtCore.Qt.AlignCenter)
        self.rightElbowFB.setObjectName("rightElbowFB")
        self.rightShoulderFB = QtWidgets.QLineEdit(self.centralwidget)
        self.rightShoulderFB.setGeometry(QtCore.QRect(490, 310, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rightShoulderFB.setFont(font)
        self.rightShoulderFB.setAlignment(QtCore.Qt.AlignCenter)
        self.rightShoulderFB.setObjectName("rightShoulderFB")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(370, 340, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(370, 280, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.rightShoulderInOut = QtWidgets.QLineEdit(self.centralwidget)
        self.rightShoulderInOut.setGeometry(QtCore.QRect(490, 280, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rightShoulderInOut.setFont(font)
        self.rightShoulderInOut.setAlignment(QtCore.Qt.AlignCenter)
        self.rightShoulderInOut.setObjectName("rightShoulderInOut")
        self.angle2xyz = QtWidgets.QPushButton(self.centralwidget)
        self.angle2xyz.setGeometry(QtCore.QRect(360, 370, 81, 51))
        self.angle2xyz.setObjectName("angle2xyz")
        self.angle2xyzSend = QtWidgets.QPushButton(self.centralwidget)
        self.angle2xyzSend.setGeometry(QtCore.QRect(450, 370, 81, 51))
        self.angle2xyzSend.setObjectName("angle2xyzSend")
        self.co_ordSet = QtWidgets.QLineEdit(self.centralwidget)
        self.co_ordSet.setGeometry(QtCore.QRect(10, 420, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.co_ordSet.setFont(font)
        self.co_ordSet.setAlignment(QtCore.Qt.AlignCenter)
        self.co_ordSet.setObjectName("co_ordSet")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 400, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.xyz2angle = QtWidgets.QPushButton(self.centralwidget)
        self.xyz2angle.setGeometry(QtCore.QRect(360, 430, 81, 51))
        self.xyz2angle.setObjectName("xyz2angle")
        self.xyz2angleSend = QtWidgets.QPushButton(self.centralwidget)
        self.xyz2angleSend.setGeometry(QtCore.QRect(450, 430, 81, 51))
        self.xyz2angleSend.setObjectName("xyz2angleSend")
        self.relax = QtWidgets.QPushButton(self.centralwidget)
        self.relax.setGeometry(QtCore.QRect(270, 450, 81, 31))
        self.relax.setObjectName("relax")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alex\'s Dog Position Tool"))
        self.label_2.setText(_translate("MainWindow", "Left Shoulder In/Out"))
        self.leftShoulderInOut.setText(_translate("MainWindow", "90"))
        self.label_3.setText(_translate("MainWindow", "Left Shoulder\n"
"Forward/Backward"))
        self.leftShoulderFB.setText(_translate("MainWindow", "90"))
        self.label_4.setText(_translate("MainWindow", "Left Elbow Up/Down"))
        self.leftElbowFB.setText(_translate("MainWindow", "90"))
        self.label_5.setText(_translate("MainWindow", "Left Hip\n"
"Forward/Backward"))
        self.leftKneeFB.setText(_translate("MainWindow", "90"))
        self.leftHipFB.setText(_translate("MainWindow", "90"))
        self.label_6.setText(_translate("MainWindow", "Left Knee Up/Down"))
        self.label_7.setText(_translate("MainWindow", "Left Hip In/Out"))
        self.leftHipInOut.setText(_translate("MainWindow", "90"))
        self.rightHipInOut.setText(_translate("MainWindow", "90"))
        self.rightHipFB.setText(_translate("MainWindow", "90"))
        self.label_8.setText(_translate("MainWindow", "Right Knee Up/Down"))
        self.label_9.setText(_translate("MainWindow", "Right Hip In/Out"))
        self.label_10.setText(_translate("MainWindow", "Right Hip\n"
"Forward/Backward"))
        self.rightKneeFB.setText(_translate("MainWindow", "90"))
        self.label_11.setText(_translate("MainWindow", "Right Shoulder\n"
"Forward/Backward"))
        self.rightElbowFB.setText(_translate("MainWindow", "90"))
        self.rightShoulderFB.setText(_translate("MainWindow", "90"))
        self.label_12.setText(_translate("MainWindow", "Right Elbow Up/Down"))
        self.label_13.setText(_translate("MainWindow", "Right Shoulder In/Out"))
        self.rightShoulderInOut.setText(_translate("MainWindow", "90"))
        self.angle2xyz.setText(_translate("MainWindow", "Angles to\n"
"Co-ordinates"))
        self.angle2xyzSend.setText(_translate("MainWindow", "Angles to\n"
"Co-ordinates\n"
"and Run"))
        self.co_ordSet.setText(_translate("MainWindow", "[[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]]"))
        self.label_14.setText(_translate("MainWindow", "X,Y,Z Co-ordinates"))
        self.xyz2angle.setText(_translate("MainWindow", "Co-ordinates\n"
"to Angles"))
        self.xyz2angleSend.setText(_translate("MainWindow", "Co-ordinates\n"
"to Angles\n"
"and Run"))
        self.relax.setText(_translate("MainWindow", "Relax"))
