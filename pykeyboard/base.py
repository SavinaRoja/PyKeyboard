"""
Provides the operational model. 
"""

import time

class PyKeyboardMeta(object):
    """
    The base class for PyKeyboard. Represents basic operational model.
    """

    def press_key(self, character=''):
        """Press a given character key."""
        raise NotImplementedError

    def release_key(self, character=''):
        """Release a given character key."""
        raise NotImplementedError

    def tap_key(self, character='', n=1):
        """Press and release a given character key n times."""
        for i in xrange(n):
            self.press_key(character)
            self.release_key(character)
        raise NotImplementedError

    def type_string(self, char_string, char_interval=0):
        """A convenience method for typing longer strings of characters."""
        for i in char_string:
            time.sleep(char_interval)
            self.tap_key(i)
        raise NotImplementedError

    def special_key_assignment(self):
        """Makes special keys more accessible."""
        self.shift_key = None
        self.alt_key = None
        self.control_key = None
        self.tab_key = None
        self.return_key = None
        self.enter_key = None
        self.up_key = None
        self.down_key = None
        self.left_key = None
        self.right_key = None
        raise NotImplementedError

    def lookup_character_value(self, character):
        """
        If necessary, lookup a valid API value for the key press from the
        character.
        """
        raise NotImplementedError