import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

Delay = 0.25

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

def rick_the_roll():
    kbd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(Delay)

    layout.write('chrome')

    time.sleep(Delay)

    kbd.send(Keycode.ENTER)

    time.sleep(Delay)

    layout.write("https://fakeupdate.net/win10ue/")

    kbd.send(Keycode.ENTER)

    time.sleep(Delay*3)

    kbd.send(Keycode.F11)

if usb_hid.devices:
    rick_the_roll()
