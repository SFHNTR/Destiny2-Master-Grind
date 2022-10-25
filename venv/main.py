import tkinter as tk
from tkinter import *
from Macros import *
import threading
import time


#creating the window
window = tk.Tk()
window.geometry("500x500")
window.title("Destiny Master Grind")



#Selection checkboxes
drunkenBool = tk.BooleanVar()
drunkenCheck = tk.Checkbutton(window, text = "Drunken Sailor", variable=drunkenBool, onvalue = True )
drunkenCheck.grid(row = 0, column = 0,)

fatBool = tk.BooleanVar()
fatCheck = tk.Checkbutton(window, text = "Fat Fingered", variable=fatBool, onvalue = True )
fatCheck.grid(row = 1, column = 0,)

indecisiveBool = tk.BooleanVar()
indecisiveCheck = tk.Checkbutton(window, text = "Indecisive", variable=indecisiveBool, onvalue = True )
indecisiveCheck.grid(row = 2, column = 0,)

#create macro threads
drukenEvent = threading.Event()
drunkenThread = threading.Thread(target=drunkenSailor, args=(drukenEvent,))
drunkenThread.daemon = True

fatEvent = threading.Event()
fatThread = threading.Thread(target=fatFingered, args=(fatEvent,))
fatThread.daemon = True

indecisiveEvent = threading.Event()
indecisiveThread = threading.Thread(target=indecisive, args=(indecisiveEvent,))
indecisiveThread.daemon = True
#Apply Selection Button
def applyButtonAction():
    if(drunkenBool.get()):
        drunkenThread.start()
    if(fatBool.get()):
        fatThread.start()
    if(indecisiveBool.get()):
        indecisiveThread.start()

def stopButtonAction():
    drukenEvent.set()
    fatEvent.set()
    indecisiveEvent.set()
    print("stopped threads")
    time.sleep(1)
    drukenEvent.clear()
    fatEvent.clear()
    indecisiveEvent.clear()
    print("events cleared")

applyButton = tk.Button(window, text="Apply", command= lambda : applyButtonAction())
applyButton.grid(row=20, column=2)

stopButton = tk.Button(window, text="Stop", command= lambda : stopButtonAction())
stopButton.grid(row=20, column=3)

#Making the program run
window.mainloop()

