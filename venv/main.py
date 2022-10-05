import tkinter as tk
from tkinter import *
from Macros import drunkenSailor

#creating the window
window = tk.Tk()
window.geometry("500x500")
window.title("Destiny Master Grind")


#Selection checkboxes
drunkenCheck = tk.Checkbutton(window, text = "Drunken Sailor")
drunkenCheck.grid(row = 0, column = 0)

#Apply Selection Button
def applyButtonAction():
    if(drunkenCheck.getboolean()):
      drunkenSailor()

applyButton = tk.Button(window, text="Apply", command= lambda : applyButtonAction())
applyButton.grid(row=2, column=2)

#Making the program run
window.mainloop()