from Battleship.res.global_variables import *
import pygame
import time


class Pixel:
    def __init__(self, screen, pos, width_height):
        self.end_pos = pos[0] + width_height[0], pos[1] + width_height[1]
        self.pixel_width, self.pixel_height = width_height
        self.start_pos = pos

        self.rect = pygame.Rect(pos, width_height)
        self.screen = screen

        self.color = None
        self.state = "empty"

    @property
    def state(self):
        if self.color == colors["WHITE"]:
            return "attacked"
        elif self.color == colors["ORANGE"]:
            return "hit"
        elif self.color == colors["TURQ"]:
            return "ship"
        elif self.color == colors["RED"]:
            return "will attacked"
        # elif self.color == colors["DEFAULT_BACKGROUND"]:
        else:
            return "empty"

    @state.setter
    def state(self, value):
        if value == "empty":
            self.color = colors["DEFAULT_BACKGROUND"]
        elif value == "attacked":
            self.color = colors["WHITE"]
        elif value == "ship":
            self.color = colors["TURQ"]
        elif value == "hit":
            self.color = colors["ORANGE"]
        elif value == "will attacked":
            self.color = colors["RED"]
        else:
            raise ValueError

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)