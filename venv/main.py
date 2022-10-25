import tkinter as tk
from tkinter import *
#from Macros import drunkenSailor
import threading

import keyboard;
import time;
import random;
import mouse;

#creating the window
window = tk.Tk()
window.geometry("500x500")
window.title("Destiny Master Grind")



#Selection checkboxes
drunkenBool = tk.BooleanVar()
drunkenCheck = tk.Checkbutton(window, text = "Drunken Sailor", variable=drunkenBool, onvalue = True )
drunkenCheck.grid(row = 0, column = 0,)


#create macros
def drunkenSailor(event):
    while(1):
        timer = random.uniform(.1, 2)
        stop = time.time() + timer
        wasdList = ["w", "a", "s", "d" ]
        selectedInput = random.choice(wasdList)
        print(selectedInput)
        while(time.time() < stop):
            keyboard.press(selectedInput)
            time.sleep(.1)
        print("stopping")
        keyboard.release(selectedInput)
        if event.isSet():
            print("Drunken Thread Killed")
            break


drukenEvent = threading.Event()
drunkenThread = threading.Thread(target=drunkenSailor, args=(drukenEvent,))
drunkenThread.daemon = True


#Apply Selection Button
def applyButtonAction():
    if(drunkenBool.get()):
        drunkenThread.start()
    else:
        drukenEvent.set()


applyButton = tk.Button(window, text="Apply", command= lambda : applyButtonAction())
applyButton.grid(row=2, column=2)

#Making the program run
window.mainloop()

