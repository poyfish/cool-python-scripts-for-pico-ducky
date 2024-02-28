import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)


Delay = .25

# Function to send key presses to open the command prompt
def rick_the_roll():
    # Press Windows key + R to open Run dialog
    kbd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(Delay)  # Wait for the Run dialog to open

    # Type 'cmd' to open Command Prompt
    kbd.send(Keycode.C, Keycode.M, Keycode.D)
    time.sleep(Delay)  # Wait for 'cmd' to be typed

    # Press Enter to execute the command
    kbd.send(Keycode.ENTER)
    time.sleep(Delay)  # Wait for the Command Prompt to open

    layout.write("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    time.sleep(Delay)

    kbd.send(Keycode.ENTER)


if usb_hid.devices:
    rick_the_roll()
