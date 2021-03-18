from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital clock")

def get_time():
    timeVar=time.strftime("%I:%M:%S %p" " %a")
    clock.config(text=timeVar)
    clock.after(200,get_time)

Label(master,font=("Arial",30),text="Digital Clock",bg="grey",fg="black").pack()
clock = Label(master,font=("Cambria",90),bg="grey",fg="cyan")
clock.pack()

get_time()

master.mainloop()

