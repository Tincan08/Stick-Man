from tkinter import PhotoImage
from Models.StickMan import StickMan
from Models.PlatformSprite import PlatformSprite
from Helpers.Collision import *

class Main:
    g = StickMan()
    platform1 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform1.gif"), 0, 480, 100, 10)
    g.sprites.append(platform1)
    g.mainloop()