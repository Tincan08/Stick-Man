from Models.Sprite import Sprite
from Models.Coords import Coords

"""
The PlatformSprite class is used for each platform that needs to be placed in the game.
"""
class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game) # Initialize Sprite parent class

        # Initialize PlatformSprite class
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image = self.photo_image, anchor = 'nw')
        self.coordinates = Coords(x, y, x  + width, y + height)
