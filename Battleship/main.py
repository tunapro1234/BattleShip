from Battleship.res.global_variables import *
from Battleship.lib.ocean import Ocean
from Battleship.lib.ship import Ship
import pygame
import time


def run_time(screen, my_ocean, enemy_ocean, test_ship):
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
            if test_ship:
                test_ship.turn()

        elif pygame.mouse.get_pressed()[2]:
            pass
            # test_ship = Ship(screen, 3, my_ocean.pixel_width,
            #                  pygame.mouse.get_pos())

    screen.fill(colors["WHITE"])

    enemy_ocean.draw()
    my_ocean.draw()

    test_ship.draw(pygame.mouse.get_pos(), False)
    pygame.display.update()

    return True


def main():
    pygame.display.init()
    pygame.display.set_caption(CAPTION)
    screen = pygame.display.set_mode((WIDTH + 1, HEIGHT + 1))
    # screen.fill(colors["DEFAULT_BACKGROUND"])

    running = bool(1)
    # yapf: disable
    my_ocean = Ocean(screen, (100, 80), (400, 380), 10)
    enemy_ocean = Ocean(screen, (600, 80), (900, 380), 10)

    test_ship = Ship(screen, 3, my_ocean.pixel_width,
                    pygame.mouse.get_pos())

    while running:
        start_time = time.time()

        running = run_time(screen, my_ocean, enemy_ocean, test_ship)

        # FPS DÜZENLEMESİ
        while (1 / FPS) > (time.time() - start_time):
            continue