from Battleship.res.global_variables import *
from Battleship.lib.ocean import Ocean
import pygame
import time


def run_time(screen, ocean, enemy_ocean):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                pass
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                pass

        if pygame.mouse.get_pressed()[0]:
            pass

        elif pygame.mouse.get_pressed()[2]:
            pass

    screen.fill(colors["WHITE"])

    enemy_ocean.update()
    ocean.update()

    # print(pygame.mouse.get_pos())
    pygame.display.update()

    return True


def main():
    pygame.display.init()
    pygame.display.set_caption(CAPTION)
    screen = pygame.display.set_mode((WIDTH + 1, HEIGHT + 1))
    # screen.fill(colors["DEFAULT_BACKGROUND"])

    running = bool(1)
    # yapf: disable
    ocean = Ocean(screen, (100, 80), (400, 380), 10)
    enemy_ocean = Ocean(screen, (600, 80), (900, 380), 10)

    while running:
        start_time = time.time()

        running = run_time(screen, ocean, enemy_ocean)

        # FPS DÜZENLEMESİ
        while (1 / FPS) > (time.time() - start_time):
            continue