from Battleship.res.global_variables import *
import random
import time
"""
LANET OLASI RANDOM SAYI ŞEYLERİ
"""

grid = [[False] * pixel_num] * pixel_num

for x in range(2):
    for y in range(10):
        grid[y][x] = True

enemy_grid = []
for x in range(pixel_num):
    enemy_grid.append([])
    for y in range(pixel_num):
        enemy_grid[-1].append((x, y))


def hitler():
    global enemy_grid
    random.seed(time.time())

    rx = random.randint(0, len(enemy_grid) - 1)
    if len(enemy_grid[rx]) == 0:
        # patlaması zorlaşsın diye
        time.sleep(0.01)
        return hitler()
    elif len(enemy_grid[rx]) == 1:
        ry = 0
    else:
        ry = random.randint(0, len(enemy_grid[rx]) - 1)

    rv = enemy_grid[rx][ry]
    enemy_grid[rx].pop(ry)
    return rv


def did_hit(location):
    # print("".join([str(i) + "\n" for i in grid]))
    # print(location)

    rv = True if grid[location[0]][location[1]] else False
    return rv, hitler()