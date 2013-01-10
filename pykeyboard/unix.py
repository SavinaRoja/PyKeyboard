from Xlib.display import Display
from Xlib import X
from Xlib.ext.xtest import fake_input
from Xlib.XK import string_to_keysym

from base import PyKeyboardMeta

import time

special_X_keysyms = {
    ' ' : "space",
    '\t' : "Tab",
    '\n' : "Return",  # for some reason this needs to be cr, not lf
    '\r' : "Return",
    '\e' : "Escape",
    '!' : "exclam",
    '#' : "numbersign",
    '%' : "percent",
    '$' : "dollar",
    '&' : "ampersand",
    '"' : "quotedbl",
    '\'' : "apostrophe",
    '(' : "parenleft",
    ')' : "parenright",
    '*' : "asterisk",
    '=' : "equal",
    '+' : "plus",
    ',' : "comma",
    '-' : "minus",
    '.' : "period",
    '/' : "slash",
    ':' : "colon",
    ';' : "semicolon",
    '<' : "less",
    '>' : "greater",
    '?' : "question",
    '@' : "at",
    '[' : "bracketleft",
    ']' : "bracketright",
    '\\' : "backslash",
    '^' : "asciicircum",
    '_' : "underscore",
    '`' : "grave",
    '{' : "braceleft",
    '|' : "bar",
    '}' : "braceright",
    '~' : "asciitilde"
    }

shift_key = 50  # This is constant, as far as I can tell; it works for now

class PyKeyboard(PyKeyboardMeta):
    """The PyKeyboard implementation for Unix systems with Xlib."""
    def __init__(self, display=None):
        PyKeyboardMeta.__init__(self)
        self.display = Display(display)
        self.display2 = Display(display)
    
    def press_key(self, character=''):
        """Press a given character key."""
        shifted = self.is_char_shifted(character)
        if shifted:
            fake_input(self.display, X.KeyPress, shift_key)
        char_val = self.lookup_character_value(character)
        fake_input(self.display, X.KeyPress, char_val)
        self.display.sync()

    def release_key(self, character=''):
        """Release a given character key."""
        shifted = self.is_char_shifted(character)
        char_val = self.lookup_character_value(character)
        fake_input(self.display, X.KeyRelease, char_val)
        if shifted:
            fake_input(self.display, X.KeyRelease, shift_key)
        self.display.sync()

    def tap_key(self, character='', repeat=1):
        """Press and release a given character key n times."""
        shifted = self.is_char_shifted(character)
        for i in xrange(repeat):
            if shifted:
                fake_input(self.display, X.KeyPress, shift_key)
            self.press_key(character)
            self.release_key(character)
            if shifted:
                fake_input(self.display, X.KeyRelease, shift_key)
            self.display.sync()
    
    def type_string(self, char_string, char_interval=0):
        """A convenience method for typing longer strings of characters."""
        for i in char_string:
            time.sleep(char_interval)
            self.tap_key(i)
    
    def is_char_shifted(self, character):
        """Returns True if the key character is uppercase or shifted."""
        if character.isupper():
            return True
        if character in '<>?:"{}|~!@#$%^&*()_+':
            return True
        return False
    
    def lookup_character_value(self, character):
        """
        Looks up the keysym for the character then returns the keycode mapping
        for that keysym.
        """
        ch_keysym = string_to_keysym(character)
        if ch_keysym == 0:
            ch_keysym = string_to_keysym(special_X_keysyms[character])
        return self.display.keysym_to_keycode(ch_keysym)
