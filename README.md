# Controlling Ubuntu Desktop Brightness 

Set brightness from command line

``` console
$ xrandr --output HDMI-1 --brightness [0.0 - 1.0]
``` 

Get current Brightness from command line
``` console
$ xrandr --verbose | awk '/Brightness/ { print $2; exit }'
```