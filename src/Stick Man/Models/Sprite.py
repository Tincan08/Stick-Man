"""
Sprite class has all the basic functionality of a sprite object.

This object will be a parent object for all the other sprite classes.  If a default behavior is needed for all sprite classes it should be set here.
"""
class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self): # Some sprites will move, some wont, this creates a pass for those that don't, and a way to overwrite for ones that do.
        pass

    def coords(self): # All sprites will need to have coordinates to be placed on the screen.
        return self.coordinates
