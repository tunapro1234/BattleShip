from Battleship.res.global_variables import *
import random
import time

# karşılık veren versiyonu gizel olur
enemy_grid = grid = [[False] * pixel_num] * pixel_num

for x in range(2):
    for y in range(10):
        grid[y][x] = True


def hitter():
    global enemy_grid

    random.seed()
    # yapf: disable
    if enemy_grid[(rx := random.randint(0, (pixel_num-1)))][(ry := random.randint(0, (pixel_num-1)))]:
        return hitter()
    else:
        enemy_grid[rx][ry] = True
        return (rx, ry)

def is_hit(location):
    rv = True if grid[location[0]][location[1]] else False
    return rv, hitter()