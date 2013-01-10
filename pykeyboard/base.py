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

    def lookup_character_value(self, character):
        """
        If necessary, lookup a valid API value for the key press from the
        character.
        """
        raise NotImplementedError