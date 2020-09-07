from Battleship.res.global_variables import *
import pygame
import time


class Ship:
    def __init__(self, screen, length, pixel_width, pos, angle=0):
        self.pixel_width = pixel_width
        self.length = length
        self.screen = screen
        self.angle = angle
        self.pos = pos
        self.calc_rect()

    def calc_rect(self):
        if self.angle == 0:
            self.rect = pygame.Rect(
                tuple([i - (self.pixel_width // 2) for i in self.pos]),
                (self.pixel_width * self.length, self.pixel_width))

        elif self.angle == 1:
            self.rect = pygame.Rect(
                tuple([i - (self.pixel_width // 2) for i in self.pos]),
                (self.pixel_width, self.pixel_width * self.length))

        elif self.angle == 2:
            self.rect = pygame.Rect(
                (self.pos[0] - (self.pixel_width *
                                (self.length - 1) + self.pixel_width // 2),
                 self.pos[1] - self.pixel_width // 2),
                (self.pixel_width * self.length, self.pixel_width))

        elif self.angle == 3:
            self.rect = pygame.Rect(
                (self.pos[0] - self.pixel_width // 2, self.pos[1] -
                 (self.pixel_width *
                  (self.length - 1) + self.pixel_width // 2)),
                (self.pixel_width, self.pixel_width * self.length))

    def draw(self, pos, is_suitable):
        self.color = colors["BLUE"] if is_suitable else colors["ORANGE"]
        self.pos = pos
        self.calc_rect()

        pygame.draw.rect(self.screen, self.color, self.rect)

    def turn(self, value=1):
        self.angle += value
        self.angle = self.angle % 4  # en fazla 4e kadar
        self.calc_rect()