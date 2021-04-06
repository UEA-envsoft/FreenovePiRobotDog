import math
from Control import *
from Servo import *
class Action:
    def __init__(self):
        self.servo=Servo()
        self.control=Control()


    #NEW ACTIONS AND TRANSITION METHOD

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

    def relax(self):
        self.transition([[55, 78, 0], [55, 78, 0], [55, 78, 0], [55, 78, 0]])

    def sit(self):
        self.transition([[-37,121,0],[-11,81,0],[-11,81,0],[-37,121,0]])

    def lets_play(self):
        recallWag = self.control.tailWagging
        self.control.tailWagging = True
        # print("forelegs")
        self.transition([[102,50,0],[27,125,0],[27,125,0],[102,50,0]])
        # print("head")
        for i in range(90,160):
            self.servo.setServoAngle(15,i)
            time.sleep(0.02)
        # print("tailwag")
        for j in range(400):
            time.sleep(0.005)
        self.relax()
        # print("head straight")
        for i in range(160,90,-1):
            self.servo.setServoAngle(15,i)
            time.sleep(0.02)
        # print("sit")
        self.sit()
        # print("head up a bit")
        for i in range(90,110):
            self.servo.setServoAngle(15,i)
            time.sleep(0.02)  
        # print("final tailwag")
        for j in range (400):
            time.sleep(0.005)
        # print("relax")
        # print("head straight")
        for i in range(110,90,-1):
            self.servo.setServoAngle(15,i)
            time.sleep(0.02)
        self.relax()
        time.sleep(3)
        self.control.tailWagging = recallWag
        if not recallWag: self.control.tailReset()
        # print("end")

     #FREENOVE PREDEFINED ACTIONS

    def push_ups(self):
        xyz=[[0,50,0],[-100,23,0],[-100,23,0],[0,50,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.01)
        for i in range(4):
            for i in range(50,120,1):
                self.control.point[0][1]=i
                self.control.point[3][1]=i
                self.control.run()
                time.sleep(0.01)
            for i in range(120,50,-1):
                self.control.point[0][1]=i
                self.control.point[3][1]=i
                self.control.run()
                time.sleep(0.01)
        xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.01)
            
    def helloOne(self):  
        xyz=[[-20,120,-40],[50,105,0],[50,105,0],[0,120,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
        x3=(80-self.control.point[3][0])/30
        y3=(23-self.control.point[3][1])/30
        z3=(0-self.control.point[3][2])/30
        for j in range(30):
            self.control.point[3][0]+=x3
            self.control.point[3][1]+=y3
            self.control.point[3][2]+=z3
            self.control.run()
            time.sleep(0.01)
        for i in range(2):
            for i in range(92,120,1):
                self.servo.setServoAngle(11,i)
                time.sleep(0.01)
            for i in range(120,60,-1):
                self.servo.setServoAngle(11,i)
                time.sleep(0.01)
            for i in range(60,92,1):
                self.servo.setServoAngle(11,i)
                time.sleep(0.01)
        xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
        for i in range(90,130):
            self.servo.setServoAngle(15,i)
            time.sleep(0.02)
        for i in range(130,50,-1):
            self.servo.setServoAngle(15,i)
            time.sleep(0.02)
        for i in range(50,110):
            self.servo.setServoAngle(15,i)
            time.sleep(0.02)
            
    def helloTwo(self): 
        xyz=[[0,99,-30],[10,99,0],[10,99,0],[0,99,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)    
        x3=(80-self.control.point[3][0])/30
        y3=(23-self.control.point[3][1])/30
        z3=(0-self.control.point[3][2])/30
        for j in range(30):
            self.control.point[3][0]+=x3
            self.control.point[3][1]+=y3
            self.control.point[3][2]+=z3
            self.control.run()
            time.sleep(0.01)
            
        for i in range(2):
            for i in range(92,120,1):
                self.servo.setServoAngle(11,i)
                time.sleep(0.01)
            for i in range(120,60,-1):
                self.servo.setServoAngle(11,i)
                time.sleep(0.01)
            for i in range(60,92,1):
                self.servo.setServoAngle(11,i)
                time.sleep(0.01)
        self.control.stop()
        for i in range(10):
            self.control.setpLeft()
            
    def hand(self):
        xyz=[[-20,120,-20],[50,105,0],[50,105,0],[-20,120,20]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
        
        for i in range(3):   
            x3=(100-self.control.point[3][0])/30
            y3=(40-self.control.point[3][1])/30
            z3=(10-self.control.point[3][2])/30
            for j in range(30):
                self.control.point[3][0]+=x3
                self.control.point[3][1]+=y3
                self.control.point[3][2]+=z3
                self.control.run()
                time.sleep(0.001)
                
        
            x3=(-20-self.control.point[3][0])/30
            y3=(120-self.control.point[3][1])/30
            z3=(20-self.control.point[3][2])/30
            for j in range(30):
                self.control.point[3][0]+=x3
                self.control.point[3][1]+=y3
                self.control.point[3][2]+=z3
                self.control.run()
                time.sleep(0.001)
            
            x0=(100-self.control.point[0][0])/30
            y0=(40-self.control.point[0][1])/30
            z0=(-10-self.control.point[0][2])/30
            for j in range(30):
                self.control.point[0][0]+=x0
                self.control.point[0][1]+=y0
                self.control.point[0][2]+=z0
                self.control.run()
                time.sleep(0.001)
            x0=(-20-self.control.point[0][0])/30
            y0=(120-self.control.point[0][1])/30
            z0=(-20-self.control.point[0][2])/30
            for j in range(30):
                self.control.point[0][0]+=x0
                self.control.point[0][1]+=y0
                self.control.point[0][2]+=z0
                self.control.run()
                time.sleep(0.001)
        xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
        
    def coquettish(self):
        xyz=[[80,80,0],[-30,120,0],[-30,120,0],[80,80,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
        for j in range(10):
            xyz=[[80,80,-30],[-30,120,30],[-30,120,30],[80,80,-30]]
            for i in range(4):
                xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
                xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
                xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
            for j in range(30):
                for i in range(4):
                    self.control.point[i][0]+=xyz[i][0]
                    self.control.point[i][1]+=xyz[i][1]
                    self.control.point[i][2]+=xyz[i][2]
                self.control.run()
                time.sleep(0.02)
            
            xyz=[[80,80,30],[-30,120,-30],[-30,120,-30],[80,80,30]]
            for i in range(4):
                xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
                xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
                xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
            for j in range(30):
                for i in range(4):
                    self.control.point[i][0]+=xyz[i][0]
                    self.control.point[i][1]+=xyz[i][1]
                    self.control.point[i][2]+=xyz[i][2]
                self.control.run()
                time.sleep(0.02)
        self.relax()

    def swim(self):
        z=100*math.cos(45/180*math.pi)+23
        x=100*math.sin(45/180*math.pi)
        xyz=[[-x,0,z],[-78,0,100],[-78,0,-100],[-x,0,-z]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
        for i in range(3):
            for i in range(45,-45,-1):
                z=100*math.cos(i/180*math.pi)+23
                x=100*math.sin(i/180*math.pi)
                xyz=[[-x,0,z],[-78,0,100],[-78,0,-100],[-x,0,-z]]
                for i in range(4):
                    xyz[i][0]=(xyz[i][0]-self.control.point[i][0])
                    xyz[i][1]=(xyz[i][1]-self.control.point[i][1])
                    xyz[i][2]=(xyz[i][2]-self.control.point[i][2])
                for i in range(4):
                    self.control.point[i][0]+=xyz[i][0]
                    self.control.point[i][1]+=xyz[i][1]
                    self.control.point[i][2]+=xyz[i][2]
                self.control.run()
            for i in range(-45,45,1):
                z=100*math.cos(i/180*math.pi)+23
                x=100*math.sin(i/180*math.pi)
                xyz=[[-x,0,z],[-78,0,100],[-78,0,-100],[-x,0,-z]]
                for i in range(4):
                    xyz[i][0]=(xyz[i][0]-self.control.point[i][0])
                    xyz[i][1]=(xyz[i][1]-self.control.point[i][1])
                    xyz[i][2]=(xyz[i][2]-self.control.point[i][2])
                for i in range(4):
                    self.control.point[i][0]+=xyz[i][0]
                    self.control.point[i][1]+=xyz[i][1]
                    self.control.point[i][2]+=xyz[i][2]
                self.control.run()
        xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
        time.sleep(1)
        
    def yoga(self):
        xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
            
        y=100*math.cos(45/180*math.pi)+23
        x=100*math.sin(45/180*math.pi)
        xyz=[[-x,y,0],[0,0,123],[0,0,-123],[-x,y,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run() 
            time.sleep(0.02)
            
        for i in range(3):
            for i in range(45,-45,-1):
                y=100*math.cos(i/180*math.pi)+23
                x=100*math.sin(i/180*math.pi)
                xyz=[[-x,y,0],[0,0,123],[0,0,-123],[-x,y,0]]
                for i in range(4):
                    xyz[i][0]=(xyz[i][0]-self.control.point[i][0])
                    xyz[i][1]=(xyz[i][1]-self.control.point[i][1])
                    xyz[i][2]=(xyz[i][2]-self.control.point[i][2])
                for i in range(4):
                    self.control.point[i][0]+=xyz[i][0]
                    self.control.point[i][1]+=xyz[i][1]
                    self.control.point[i][2]+=xyz[i][2]
                self.control.run() 
            for i in range(-45,45,1):
                y=100*math.cos(i/180*math.pi)+23
                x=100*math.sin(i/180*math.pi)
                xyz=xyz=[[-x,y,0],[0,0,123],[0,0,-123],[-x,y,0]]
                for i in range(4):
                    xyz[i][0]=(xyz[i][0]-self.control.point[i][0])
                    xyz[i][1]=(xyz[i][1]-self.control.point[i][1])
                    xyz[i][2]=(xyz[i][2]-self.control.point[i][2])
                for i in range(4):
                    self.control.point[i][0]+=xyz[i][0]
                    self.control.point[i][1]+=xyz[i][1]
                    self.control.point[i][2]+=xyz[i][2]
                self.control.run() 
        xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
        time.sleep(1)
    
        
if __name__=='__main__':
    action=Action()  
    time.sleep(2) 
    while True:
        action.lets_play()
        #action.push_ups()
        #action.helloOne()
        #action.hand()
        #action.coquettish() 
        #action.swim() 
        #action.yoga() 
        #action.helloTwo()
        time.sleep(3)
        
