from Battleship.res.global_variables import *
from Battleship.ocean import Ocean
import pygame
import time


def run_time(ocean, enemy_ocean):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
            if event.key == pygame.K_RIGHT:
            if event.key == pygame.K_UP:
            if event.key == pygame.K_DOWN:

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:

        if pygame.mouse.get_pressed()[0]:
            print(Board.get_pos(pygame.mouse.get_pos()))

        elif pygame.mouse.get_pressed()[2]:
            # rv = pygame.mouse.get_pos()
            pass

        if event.type == pygame.KEYDOWN:
            pass

    ocean.update()
    return True


def main():
    pygame.display.init()
    pygame.display.set_caption(CAPTION)
    screen = pygame.display.set_mode((WIDTH + 1, HEIGHT + 1))
    screen.fill(colors["DEFAULT_BACKGROUND"])

    running = bool(1)
    # yapf: disable
    ocean = Ocean(screen, (0, 0), (WIDTH + 1, HEIGHT + 1))
    # enemy_ocean = Ocean(screen, (0, 0), (WIDTH + 1, HEIGHT + 1))

    while running:
        start_time = time.time()

        running = run_time(ocean, None)

        # FPS DÜZENLEMESİ
        while (1 / FPS) > (time.time() - start_time):
            continue