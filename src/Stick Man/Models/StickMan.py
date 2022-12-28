from tkinter import *
import time

"""
Main game logic.
"""
class StickMan:
    def __init__(self):
        self.tk = Tk() # Tkinter is initialized. 
        self.tk.title("Mr. Stickman Races for the Exit") # The title is set.
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width = 500, height = 500, highlightthickness = 0) # The game canvas is created.
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.bg = PhotoImage(file = "Assets/animations/background.gif") # Background is loaded into the canvas, and set to be tiled.
        w = self.bg.width()
        h = self.bg.height()

        # Make background image tiled into the background.
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor = 'nw')

        self.sprites = [] # Sprite list is initialized.
        self.running = True # Game is set to running.

    """
    Main loop logic for the game.
    """
    def mainloop(self):
        while 1:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)