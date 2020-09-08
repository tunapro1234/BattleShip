from Battleship.res.global_variables import *
import random
import time
"""
LANET OLASI RANDOM SAYI ŞEYLERİ
"""

enemy_grid = grid = [[False] * pixel_num] * pixel_num
for x in range(2):
    for y in range(10):
        grid[y][x] = True

for x in range(pixel_num):
    for y in range(pixel_num):
        enemy_grid[x][y] = (x, y)


def hitter():
    global enemy_grid
    random.seed(time.time())

    rx = random.randint(0, len(enemy_grid) - 1)
    if len(enemy_grid[rx]) == 0:
        # patlaması zorlaşsın diye
        time.sleep(0.01)
        hitter()

    ry = random.randint(0, len(enemy_grid[rx]) - 1)

    rv = enemy_grid[rx][ry]
    enemy_grid[rx].pop(ry)
    return rv


def is_hit(location):
    print(grid)
    print([i for i in location])
    rv = True if grid[location[0]][location[1]] else False
    return rv, hitter()