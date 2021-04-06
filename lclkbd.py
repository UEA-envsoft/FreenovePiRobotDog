from Action import *
import evdev
from Buzzer import *
from subprocess import call
import atexit
from Led import *
import time
import sys
from selectors import DefaultSelector, EVENT_READ
import threading

class localKeyboard:
    def __init__(self):
        self.headUpDownAngle = 90
        self.action = Action()
        self.bark = Buzzer()
        self.led = Led()
        self.led.colorWipe(self.led.strip, Color(0, 0, 0))  # turn off leds

        self.selector = DefaultSelector()
        self.mouse = evdev.InputDevice('/dev/input/event1')
        self.keybd = evdev.InputDevice('/dev/input/event0')
        self.readingKeys = False
        atexit.register(self.keybd.ungrab)  # Don't forget to ungrab the keyboard on exit!
        atexit.register(self.mouse.ungrab)
        self.keybd.grab()  # Grab, i.e. prevent the keyboard from emitting original events.#
        self.mouse.grab()
        # This works because InputDevice has a `fileno()` method.
        self.selector.register(self.mouse, EVENT_READ)
        self.selector.register(self.keybd, EVENT_READ)




    def read_keys_loop(self):
        self.readingKeys = True
        #signal ready
        self.woof()
        while self.readingKeys:
            self.read_keys()

    def read_keys(self):
        for key, mask in self.selector.select():
            device = key.fileobj
            for event in device.read():
                if event.type == evdev.ecodes.EV_KEY:
                    print("event val: " + str(event.value))
                    # print(evdev.ecodes.bytype[evdev.ecodes.EV_KEY][event.code])
                    self.key_press(event, self.keybd)
                elif event.type == evdev.ecodes.EV_REL:
                    if event.code == evdev.ecodes.REL_Y:
                        if event.value < 0:
                            self.head_down()
                        else:
                            self.head_up()
                else:
                    pass
                    # print(event)

    def key_press(self, ev, kbd):
        # EVENTS CALLED ON PRESS AND ON HOLD
        if ev.value == 1 or ev.value == 2:
            # HEAD POSITION
            if ev.code == evdev.ecodes.KEY_A: self.head_down()
            elif ev.code == evdev.ecodes.KEY_Q: self.head_up()
            # MOVEMENT
            elif ev.code == evdev.ecodes.KEY_UP: self.action.control.forWard()
            elif ev.code == evdev.ecodes.KEY_DOWN: self.action.control.backWard()
            elif ev.code == evdev.ecodes.KEY_LEFT: self.action.control.turnLeft()
            elif ev.code == evdev.ecodes.KEY_RIGHT: self.action.control.turnRight()
            elif ev.code == evdev.ecodes.KEY_Z: self.action.control.setpLeft()
            elif ev.code == evdev.ecodes.KEY_X: self.action.control.setpRight()
            # Bark
            elif ev.code == evdev.ecodes.KEY_W: self.woof()
            # not interested in any other held keys
            elif ev.value == 2: pass

            #EVENTS THAT SHOULD ONLY BE CALLED ON PRESS AND NOT HOLD
            # freenove predefined actions
            elif ev.code == evdev.ecodes.KEY_1:
                self.action.control.stop()
                self.action.push_ups()
            elif ev.code == evdev.ecodes.KEY_2:
                self.action.control.stop()
                self.action.helloOne()
            elif ev.code == evdev.ecodes.KEY_3:
                self.action.control.stop()
                self.action.hand()
            elif ev.code == evdev.ecodes.KEY_4:
                self.action.control.stop()
                self.action.coquettish()
            elif ev.code == evdev.ecodes.KEY_5:
                self.action.control.stop()
                self.action.swim()
            elif ev.code == evdev.ecodes.KEY_6:
                self.action.control.stop()
                self.action.yoga()
            elif ev.code == evdev.ecodes.KEY_7:
                self.action.control.stop()
                self.action.helloTwo()
            # actions below are ones I have defined
            elif ev.code == evdev.ecodes.KEY_P:
                self.action.control.stop()
                self.action.lets_play()
            elif ev.code == evdev.ecodes.KEY_R:
                self.action.control.stop()
                self.action.relax()
            elif ev.code == evdev.ecodes.KEY_W:
                self.woof()
            elif ev.code == evdev.ecodes.KEY_T:
                self.action.control.tailWagging = not self.action.control.tailWagging
                if self.action.control.tailWagging:
                    thread_TailWag = threading.Thread(target=self.action.control.tailThread)
                    thread_TailWag.start()
                else:
                    self.action.control.tailReset()
            elif ev.code == evdev.ecodes.KEY_S:
                self.action.control.stop()
                self.action.sit()

            # PROG FUNCTIONS
            elif ev.code == evdev.ecodes.KEY_LEFTMETA: self.close()
            elif ev.code == evdev.ecodes.KEY_END: self.shutdown_pi()
            elif ev.code == evdev.ecodes.KEY_SYSRQ: self.reboot_pi()

            else:
                print("UNUSED KEY CODE")
                print(evdev.ecodes.bytype[evdev.ecodes.EV_KEY][ev.code])
        # flush backed up key presses
        while kbd.read_one() != None:
            pass

    def head_up(self):
        self.headUpDownAngle += 1
        if self.headUpDownAngle > 180: self.headUpDownAngle = 180
        self.action.control.servo.setServoAngle(15, self.headUpDownAngle)
        # print("Up/down " + str(self.headUpDownAngle))

    def head_down(self):
        self.headUpDownAngle -= 1
        if self.headUpDownAngle < 80: self.headUpDownAngle = 80
        self.action.control.servo.setServoAngle(15, self.headUpDownAngle)
        # print("Up/down " + str(self.headUpDownAngle))

    def close(self):
        self.action.control.tailWagging = False
        self.action.control.tailReset()
        self.woof()
        time.sleep(0.2)
        self.woof()
        time.sleep(0.2)
        self.woof()
        self.readingKeys = False
        self.selector.unregister(self.mouse)
        self.selector.unregister(self.keybd)
        self.led.colorWipe(self.led.strip, Color(0,0,0),0)
        # kbd should be ungrabbed by atexit
        # but belt and braces
        try:
            self.keybd.ungrab
            self.mouse.ungrab
        except:
            pass
        sys.exit()

    def shutdown_pi(self):
        self.woof()
        time.sleep(0.2)
        self.woof()
        call("sudo nohup shutdown -h now", shell=True)

    def reboot_pi(self):
        self.woof()
        call("sudo nohup reboot", shell=True)

    def woof(self):
        self.bark.run('1')
        time.sleep(0.2)
        self.bark.run('0')


if __name__ == '__main__':
    kb = localKeyboard()
    try:
        kb.read_keys_loop()
    except KeyboardInterrupt:
        print("calling close")
        kb.close()