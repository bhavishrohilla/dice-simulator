import random
from tkinter import *

root = Tk()
root.geometry("700x450")

l1 = Label(root,font=("times", 200))

def roll():
    print("rolling")
b1 = Button(root, text="lets roll....", command = roll)
b1.place(x=330,y=0)

root.mainloop()