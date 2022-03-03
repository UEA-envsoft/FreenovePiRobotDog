from AlexsDogPosToolui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Control import *
from Servo import *


class mywindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.control = Control()
        self.servo = Servo()
        self.co_ordsStr = "[[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]]"
        self.co_ords = [[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]]
        self.servoAngles = [[90, 90, 90], [90, 90, 90], [90, 90, 90], [90, 90, 90]] 
        self.calculatedAngles = [[90, 0, 90], [90, 0, 90], [90, 0, 90], [90, 0, 90]]
        self.xyz2angle.clicked.connect(self.coord2angle)
        self.angle2xyz.clicked.connect(self.angle2coord)
        self.xyz2angleSend.clicked.connect(self.coord2angleAndRun)
        self.angle2xyzSend.clicked.connect(self.angle2coordAndRun)
        self.relax.clicked.connect(self.relaxPos)
        self.calibAngles = self.control.calibration_angle
        
        self.btnCopyCoords1.clicked.connect(self.copyCoords1)
        self.btnCopyCoords2.clicked.connect(self.copyCoords2)
        self.btnCopyCoords3.clicked.connect(self.copyCoords3)
        self.btnCopyCoords4.clicked.connect(self.copyCoords4)
        self.btnTransitionTo1.clicked.connect(self.transitionTo1)
        self.btnTransitionTo2.clicked.connect(self.transitionTo2)
        self.btnTransitionTo3.clicked.connect(self.transitionTo3)
        self.btnTransitionTo4.clicked.connect(self.transitionTo4)
        

    # to move from current position to desired position
    # targetPosition - the new desired position  default = relax
    # steps - the number of intermeidate positions to get from current to desired position
    #                                            default is 30
    # sleep - the pause between each stage       default is 0.01
    def transition(self,targetPosition=[[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]],steps=30,sleep=0.01):

        xyz = targetPosition
        for i in range(4):   #For each limb, calculate the incremental change in X Y Z for each step
            xyz[i][0] = (xyz[i][0] - self.control.point[i][0]) / steps
            xyz[i][1] = (xyz[i][1] - self.control.point[i][1]) / steps
            xyz[i][2] = (xyz[i][2] - self.control.point[i][2]) / steps

        # print("Fractional steps: " + str(xyz))
        for j in range(steps):   # For each step ....
            for i in range(4):   # Tell control class about the new position of each limb
                self.control.point[i][0] += xyz[i][0]
                self.control.point[i][1] += xyz[i][1]
                self.control.point[i][2] += xyz[i][2]
            # print("new self.control.point: " + str(self.control.point))
            self.control.run()    # move limbs to new position
            time.sleep(sleep)

    def relaxPos(self):
        self.co_ordsStr = "[[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]]"
        self.co_ords = [[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]]
        self.co_ordSet.setText(self.co_ordsStr)
        self.coord2angle()
        self.setTheServos()
    
    def coord2angle(self):
        # "[[-100,-100,-100],[-100,-100,-100],[-100,-100,-100],[-100,-100,-100]]"
        coord = self.co_ordSet.text()
        # lose any white space
        coord = coord.replace(" ", "")
        coord = coord.replace("],[", ":")
        coord = coord.replace("]]", "")
        coord = coord.replace("[[", "")
        # "-100,-100,-100:-100,-100,-100:-100,-100,-100:-100,-100,-100"
        xyzs = coord.split(":")
        for i in range(2):
            # for 0 and 1
            self.co_ords[i] = xyzs[i].split(",")
            self.calculatedAngles[i][0], self.calculatedAngles[i][1], self.calculatedAngles[i][2] = self.control.coordinateToAngle(int(float(self.co_ords[i][0])), int(float(self.co_ords[i][1])),int(float(self.co_ords[i][2])))
            self.servoAngles[i][0] = self.calculatedAngles[i][0]
            self.servoAngles[i][1] = 90 - self.calculatedAngles[i][1]
            self.servoAngles[i][2] = self.calculatedAngles[i][2]
            # for 2 and 3
            self.co_ords[i + 2] = xyzs[i + 2].split(",")
            self.calculatedAngles[i + 2][0], self.calculatedAngles[i + 2][1], self.calculatedAngles[i + 2][2] = self.control.coordinateToAngle(int(float(self.co_ords[i + 2][0])), int(float(self.co_ords[i + 2][1])),int(float(self.co_ords[i + 2][2])))
            self.servoAngles[i + 2][0] = self.calculatedAngles[i + 2][0]
            self.servoAngles[i + 2][1] = 90 + self.calculatedAngles[i + 2][1]
            self.servoAngles[i + 2][2] = 180 - self.calculatedAngles[i + 2][2]

        self.leftShoulderInOut.setText(str(int(self.servoAngles[0][0])))
        self.leftShoulderFB.setText(str(int(self.servoAngles[0][1])))
        self.leftElbowFB.setText(str(int(self.servoAngles[0][2])))
        self.leftHipInOut.setText(str(int(self.servoAngles[1][0])))
        self.leftHipFB.setText(str(int(self.servoAngles[1][1])))
        self.leftKneeFB.setText(str(int(self.servoAngles[1][2])))
        self.rightHipInOut.setText(str(int(self.servoAngles[2][0])))
        self.rightHipFB.setText(str(int(self.servoAngles[2][1])))
        self.rightKneeFB.setText(str(int(self.servoAngles[2][2])))
        self.rightShoulderInOut.setText(str(int(self.servoAngles[3][0])))
        self.rightShoulderFB.setText(str(int(self.servoAngles[3][1])))
        self.rightElbowFB.setText(str(int(self.servoAngles[3][2])))

    def angle2coord(self):
        self.servoAngles[0][0] = int(self.leftShoulderInOut.text())
        self.servoAngles[0][1] = int(self.leftShoulderFB.text())
        self.servoAngles[0][2] = int(self.leftElbowFB.text())
        self.servoAngles[1][0] = int(self.leftHipInOut.text())
        self.servoAngles[1][1] = int(self.leftHipFB.text())
        self.servoAngles[1][2] = int(self.leftKneeFB.text())
        self.servoAngles[2][0] = int(self.rightHipInOut.text())
        self.servoAngles[2][1] = int(self.rightHipFB.text())
        self.servoAngles[2][2] = int(self.rightKneeFB.text())
        self.servoAngles[3][0] = int(self.rightShoulderInOut.text())
        self.servoAngles[3][1] = int(self.rightShoulderFB.text())
        self.servoAngles[3][2] = int(self.rightElbowFB.text())

        for i in range(2):
            # for 0 and 1
            self.calculatedAngles[i][0] = self.servoAngles[i][0]
            self.calculatedAngles[i][1] = 90 - self.servoAngles[i][1]
            self.calculatedAngles[i][2] = self.servoAngles[i][2]
            # for 2 and 3
            self.calculatedAngles[i + 2][0] = self.servoAngles[i + 2][0]
            self.calculatedAngles[i + 2][1] = self.servoAngles[i + 2][1] - 90
            self.calculatedAngles[i + 2][2] = 180 - self.servoAngles[i + 2][2]

        self.co_ordsStr = "[["
        for i in range(4):
            self.co_ords[i][0], self.co_ords[i][1], self.co_ords[i][2] = self.control.angleToCoordinate(self.calculatedAngles[i][0], self.calculatedAngles[i][1], self.calculatedAngles[i][2])
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
        self.transition(self.coordStrToCoordIntArray(self.co_ordSet.text()))
        """
        for i in range(2):
            self.servo.setServoAngle(4 + i * 3, self.servoAngles[i][0] + self.calibAngles[i][0])          # 4   7   Left shoulder   Left Hip In/Out  servo 4 gets angle [0][0] servo 7  gets [1][0]
            self.servo.setServoAngle(3 + i * 3, self.servoAngles[i][1] - self.calibAngles[i][1])          # 3   6   Left shoulder   Left Hip  for/back   [0][1]    [1][1]
            self.servo.setServoAngle(2 + i * 3, self.servoAngles[i][2] + self.calibAngles[i][2])          # 2   5   Left elbow       left knee            [0][2]    [1][2]
            self.servo.setServoAngle(8 + i * 3, self.servoAngles[i + 2][0] + self.calibAngles[i + 2][0])  # 8  11   right shoulder  right hip  in/out    [2][0]    [3][0]
            self.servo.setServoAngle(9 + i * 3, self.servoAngles[i + 2][1] + self.calibAngles[i + 2][1])  # 9  12   right shoulder   right hip  for/back  [2][1]    [3][1]
            self.servo.setServoAngle(10 + i * 3, self.servoAngles[i + 2][2] - self.calibAngles[i + 2][2]) # 10  13   right elbow    right knee           [2][2]    [3][2]
        """
        
    def coordStrToCoordIntArray(self, coord):
        # lose any white space
        coord = coord.replace(" ", "")
        coord = coord.replace("],[", ":")
        coord = coord.replace("]]", "")
        coord = coord.replace("[[", "")
        xyzs = coord.split(":")
        coordIntArray = [[],[],[],[]]
        for i in range(4):
            xyz = xyzs[i].split(",")
            coordIntArray[i] = [int(float(xyz[0])),int(float(xyz[1])),int(float(xyz[2]))]
        return coordIntArray

    def copyCoords1(self):
        coord = self.co_ordSet.text()
        # lose any white space
        coord = coord.replace(" ", "")
        self.position1coords.setText(coord)

    def copyCoords2(self):
        coord = self.co_ordSet.text()
        # lose any white space
        coord = coord.replace(" ", "")
        self.position2coords.setText(coord)

    def copyCoords3(self):
        coord = self.co_ordSet.text()
        # lose any white space
        coord = coord.replace(" ", "")
        self.position3coords.setText(coord)

    def copyCoords4(self):
        coord = self.co_ordSet.text()
        # lose any white space
        coord = coord.replace(" ", "")
        self.position4coords.setText(coord)

    def transitionTo1(self):
        if self.position1coords.text() != "":
            self.transition(self.coordStrToCoordIntArray(self.position1coords.text()))

    def transitionTo2(self):
        if self.position2coords.text() != "":
            self.transition(self.coordStrToCoordIntArray(self.position2coords.text()))

    def transitionTo3(self):
        if self.position3coords.text() != "":
            self.transition(self.coordStrToCoordIntArray(self.position3coords.text()))

    def transitionTo4(self):
        if self.position4coords.text() != "":
            self.transition(self.coordStrToCoordIntArray(self.position4coords.text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = mywindow()
    myshow.show();
    sys.exit(app.exec_())
