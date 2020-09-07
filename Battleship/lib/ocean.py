from Battleship.res.global_variables import *
from Battleship.lib.pixel import Pixel
import pygame


class Ocean:
    def __init__(self, screen, start_pos, end_pos, pixel_num, draw_grid=1):
        self.height = abs(end_pos[1] - start_pos[1])
        self.width = abs(end_pos[0] - start_pos[0])

        self.pixel_num = pixel_num
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.screen = screen
        self.init_ocean()

        self.rect = pygame.Rect(start_pos, (self.width, self.height))
        self.default_background_color = colors["DEFAULT_BACKGROUND"]

        self.draw_g = draw_grid
        self.pixel_width = self.width // pixel_num
        self.pixel_height = self.height // pixel_num

    def init_ocean(self):
        # for döngülü hale getirip pozisyon ve width_height ver
        self.ocean = [[None] * self.pixel_num] * self.pixel_num

    def draw_grid(self):
        color = colors["WHITE"]
        for i in range(self.pixel_num + 1):
            # Dinamik yapmalıydım
            pygame.draw.line(
                self.screen, color,
                (self.start_pos[0], self.start_pos[1] + i * self.pixel_width),
                (self.end_pos[0], self.start_pos[1] + i * self.pixel_width))

            pygame.draw.line(
                self.screen, color,
                (self.start_pos[0] + i * self.pixel_width, self.start_pos[1]),
                (self.start_pos[0] + i * self.pixel_width, self.end_pos[1]))

    def draw_pixels(self):
        for x in range(self.pixel_num):
            for y in range(self.pixel_num):
                self.ocean[x][y].draw()

    def update(self):
        pygame.draw.rect(self.screen, self.default_background_color, self.rect)
        if self.draw_g:
            self.draw_grid()

        self.draw_pixels()

        # pygame.display.update()
