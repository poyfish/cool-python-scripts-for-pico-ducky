import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)


Delay = .35


def troll():

    kbd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(Delay)
    layout.write("cmd")
    time.sleep(Delay)
    kbd.send(Keycode.ENTER)
    time.sleep(Delay)
    layout.write("curl ascii.live/rick")
    time.sleep(Delay)
    kbd.send(Keycode.ENTER)



if usb_hid.devices:
    troll()
    time.sleep(5)