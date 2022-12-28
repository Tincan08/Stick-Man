from Models.Coords import Coords
from Models.Sprite import Sprite
"""
DoorSprite is the class for the door object near the top of the canvas.

This object is a child of the Sprite class.
"""
class DoorSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height): # Define class constructor and input parameters
        Sprite.__init__(self, game) # Initialize Sprite parent class

        # Initialize DoorSprite class
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + (width / 2), y + height)
        self.endgame = True # When character reaches door the game ends