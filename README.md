# FreenovePiRobotDog
Useful files for the Freenove Robot Dog for Raspberry Pi   

<hr />
<h2>Leg position tool</h2>
  <pre>
AlexDogPos.py                 a tool for converting leg angles to the freenove co-ordinate system  
                              It can store four positions and transition smoothly between them.  
AlexsDogPosToolui.py  and  
AlexsDogPosToolui.ui          Qt design files for above  
spike_legs3.png               the image in the GUI   
    </pre>
Place AlexDogPos.py, AlexsDogPosToolui.py and spike_legs3.png in Server directory
To run it type: <pre>python AlexDogPos.py</pre> 
  
<hr />
<h2>STL files</h2>
  <pre>
rear board.STL              STL file of rear board courtesy of Freenove  
tail-servo-mount-mg90s.stl  STL file for tail servo mount courtesy of Simon Khoury   
SpikeHead.stl               STL file for an alternative head
</pre>  
<h3>STL files for Cat head and tail courtesy of Thomas Jaeger</h3>
<pre>
cat v6.stl                 STL file for cat head
Körper1.stl                STL file for head mounting
PiCamAngle.STL
tail.stl                   STL file for cat tail
</pre>
<hr />
   
<h2>Local wireless keyboard, wagging tail and very crude autonomous movement </h2>

The code has a dependancy for evdev (https://python-evdev.readthedocs.io/en/latest/): 

<ul>sudo pip3 install evdev</ul>

This code was written for the "Rii i8S Mini Keyboard" available from Amazon

evdev sees this keyboard as 4 separate devices: a keyboard, a mouse, a consumer control and a system control

If you wish to use this code with other controllers or keyboards you may well have to comment out some of the devices and remap some of the keyboard associations

Drop the following 4 files into the Server directory on the Pi. You may want to backup your copies of Action.py and Control.py first!

<pre>
lclkbd.py          the keyboard reading routine - this is the one you run: sudo python lclkbd.py
Control.py         modified version of the freenove file to wagging tail
Action.py          additional actions
wander.py          a quick stab at autonomous movement code - needs quite a bit of tinkering
                   try adjusting these values
                      aheadClear = 50
                      obstDanger = 35
</pre>
<h3>Keyboard commands</h3>
<pre>
HEAD
A or mouse down  Head down
Q or mouse up    Head up
<br />
MOVEMENT
Up arrow        Move forward
Down arrow      Move backward
Left arrow      Turn left
Right arrow     Turn right
Z               Sideways left
X               Sideways right
Volume up       Increase height
Volume down     Decrease height
<br />
Tab             Start/Stop autonomous movement
 
T              tail wagging on/off
W              woof (beep)
R              Relax
 
1 to 0         Speed
 
ACTIONS
F1             push_ups
F2             helloOne
F3             hand
F4             coquettish
F5             swim
F6             yoga
F7             helloTwo
actions I have defined
P             lets_play
S             sit
 
PROG FUNCTIONS
Win/cmd       close program (3 beeps)
END           shutdown_pi (1 beep)
PrtScn/SysRq  reboot_pi(2 beeps)
</pre>
