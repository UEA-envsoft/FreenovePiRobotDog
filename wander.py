import time
from lclkbd import *
from Ultrasonic import *


class wander:
    def __init__(self, kb):
        self.kb = kb
        self.kb.reset_head()
        self.kb.action.control.speed = 8
        self.ultrasonic = Ultrasonic()

    def go(self):
        try:
            #print("Try")
            f = self.ultrasonic.getDistance()
            print("f",f)
            l = 0
            r = 0
            #edgeDanger = 40
            aheadClear = 50
            obstDanger = 35
            #criticalEdge = 15

            #make some decisions
            #way ahead blocked

            if (f < obstDanger):
                print("Blocked")
                # backup
                self.kb.action.control.backWard()
                # look left
                self.kb.action.control.turnLeft()
                self.kb.action.control.turnLeft()
                l = self.ultrasonic.getDistance()
                print("l",l)
                if (l > aheadClear):
                    self.kb.action.control.forWard()
                else:
                    #look right
                    self.kb.action.control.turnRight()
                    self.kb.action.control.turnRight()
                    self.kb.action.control.turnRight()
                    self.kb.action.control.turnRight()
                    r = self.ultrasonic.getDistance()
                    print("r",r)
                    if (r > aheadClear):
                        self.kb.action.control.forWard()
                    else:
                        #go back to faccing forward
                        self.kb.action.control.turnLeft()
                        self.kb.action.control.turnLeft()
                        #back up a bit more
                        self.kb.action.control.backWard()
                        if (r > l):
                            self.kb.action.control.turnRight()
                            self.kb.action.control.turnRight()
                            r = self.ultrasonic.getDistance()
                            print("r2",r)
                            if (r > aheadClear):
                                self.kb.action.control.forWard()
                        else:
                            # look left
                            self.kb.action.control.turnLeft()
                            self.kb.action.control.turnLeft()
                            l = self.ultrasonic.getDistance()
                            print("l2",l)
                            if (l > aheadClear):
                                self.kb.action.control.forWard()
            else:
                print("forward")
                self.kb.action.control.forWard()
        except:
            e = sys.exc_info()[0]
            print("Except: %s" % e)
            pass
