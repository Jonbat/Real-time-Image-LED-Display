#!/usr/bin/env python3

""" IR remote set-up instructions:
1. First, run IR_Mode.py from the command line
2. Point and press two IR remote buttons: one to scroll through examples and one to
   turn off the display. IR codes will be displayed on the command line after each 
   press. Copy the codes to a text editor
3. Assign one the codes to the following scroll and off variables. IR remote set-up is
   complete!
"""

scroll = 16236607
off = 16203967

"""
Copyright 2018 Owain Martin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import RPi.GPIO as GPIO
import IRModule
import time
import os
import signal
import subprocess

state = {
    "process": None
}

demoNumber = 3

def remote_callback(code):        
    if code == scroll:
        global demoNumber
        if demoNumber >= 11:
            demoNumber = 3
        else:
            demoNumber = demoNumber + 1
        if state["process"]:
            os.killpg(os.getpgid(state["process"].pid), signal.SIGTERM)  # Send the signal to all the process groups
        state["process"] = subprocess.Popen(["sudo", "./rpi-rgb-led-matrix/examples-api-use/demo", "-D", str(demoNumber)], stdout=subprocess.PIPE, 
        shell=False, preexec_fn=os.setsid)
    elif code == off:
        os.killpg(os.getpgid(state["process"].pid), signal.SIGTERM)  # Send the signal to all the process groups
    else:
	    print(code)

    return

# set up IR pi pin and IR remote object
irPin = 8
ir = IRModule.IRRemote(callback='DECODE')
# using 'DECODE' option for callback will print out
# the IR code received in hexadecimal
# this can used to get the codes for whichever NEC
# compatable remote you are using

# set up GPIO options and set callback function required
# by the IR remote module (ir.pWidth)        
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)      # uses numbering outside circles
GPIO.setup(irPin,GPIO.IN)   # set irPin to input
GPIO.add_event_detect(irPin,GPIO.BOTH,callback=ir.pWidth)

ir.set_verbose() # verbose option prints outs high and low width durations (ms)
print('Starting IR remote sensing using DECODE function and verbose setting equal True ')
print('Use ctrl-c to exit program')

try:    
    time.sleep(5)

    # turn off verbose option and change callback function
    # to the function created above - remote_callback()
    print('Turning off verbose setting and setting up callback')
    ir.set_verbose(False)
    ir.set_callback(remote_callback)

    # This is where you could do other stuff
    # Blink a light, turn a motor, run a webserver
    # count sheep or mine bitcoin
    
    while True:
        time.sleep(1)

except:
    print('Removing callback and cleaning up GPIO')
    ir.remove_callback()
    GPIO.cleanup(irPin)
