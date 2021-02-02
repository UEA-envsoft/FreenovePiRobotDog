from AlexsDogPosToolui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Control import *
from Servo import *

class mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
            super(mywindow,self).__init__()
            self.setupUi(self)
            self.control = Control()
            self.servo = Servo()
            self.co_ordsStr = "[[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]]"
            self.co_ords = [[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]]
            self.angles = [[90, 90, 90], [90, 90, 90], [90, 90, 90], [90, 90, 90]]
            self.xyz2angle.clicked.connect(self.coord2angle)
            self.angle2xyz.clicked.connect(self.angle2coord)
            self.xyz2angleSend.clicked.connect(self.coord2angleAndRun)
            self.angle2xyzSend.clicked.connect(self.angle2coordAndRun)
            self.relax.clicked.connect(self.relaxPos)
            self.calAngles = self.control.calibration_angle

    def relaxPos(self):
        self.co_ordsStr = "[[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]]"
        self.co_ords = [[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]]
        self.co_ordSet.setText(self.co_ordsStr)
        self.coord2angle()
        self.setTheServos()

    def coord2angle(self):
        # "[[-100,-100,-100],[-100,-100,-100],[-100,-100,-100],[-100,-100,-100]]"
        coord = self.co_ordSet.text()
        #lose any white space
        coord = coord.replace(" ", "")
        coord = coord.replace("],[", ":")
        coord = coord.replace("]]", "")
        coord = coord.replace("[[", "")
        # "-100,-100,-100:-100,-100,-100:-100,-100,-100:-100,-100,-100"
        xyzs = coord.split(":")
        for i in range(4):
            self.co_ords[i] = xyzs[i].split(",")
            self.angles[i][0], self.angles[i][1], self.angles[i][2] = self.control.coordinateToAngle(int(self.co_ords[i][0]),int(self.co_ords[i][1]),int(self.co_ords[i][2]))
        self.leftShoulderInOut.setText(str(int(self.angles[0][0])))
        self.leftShoulderFB.setText(str(90 - int(self.angles[0][1])))
        self.leftElbowFB.setText(str(int(self.angles[0][2])))
        self.leftHipInOut.setText(str(int(self.angles[1][0])))
        self.leftHipFB.setText(str(90 - int(self.angles[1][1])))
        self.leftKneeFB.setText(str(int(self.angles[1][2])))
        self.rightHipInOut.setText(str(int(self.angles[2][0])))
        self.rightHipFB.setText(str(90 + int(self.angles[2][1])))
        self.rightKneeFB.setText(str(180 - int(self.angles[2][2])))
        self.rightShoulderInOut.setText(str(int(self.angles[3][0])))
        self.rightShoulderFB.setText(str(90 + int(self.angles[3][1])))
        self.rightElbowFB.setText(str(180 - int(self.angles[3][2])))

    def angle2coord(self):
        self.angles[0][0] = int(self.leftShoulderInOut.text())
        self.angles[0][1] = 90 - int(self.leftShoulderFB.text())
        self.angles[0][2] = int(self.leftElbowFB.text())
        self.angles[1][0] = int(self.leftHipInOut.text())
        self.angles[1][1] = 90 - int(self.leftHipFB.text())
        self.angles[1][2] = int(self.leftKneeFB.text())
        self.angles[2][0] = int(self.rightHipInOut.text())
        self.angles[2][1] = int(self.rightHipFB.text()) - 90
        self.angles[2][2] = 180 - int(self.rightKneeFB.text())
        self.angles[3][0] = int(self.rightShoulderInOut.text())
        self.angles[3][1] = int(self.rightShoulderFB.text()) - 90
        self.angles[3][2] = 180 - int(self.rightElbowFB.text())
        self.co_ordsStr = "[["
        for i in range(4):
            self.co_ords[i][0], self.co_ords[i][1], self.co_ords[i][2] = self.control.angleToCoordinate(self.angles[i][0], self.angles[i][1], self.angles[i][2])
            self.co_ordsStr = self.co_ordsStr + str(int(self.co_ords[i][0])) + "," + str(int(self.co_ords[i][1])) + "," + str(int(self.co_ords[i][2]))
            if i < 3:
                self.co_ordsStr = self.co_ordsStr + "],["
            else:
                self.co_ordsStr = self.co_ordsStr + "]]"
        self.co_ordSet.setText(self.co_ordsStr)

    def coord2angleAndRun(self):
        self.coord2angle()
        self.setTheServos()

    def angle2coordAndRun(self):
        self.angle2coord()
        self.setTheServos()

    def setTheServos(self):
        for i in range(2):  # these 4 sets of 3 angles (ie 12 angles) are now applied to the 12 leg servos
            print ("setting " + str(4+i*3) + " to " + str(self.angles[i][0]))
            self.servo.setServoAngle(4 + i * 3, self.angles[i][0] + self.calAngles[i][0])  # 4   7   Left shoulder   LReft Hip In/Out    servo 4 gets angle [0][0]    servo 7  gets [1][0]
            print("setting " + str(3 + i * 3) + " to " + str(self.angles[i][1]))
            self.servo.setServoAngle(3 + i * 3, 90 - (self.angles[i][1] + self.calAngles[i][1]))  # 3   6   Left shoulder   Left Hip  for/back       [0][1]    [1][1]
            print("setting " + str(2 + i * 3) + " to " + str(self.angles[i][2]))
            self.servo.setServoAngle(2 + i * 3, self.angles[i][2] + self.calAngles[i][2])  # 2   5  Left elbow     left knee   [0][2]    [1][2]
            print("setting " + str(8 + i * 3) + " to " + str(self.angles[i+2][0]))
            self.servo.setServoAngle(8 + i * 3, self.angles[i + 2][0] + self.calAngles[i+2][0])  # 8  11   right shoulder  right hip  in/out     [2][0]    [3][0]
            print("setting " + str(9 + i * 3) + " to " + str(self.angles[i+2][1]))
            self.servo.setServoAngle(9 + i * 3, 90 + self.angles[i + 2][1] + self.calAngles[i+2][1])  # 9  12  right shoulder  right hip  for/back     [2][1]    [3][1]
            print("setting " + str(10 + i * 3) + " to " + str(self.angles[i+2][2]))
            self.servo.setServoAngle(10 + i * 3, 180 - (self.angles[i + 2][2] + self.calAngles[i+2][2]))  # 10  13   right elbow    right knee     [2][2]    [3][2]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow=mywindow()
    myshow.show();
    sys.exit(app.exec_())
