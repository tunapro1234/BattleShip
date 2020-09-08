from Battleship.res.global_variables import *

# karşılık veren versiyonu gizel olur
grid = [[False] * pixel_num] * pixel_num

for x in range(2):
    for y in range(10):
        grid[y][x] = True


def is_hit(location):
    return True if grid[location[0]][location[1]] else False