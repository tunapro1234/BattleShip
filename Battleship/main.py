from Battleship.test.enemy_ai1 import did_hit
from Battleship.res.global_variables import *
from Battleship.lib.ocean import Ocean
from Battleship.lib.ship import Ship
import pygame
import time
"""
end game 
GUI düzenlemesi lazım gemilerin etrafına çizgi gibi
gemiler ilk konumlarında yan yana yerleşebilseler çok hoş olur
enemy_ai branch
socket branch

"""
selected_ship = None
attack_cursor = None
ready = None


def run_time(screen, my_ocean, enemy_ocean, ships, x_rect):
    global selected_ship
    global attack_cursor
    global ready

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if ready == "started":
            # attack cursor varsa değişti mi diye kotrol et yoksa olup olmadığını kontrol et
            if attack_cursor is not None:
                # yapf: disable
                attack_c = enemy_ocean.ocean[attack_cursor[0]][attack_cursor[1]]
                # karmaşık görünmesin diye
                # yapf: disable
                if not is_in_area((mouse_pos := pygame.mouse.get_pos()), attack_c):
                    # yapf: disable
                    enemy_ocean.ocean[attack_cursor[0]][attack_cursor[1]].state = "empty"
                    # eğer mouse alanın içinden çıktıysa baştan hesapla
                    attack_cursor = None

            # yapf: disable
            if is_in_area((mouse_pos := pygame.mouse.get_pos()), enemy_ocean):
                # yapf: disable
                (x, y) = enemy_ocean.get_location(mouse_pos)
                if enemy_ocean.ocean[x][y].state == "empty":
                    enemy_ocean.ocean[x][y].state = "will attacked"
                    attack_cursor = (x, y)

            if pygame.mouse.get_pressed()[0] and attack_cursor is not None:
                did_hit_, incoming_hit = did_hit(attack_cursor)
                # enemy_ocean.ocean[attack_cursor[0]][attack_cursor[1]].state = "hit" if did_hit_ else "attacked"

                # eğer gemi kalmadıysa True döndürüyor
                if enemy_ocean.take_hit(attack_cursor, did_hit_):
                    ready = "won"

                elif my_ocean.take_hit(incoming_hit):
                    ready = "lost"

                attack_cursor = None

        elif ready in ["lost", "won"]:
            pass

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # yapf: disable
                    if len([i for i in ships if i.state == "placed"]) == len(ships) or DEBUG_MODE:
                        ready = "started"
                        continue


                if event.key == pygame.K_ESCAPE:
                    ships[selected_ship].angle = 0
                    ships[selected_ship].state = "not selected"
                    ships[selected_ship].go(ships[selected_ship].default_pos)

                    selected_ship = None

            # sol klik
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if selected_ship is None:
                    for index, ship in enumerate(ships):
                        if is_in_area(mouse_pos, ship):
                            if ship.state == "placed":
                                my_ocean.remove(ship)

                            selected_ship = index
                            ships[selected_ship].location = None
                            ships[selected_ship].state = "not suitable"
                # sağ klik
                else:
                    if ships[selected_ship].state == "suitable":
                        my_ocean.place(ships[selected_ship])
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

                    if but_does_it_fit(s_ship, (x, y), ships, my_ocean):
                        # gemi olması gereken konuma yerleştiriliyor
                        ships[selected_ship].move(my_ocean.ocean[x][y].start_pos)

                        # gemi rengi yeşile dönüştürülüyor
                        ships[selected_ship].location = (x, y)
                        ships[selected_ship].state = "suitable"

                    else:
                        ships[selected_ship].location = None
                        ships[selected_ship].state = "not suitable"

                else:
                    ships[selected_ship].location = None
                    ships[selected_ship].state = "not suitable"

    if ready == "waiting":
        screen.fill(colors["ORANGE"])
    elif ready == "lost":
        screen.fill(colors["RED"])
    elif ready == "won":
        screen.fill(colors["GREEN"])
    elif ready == "started":
        screen.fill(colors["WHITE"])
    else:
        screen.fill(colors["BLUE"])

    enemy_ocean.draw()
    my_ocean.draw()
    pygame.draw.rect(screen, colors["BLACK"], x_rect)
    pygame.draw.rect(screen, colors["WHITE"], x_rect, 1)

    for index, ship in enumerate(ships):
        if index != selected_ship:
            if ship.state != "placed":
                ship.draw()
        else:
            # eğer gride oturtulmadıysa fareyi takip ediyor
            # yapf: disable
            pos = pygame.mouse.get_pos() if ship.state == "not suitable" else ship.pos

            # bilmiyorum
            ship.draw(pos=pos)

    pygame.display.update()
    return True


def but_does_it_fit(ship, pos, ships, ocean):
    # isim tuhaf kaçtı biraz

    if ship.angle == 0 and pos[0] + (ship.length - 1) < ocean.pixel_num:
        for i in range(ship.length):
            if ocean.ocean[pos[0]+i][pos[1]].state == "ship":
                return False
        return True

    elif ship.angle == 1 and pos[1] + (ship.length - 1) < ocean.pixel_num:
        for i in range(ship.length):
            if ocean.ocean[pos[0]][pos[1]+i].state == "ship":
                return False
        return True

    elif ship.angle == 2 and pos[0] - (ship.length - 1) >= 0:
        for i in range(ship.length):
            if ocean.ocean[pos[0]-i][pos[1]].state == "ship":
                return False
        return True

    elif ship.angle == 3 and pos[1] - (ship.length - 1) >= 0:
        for i in range(ship.length):
            if ocean.ocean[pos[0]][pos[1]-i].state == "ship":
                return False
        return True

    return bool(0) #UuUUUUUUuuuUUUUuuu


def main():
    pygame.display.init()
    pygame.display.set_caption(CAPTION)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # screen.fill(colors["DEFAULT_BACKGROUND"])

    running = bool(1)

    ships = []
    # ship_lens = sorted(ship_lens)

    #   Bunları zaten global_variablesda
    # ayarlamıştım ama yine de silmeye kıyamadım

    # width yetiyor mu
    if (ship_lens[-1])*(b_width//pixel_num) > (x_area := WIDTH - (x_offset*2+b_width)*2):
        raise Exception("Size Error (width)")

    # height yetiyor mu
    # if len(ship_lens) >= pixel_num:
    #     raise Exception("Size Error (height)")

    # yapf: disable
    my_ocean = Ocean(screen, (x_offset*2+x_area, y_offset), (b_width+x_offset*2+x_area, b_width+y_offset), pixel_num, total_ship, draw_grid=grid_)
    enemy_ocean = Ocean(screen, ((WIDTH-x_offset)-b_width, y_offset), (WIDTH-x_offset, b_width+y_offset), pixel_num, total_ship , draw_grid=grid_)

    ### ŞŞŞ BURAYA

    x_rect = pygame.Rect((0, 0), (x_area+x_offset, HEIGHT))
    # pygame.draw.rect(screen, colors["DEFAULT_BACKGROUND"], x_rect)

    # gemilerin arasında olması gereken mesafe
    ship_y_gap = ((HEIGHT - y_offset*2) - len(ship_lens)*my_ocean.pixel_width) // (len(ship_lens)-1)

    for index, ship_len in enumerate(ship_lens):
        #   ortada kalan bölümün yarısını alıyon sonra ilk geminin
        # uzunluğunun yarısını aldığın şeyden çıkarıp genişliğin yarısını ekliyon

        # genişliğin yarısını ekleme sebebin benim mouse için geliştirdiğim boş şey
        ship_pos = ((x_area//2)-((ship_len/2)*my_ocean.pixel_width)+my_ocean.pixel_width//2 + (x_offset//2),
                    index*(my_ocean.pixel_width + ship_y_gap) + y_offset + my_ocean.pixel_width//2)

        ships.append(Ship(screen, ship_len, my_ocean.pixel_width, ship_pos))




    while running:
        start_time = time.time()

        running = run_time(screen, my_ocean, enemy_ocean, ships, x_rect)
        # print(pygame.mouse.get_pos())

        # FPS DÜZENLEMESİ
        while (1 / FPS) > (time.time() - start_time):
            continue