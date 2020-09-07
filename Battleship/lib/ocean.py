from Battleship.res.global_variables import *
from Battleship.lib.pixel import Pixel


class Ocean:
    def __init__(self, screen, start_pos, end_pos, pixel_num):
        self.height = start_pos[1] - end_pos[1]
        self.width = start_pos[0] - end_pos[0]

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.screen = screen

        self.pixel_num = pixel_num
        self.pixel_width = self.width // pixel_num
        self.pixel_height = self.height // pixel_num

    def draw_grid():
        grid = [[Pixel()] * pixel_num] * pixel_num