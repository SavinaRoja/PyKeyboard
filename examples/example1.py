"""
A script to illustrate PyKeyboard use..
"""

import pykeyboard
import time

k = pykeyboard.PyKeyboard()

def press_and_hold(character, hold_time):
    k.press_key(character)
    time.sleep(hold_time)
    k.release_key(character)

k.type_string('Hello World!', char_interval=0.15)

k.type_string('https://github.com/SavinaRoja/PyKeyboard')

k.tap_key('A', repeat=4)
press_and_hold('W', 1)
