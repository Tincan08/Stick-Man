class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def Move(self):
        pass

    def Coords(self):
        return self.coordinates
