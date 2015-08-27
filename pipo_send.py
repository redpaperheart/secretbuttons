import OSC
import time, random
import RPi.GPIO as GPIO

button = 18

prev_input = 0
delay = 500        #how many millis between button pushes

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

client = OSC.OSCClient()
client.connect( ('10.0.1.119', 8005) )    # note that the argument is a tupple and not two arguments
msg = OSC.OSCMessage() 
msg.setAddress("/button")

def millis():
    return time.time()*1000

timestop = millis()

print("waiting for button push")

while True:
    input = GPIO.input(button)
    if((millis() - timestop) > delay):
        prev_input = 0
    if ((not prev_input) and input):
            print("pressed!")
            msg.append(1)
            client.send(msg)
            prev_input = input
            time.sleep(0.05)
            timestop = millis()
#Calls the "quit_callback function in the receiver, not needed yet
#msg.setAddress("/quit")
#client.send(msg)
