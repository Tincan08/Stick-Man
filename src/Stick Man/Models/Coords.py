"""
Class that organizes coordinates within the game.

This class matches up with the tkinter coordinate system and can help facilitate tracking coordinate data for objects in a consistent way.
"""
class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.y1 = y1
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2
