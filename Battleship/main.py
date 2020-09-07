from Battleship.res.global_variables import *
from Battleship.lib.ocean import Ocean
from Battleship.lib.ship import Ship
import pygame
import time

selected_ship = None


def run_time(screen, my_ocean, enemy_ocean, ships):
    global selected_ship
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ships[selected_ship].angle = 0
                ships[selected_ship].state = "not selected"
                ships[selected_ship].go(ships[selected_ship].default_pos)

                selected_ship = None

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if selected_ship is None:
                for index, ship in enumerate(ships):
                    if is_in_area(mouse_pos, ship):
                        selected_ship = index
                        ships[selected_ship].state = "not suitable"
            else:
                if ships[selected_ship].state == "suitable":
                    ships[selected_ship].state = "placed"
                    selected_ship = None

        elif pygame.mouse.get_pressed()[2]:
            ships[selected_ship].turn()

    if selected_ship is not None:
        s_ship = ships[selected_ship]

        # eğer fare kafanın içinden çıkarsa
        if not is_in((mouse_pos := pygame.mouse.get_pos()), s_ship.start_pos,
                     [(i + s_ship.pixel_width) for i in s_ship.start_pos]):
            # fareyi takip et
            ships[selected_ship].go(mouse_pos)

        if is_in_area(s_ship.pos, my_ocean):
            # olması gereken konum alınıyor
            (x, y) = my_ocean.get_location(s_ship.pos)

            if but_does_it_fit(s_ship, (x, y), my_ocean):
                # gemi olması gereken konuma yerleştiriliyor
                ships[selected_ship].move(my_ocean.ocean[x][y].start_pos)

                # gemi rengi yeşile dönüştürülüyor
                ships[selected_ship].state = "suitable"

            else:
                ships[selected_ship].state = "not suitable"

        else:
            ships[selected_ship].state = "not suitable"

    screen.fill(colors["WHITE"])

    enemy_ocean.draw()
    my_ocean.draw()

    for index, ship in enumerate(ships):
        if index != selected_ship:
            ship.draw()
        else:
            # eğer gride oturtulmadıysa fareyi takip ediyor
            # yapf: disable
            pos = pygame.mouse.get_pos() if ship.state == "not suitable" else ship.pos
            ship.draw(pos=pos)

    pygame.display.update()
    return True


def but_does_it_fit(ship, pos, ocean):
    # isim tuhaf kaçtı biraz
    if ship.angle == 0:
        if pos[0] + (ship.length - 1) < ocean.pixel_num:
            return True
    elif ship.angle == 1:
        if pos[1] + (ship.length - 1) < ocean.pixel_num:
            return True
    elif ship.angle == 2:
        if pos[0] - (ship.length - 1) >= 0:
            return True
    elif ship.angle == 3:
        if pos[1] - (ship.length - 1) >= 0:
            return True
    return bool(0) #UuUUUUUUuuuUUUUuuu



def main():
    pygame.display.init()
    pygame.display.set_caption(CAPTION)
    screen = pygame.display.set_mode((WIDTH + 1, HEIGHT + 1))
    # screen.fill(colors["DEFAULT_BACKGROUND"])

    running = bool(1)
    # yapf: disable
    my_ocean = Ocean(screen, (100, 80), (400, 380), 10)
    enemy_ocean = Ocean(screen, (600, 80), (900, 380), 10)

    ships = []
    ship_lens = [2, 3, 4]
    last_ship_pos = (100, 500)
    for index, ship_len in enumerate(ship_lens):
        ships.append(Ship(screen, ship_len, my_ocean.pixel_width, last_ship_pos))
        last_ship_pos = last_ship_pos[0] + (ship_len+1)*my_ocean.pixel_width, last_ship_pos[1]

    while running:
        start_time = time.time()

        running = run_time(screen, my_ocean, enemy_ocean, ships)

        # FPS DÜZENLEMESİ
        while (1 / FPS) > (time.time() - start_time):
            continue