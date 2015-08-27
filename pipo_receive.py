#import system libraries
import RPi.GPIO as GPIO
from OSC import OSCServer
import time
import sys
import random
import pygame
import json
import os
import datetime

pipolauncher = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pipolauncher, GPIO.OUT)

server = OSCServer( ("10.0.1.205", 8005) )
server.timeout = 0
run = True

jsonPath = '/home/pi/pipo/data/info.json'

x = 0
l = 0
s = 0 

pygame.init()
pygame.mixer.init(frequency=22050, size=16, channels=2, buffer=128)
pygame.mixer.music.load("/home/pi/pipo/data/explosion.mp3")

print("waiting!")


with open (jsonPath) as data_file: 
    info = json.load(data_file)
    x = int(info["NumberOfHits"])   
    l = info["TimeOfLastHit"]
    s = info["StartDate"]

def handle_timeout(self):
    self.timed_out = True

def user_callback(path, tags, args, source):
    jsonPrep()
    GPIO.output(pipolauncher, GPIO.HIGH)
    pygame.mixer.music.play()
    time.sleep(1)
    GPIO.output(pipolauncher, GPIO.LOW)
    print("launched!")
    jsonUpdate()    

def quit_callback(path, tags, args, source):
    # don't do this at home (or it'll quit blender)
    global run
    run = False

server.addMsgHandler( "button", user_callback )

#JSON stuff
def jsonPrep():
    global l
    l = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    global x
    x = x + 1
    info["NumberOfHits"] = str(x)
    info["TimeOfLastHit"] = str(l)
    info["StartDate"] = s

def jsonUpdate():
    with open(jsonPath, "w") as jsonFile:
        json.dump(info, jsonFile)
        print("Saved Json file")

# user script that's called by the game engine every frame
def loop():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()

try:
	while True:
		loop()

finally:
	GPIO.cleanup()
	server.close()
