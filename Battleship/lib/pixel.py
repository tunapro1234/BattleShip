from Battleship.res.global_variables import *
import pygame
import time


class Pixel:
    def __init__(self, screen, pos, width_height):
        self.rect = pygame.Rect(pos, width_height)
        self.screen = screen

        self.color = None
        self.state = "empty"

    @property
    def state(self):
        if self.color == colors["RED"]:
            return "attacked"
        elif self.color == colors["GREEN"]:
            return "hit"
        elif self.color == colors["BLUE"]:
            return "ship"
        # elif self.color == colors["DEFAULT_BACKGROUND"]:
        else:
            return "empty"

    @state.setter
    def state(self, value):
        if value == "empty":
            self.color = colors["DEFAULT_BACKGROUND"]
        elif value == "attacked":
            self.color = colors["RED"]
        elif value == "ship":
            self.color = colors["BLUE"]
        elif value == "hit":
            self.color = colors["GREEN"]
        else:
            raise ValueError

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)