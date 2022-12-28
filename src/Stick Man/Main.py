from tkinter import PhotoImage
from Models.StickMan import StickMan
from Models.PlatformSprite import PlatformSprite
from Models.StickFigureSprite import StickFigureSprite
from Models.DoorSprite import DoorSprite

"""
Main entry point for the application.  

This class begins the game processing, loads assets into the game, initilizes game parameters, and starts the main loop for the game.
"""
class Main:
    g = StickMan() # Initialize StickMan class, this will begin the instance of the game.

    # Create door, player, and platform objects, and set coordinates for placement in the game.
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
    door = DoorSprite(g, PhotoImage(file = "Assets/animations/door-closed.gif"),45, 30, 40, 35)
    sf = StickFigureSprite(g)

    # Append objects to the list of sprites and load them into the game.
    g.sprites.append(door)
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
    g.sprites.append(sf)

    g.mainloop() # Begin the game's main loop logic.

