from Battleship.res.global_variables import *
import pygame
import time


class Ship:
    def __init__(self, screen, length, pixel_width, pos, angle=0):
        self.default_pos = self.pos = pos
        self.pixel_width = pixel_width
        # self.is_selected = False
        # self.is_suitable = False
        # self.is_placed = False
        self.length = length
        self.screen = screen
        self.angle = angle

        # calc rect fonksiyonunda belirlenecek
        self.state = "not selected"
        self.start_pos = None
        self.location = None
        self.end_pos = None
        self.height = None
        self.width = None

        self.calc_rect()

    @property
    def state(self):
        # kullanılmıyor
        if self.color == colors["BLUE"]:
            return "placed"
        elif self.color == colors["TURQ"]:
            return "not selected"
        elif self.color == colors["GREEN"]:
            return "suitable"
        elif self.color == colors["ORANGE"]:
            return "not suitable"

    @state.setter
    def state(self, value):
        if value == "placed":
            self.color = colors["BLUE"]
        elif value == "not selected":
            self.color = colors["TURQ"]
        elif value == "suitable":
            self.color = colors["GREEN"]
        elif value == "not suitable":
            self.color = colors["ORANGE"]
        else:
            raise ValueError

    def calc_rect(self):
        # sağa
        if self.angle == 0:
            self.start_pos = [i - (self.pixel_width // 2) for i in self.pos]
            self.width = self.pixel_width * self.length
            self.height = self.pixel_width

        # aşağı
        elif self.angle == 1:
            self.start_pos = [i - (self.pixel_width // 2) for i in self.pos]
            self.width = self.pixel_width
            self.height = self.pixel_width * self.length

        # sola
        elif self.angle == 2:
            self.start_pos = (self.pos[0] -
                              (self.pixel_width *
                               (self.length - 1) + self.pixel_width // 2),
                              self.pos[1] - self.pixel_width // 2)

            self.width = self.pixel_width * self.length
            self.height = self.pixel_width

        # yukarı
        elif self.angle == 3:
            # Burada ne yaptğımı bir daha hiçbir zaman anlayamayacağım )-:
            self.start_pos = (self.pos[0] - self.pixel_width // 2,
                              self.pos[1] -
                              (self.pixel_width *
                               (self.length - 1) + self.pixel_width // 2))

            self.width = self.pixel_width
            self.height = self.pixel_width * self.length

        # yapf: disable
        self.end_pos = self.start_pos[0] + self.width, self.start_pos[1] + self.height
        self.rect = pygame.Rect(self.start_pos, (self.width, self.height))

    def go(self, pos):
        self.pos = pos
        self.calc_rect()

    def move(self, start_pos):
        self.pos = tuple([(i + self.pixel_width // 2) for i in start_pos])
        self.calc_rect()

    def draw(self, pos=None):
        # self.is_suitable = is_suitable if is_suitable is not None else self.is_suitable
        # self.color = colors["BLUE"] if is_suitable else colors["ORANGE"]
        if pos:
            self.go(pos)

        pygame.draw.rect(self.screen, self.color, self.rect)

    def turn(self, value=1):
        self.angle += value
        # self.angle = self.angle % 4  # en fazla 4e kadar
        self.angle = self.angle % 2  # gereksiz keşke daha önce fark etseydim
        self.calc_rect()