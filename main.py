#!/usr/bin/env python3
from tkinter import Scale, Tk
from os import system, popen

# window declaration
# 50x100 | non resizable | always on top
root = Tk() 
root.title('☼')
root.geometry('50x100')
root.resizable(False, False)
root.wm_attributes("-topmost", 1)

# uses xrandr to get current output
currentOutput = str(popen('xrandr | grep " connected" | cut -f1 -d " " ').read()).strip()
print(currentOutput)

def setBrightness(event, limiter = 0.2):
    _level = level.get() / 100 # scale returns value from 0 - 100 must be converted to decimal
    print(_level)

    # limits darkest setting to 20% to prevent user from completly blacking out moniter
    if _level <= limiter: 
        _level = limiter
    
    system(f'xrandr --output {currentOutput} --brightness {_level}')

level = Scale(root, from_=100, to_=0)
level.set(float(popen("xrandr --verbose | awk '/Brightness/ { print $2; exit }'").read()) * 100) # sets scale slider to current brightness
level.bind("<ButtonRelease-1>", setBrightness)
level.pack()

root.mainloop()

