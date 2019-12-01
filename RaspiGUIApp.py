## Buttons to rool my Car model ##

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
led=LED(6)
back=LED(13)
left=LED(19)
right=LED(26)

### GUI DEFINITIONS ###
win = Tk()
win.title("CAR")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


### Event Functions ###
def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"]="Turn LED on" # Change only the button text property
    else:
        led.on()
        ledButton["text"]="Turn LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

def backToggle():
    if back.is_lit:
        back.off()
        backButton["text"]="back on" # Change only the button text property
    else:
        back.on()
        backButton["text"]="back off"
def leftToggle():
    if left.is_lit:
        left.off()
        leftButton["text"]="left on" # Change only the button text property
    else:
        left.on()
        leftButton["text"]="left off"
def rightToggle():
    if right.is_lit:
        right.off()
        rightButton["text"]="right on" # Change only the button text property
    else:
        right.on()
        rightButton["text"]="right off"
### WIDGETS ###

# Button, triggers the connected command when it is pressed
ledButton = Button(win, text='forward on', font=myFont, command=ledToggle, bg='bisque2', height=1, width=24)
ledButton.grid(row=0,column=2)

backButton = Button(win, text='back on', font=myFont, command=backToggle, bg='bisque2', height=1, width=24)
backButton.grid(row=2,column=2)

leftButton = Button(win, text='left on', font=myFont, command=leftToggle, bg='bisque2', height=1, width=24)
leftButton.grid(row=2,column=1)

rightButton = Button(win, text='right on', font=myFont, command=rightToggle, bg='bisque2', height=1, width=24)
rightButton.grid(row=2,column=3)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
exitButton.grid(row=3, column=2)

win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window
