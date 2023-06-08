from src.engine.files.imports import *

class Main:
    def __init__(self):
        SDL_Init(SDL_INIT_VIDEO)
        self.window = window.Window()
        self.color = color.Colors()
        self.event = event.Event()
        self.keys = event.Keys()
        self.draw = draw.Draw()

    def Quit(self, window):
        SDL_DestroyRenderer(window.renderer)
        SDL_FlushEvent(window.event)
        SDL_DestroyWindow(window.window)
        SDL_Quit()
