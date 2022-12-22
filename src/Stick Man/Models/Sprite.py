class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def Move(self):
        pass #ToDo: Update this with movement logic.

    def Coords(self):
        return self.coordinates
