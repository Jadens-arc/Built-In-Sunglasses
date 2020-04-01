#!/usr/bin/env python3
from tkinter import Scale
from tkinter import Tk
from tkinter import Button
from os import system, popen



root = Tk()
root.title('☼')
root.geometry('50x100')
root.resizable(False, False)
root.wm_attributes("-topmost", 1)

def setBrightness(event):
    _level = level.get() / 100
    if _level <= .2:
        _level = .2
    system(f'xrandr --output HDMI-1 --brightness {_level}')

level = Scale(root, from_=100, to_=0)
level.set(float(popen("xrandr --verbose | awk '/Brightness/ { print $2; exit }'").read()) * 100)
level.bind("<ButtonRelease-1>", setBrightness)
level.pack()



root.mainloop()

