import pyttsx3
import random
import serial
from  DIALOGUE import *

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

volume = engine.getProperty('volume')
engine.setProperty('volume',3.0)

engine.setProperty('rate', 150)

def say(line):
    engine.say(line)
    engine.runAndWait()

RUN = True
run_count = 0

Arduino = serial.Serial('COM3', 9600)

while RUN:
    if Arduino.inWaiting() > 0:
        data = Arduino.readline().decode('ascii')
        
        print(data)

        if int(data) == 0 and run_count == 0:
        
            run_count += 1
        
            for log in FIXED_DIALOGUES:
                say(log)
        
            log = random.choice(DIALOGUES)
            say(log)
        
        else:
            run_count = 0 