from Battleship.res.global_variables import *
from Battleship.lib.pixel import Pixel
import pygame


class Ocean:
    def __init__(self, screen, start_pos, end_pos, pixel_num, draw_grid=0):
        self.height = abs(end_pos[1] - start_pos[1])
        self.width = abs(end_pos[0] - start_pos[0])

        self.pixel_num = pixel_num
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.screen = screen

        self.rect = pygame.Rect(start_pos, (self.width, self.height))
        self.default_background_color = colors["DEFAULT_BACKGROUND"]

        self.draw_g = draw_grid
        self.pixel_width = self.width // pixel_num
        self.pixel_height = self.height // pixel_num
        self.init_ocean()

    def get_location(self, pos):
        x, y = pos[0] - self.start_pos[0], pos[1] - self.start_pos[1]
        return x // self.pixel_width, y // self.pixel_height

    def init_ocean(self):
        self.ocean = []
        for x in range(self.pixel_num):
            self.ocean.append([])
            for y in range(self.pixel_num):
                self.ocean[x].append(
                    Pixel(self.screen,
                          (self.start_pos[0] + (x * self.pixel_width),
                           self.start_pos[1] + (y * self.pixel_height)),
                          (self.pixel_width, self.pixel_height)))

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

    def draw(self):
        pygame.draw.rect(self.screen, self.default_background_color, self.rect)

        self.draw_pixels()
        if self.draw_g:
            self.draw_grid()

        # pygame.display.update()

    def change_ocean_state(self, ship, state):
        (x, y) = ship.location
        if ship.angle == 0:
            for i in range(ship.length):
                self.ocean[x + i][y].state = state
        elif ship.angle == 1:
            for i in range(ship.length):
                self.ocean[x][y + i].state = state
        elif ship.angle == 2:
            for i in range(ship.length):
                self.ocean[x - i][y].state = state
        elif ship.angle == 3:
            for i in range(ship.length):
                self.ocean[x][y - i].state = state
        else:
            raise Exception

    def remove(self, ship):
        self.change_ocean_state(ship, "empty")

    def place(self, ship):
        self.change_ocean_state(ship, "ship")
