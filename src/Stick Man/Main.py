from tkinter import PhotoImage
from Models.StickMan import StickMan
from Models.PlatformSprite import PlatformSprite
from Models.StickFigureSprite import StickFigureSprite
from Helpers.Collision import *

class Main:
    g = StickMan()
    platform1 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform1.gif"), 0, 480, 100, 10)
    platform2 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform1.gif"), 150, 440, 100, 10)
    platform3 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform1.gif"), 300, 400, 100, 10)
    platform4 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform1.gif"), 300, 160, 100, 10)
    platform5 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform2.gif"), 175, 350, 66, 10)
    platform6 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform2.gif"), 50, 300, 66, 10)
    platform7 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform2.gif"), 170, 120, 66, 10)
    platform8 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform2.gif"), 45, 60, 66, 10)
    platform9 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform3.gif"), 170, 250, 32, 10)
    platform10 = PlatformSprite(g, PhotoImage(file = "Assets/animations/platform3.gif"), 230, 200, 32, 10)
    g.sprites.append(platform1)
    g.sprites.append(platform2)
    g.sprites.append(platform3)
    g.sprites.append(platform4)
    g.sprites.append(platform5)
    g.sprites.append(platform6)
    g.sprites.append(platform7)
    g.sprites.append(platform8)
    g.sprites.append(platform9)
    g.sprites.append(platform10)
    sf = StickFigureSprite(g)
    g.sprites.append(sf)
    g.mainloop()

