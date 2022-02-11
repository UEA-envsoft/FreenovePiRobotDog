# FreenovePiRobotDog
Useful files for the Freenove Robot Dog for Raspberry Pi   

<hr />
<h3>Leg position tool</h3>
  <pre>
AlexDogPos.py                 a tool for converting leg angles to the freenove co-ordinate system  
AlexsDogPosToolui.py  and  
AlexsDogPosToolui.ui          Qt design files for above  
spike_legs3.png               the image in the GUI   
    </pre>
Place AlexDogPos.py, AlexsDogPosToolui.py and spike_legs3.png in Server directory and run AlexDogPos.py  
  
<hr />
<h3>STL files</h3>
  <pre>
rear board.STL              STL file of rear board courtesy of Freenove  
tail-servo-mount-mg90s.stl  STL file for tail servo mount courtesy of Simon Khoury   
SpikeHead.stl               STL file for an alternative head
</pre>  
<hr />
   
<h3>Local wireless keyboard and wagging tail  </h3>
Copy lclkbd.py control.py and actions.py to Server directory  
Connect wireless keyboard and run lclkbd.py  
NOTE: THERE IS NO TIME OUT ON THE SERVOS UNLIKE RUNNING THE SERVER  
you may need to adjust the value for self.TailCorrection in control.py to make your dog's tail start straight  
  
Commands (easy enough to remap to suit your own keyboard)  
HEAD  
A or mouse down: move head down  
Q or mouse up: move head up  
MOVEMENT  
Up Arrow: forward  
Down Arrow: backward  
Left Arrow: turn left  
Right Arrow: turn right  
Z: crab left  
X: crab right  
T: tail wagging on/off  
W: woof (beep)  
ACTIONS  
freenove predefined actions  
1: push_ups   
2: helloOne   
3: hand  
4: coquettish  
5: swim  
6: yoga  
7: helloTwo  
actions I have defined  
P: lets_play  
R: relax  
S: sit  
PROG FUNCTIONS  
Win/cmd: close program (3 beeps)  
END: shutdown_pi (1 beep)  
PrtScn/SysRq: reboot_pi(2 beeps)  
