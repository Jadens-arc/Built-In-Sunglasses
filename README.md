# Controlling Ubuntu Desktop Brightness 


get the current display output
```console
$ xrandr | grep " connected" | cut -f1 -d " " 
```

Set brightness from command line
``` console
$ xrandr --output [display output] --brightness [0.0 - 1.0]
``` 

Get current Brightness from command line
``` console
$ xrandr --verbose | awk '/Brightness/ { print $2; exit }'
```