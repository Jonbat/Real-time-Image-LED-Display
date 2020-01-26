import RPi.GPIO as GPIO
import time
import os
import signal
import subprocess
import time

state = {
    "process": None
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)
processRunning = False

# handle the button event
def buttonEventHandler (pin):
    print("handling button event")
    global processRunning

    time.sleep(0.1)
    if GPIO.input(25) == False and processRunning == False:
        state["process"] = subprocess.Popen(["sudo", "./rpi-rgb-led-matrix/examples-api-use/demo", "-D", "6"], stdout=subprocess.PIPE, 
            shell=False, preexec_fn=os.setsid)
        processRunning = True   
    elif GPIO.input(25) == True and processRunning == True:
        os.killpg(os.getpgid(state["process"].pid), signal.SIGTERM)  # Send the signal to all the process groups
        processRunning = False


GPIO.add_event_detect(25,GPIO.RISING)
GPIO.add_event_callback(25,buttonEventHandler)

while True:
    pass
# while True:
#     if GPIO.input(25) != previousLightState and state["process"]:
#         os.killpg(os.getpgid(state["process"].pid), signal.SIGTERM)  # Send the signal to all the process groups
#         previousLightState = GPIO.input(25)
#     elif GPIO.input(25) != previousLightState:
#         state["process"] = subprocess.Popen(["sudo", "./rpi-rgb-led-matrix/examples-api-use/demo", "-D", "6"], stdout=subprocess.PIPE, 
#             shell=False, preexec_fn=os.setsid)
#         previousLightState = GPIO.input(25)
