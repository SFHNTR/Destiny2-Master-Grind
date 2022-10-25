import tkinter as tk
from tkinter import *
from Macros import *
import multiprocessing
import time

#create macro threads
drunkenProcess = multiprocessing.Process(target=drunkenSailor)

fatProcess = multiprocessing.Process(target=fatFingered)

indecisiveProcess = multiprocessing.Process(target=indecisive)

dancingProcess = multiprocessing.Process(target=randomDancing)

tripProcess = multiprocessing.Process(target=tripping)

hopsProcess= multiprocessing.Process(target=hops)

reloadProcess = multiprocessing.Process(target=compulsiveReload)


#Apply Selection Button
def applyButtonAction():
    if(drunkenBool.get()):
        drunkenProcess.start()
    if(fatBool.get()):
        fatProcess.start()
    if(indecisiveBool.get()):
        indecisiveProcess.start()
    if(dancingBool.get()):
        dancingProcess.start()
    if(tripBool.get()):
        tripProcess.start()
    if (hopsBool.get()):
        hopsProcess.start()
    if (reloadBool.get()):
        reloadProcess.start()

def stopButtonAction():
    if(drunkenProcess.is_alive()):
        drunkenProcess.terminate()
    if(fatProcess.is_alive()):
        fatProcess.terminate()
    if(indecisiveProcess.is_alive()):
        indecisiveProcess.terminate()
    if(dancingProcess.is_alive()):
        dancingProcess.terminate()
    if(tripProcess.is_alive()):
        tripProcess.terminate()
    if(hopsProcess.is_alive()):
        hopsProcess.terminate()
    if(reloadProcess.is_alive()):
        reloadProcess.terminate()
    print("Processes Killed")

if __name__ == '__main__':
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

    dancingBool = tk.BooleanVar()
    dancingCheck = tk.Checkbutton(window, text = "Random Dancing", variable=dancingBool, onvalue = True )
    dancingCheck.grid(row = 3, column = 0,)

    tripBool = tk.BooleanVar()
    tripCheck = tk.Checkbutton(window, text = "Tripping", variable=tripBool, onvalue = True )
    tripCheck.grid(row = 4, column = 0,)

    hopsBool = tk.BooleanVar()
    hopsCheck = tk.Checkbutton(window, text = "Hops", variable=hopsBool, onvalue = True )
    hopsCheck.grid(row = 5, column = 0,)

    reloadBool = tk.BooleanVar()
    reloadCheck = tk.Checkbutton(window, text = "Compulsive Reload", variable=reloadBool, onvalue = True )
    reloadCheck.grid(row = 6, column = 0,)


    applyButton = tk.Button(window, text="Apply", command= lambda : applyButtonAction())
    applyButton.grid(row=20, column=2)

    stopButton = tk.Button(window, text="Stop", command= lambda : stopButtonAction())
    stopButton.grid(row=20, column=3)

    #Making the program run
    window.mainloop()


