grid_ = 1
grid_color = "WHITE"
x_offset = 60
y_offset = 60
b_width = 400
pixel_num = 10

ship_lens = sorted([2, 2, 2, 3, 3, 4, 4])

if b_width % pixel_num != 0:
    raise Exception("genişlik ve pixel sayısı uyumlu değil")

# yapf: disable
WIDTH = (x_offset * 2 + b_width) * 2 + ship_lens[-1] * (b_width // pixel_num)
if pixel_num > len(ship_lens):
    HEIGHT = y_offset * 2 + b_width
else:
    print("[ FAIL ] b_width must be bigger")
    # exit()
    HEIGHT = len(ship_lens)*2*(b_width // pixel_num) + y_offset*2

CAPTION = "BATTLESHIP"
P_WIDTH = 20
FPS = 120

colors = {
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255),
    "GREEN": (0, 255, 0),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "TURQ": (64, 224, 208),
    "ORANGE": (255, 69, 0),
    "DEFAULT_BACKGROUND": (50, 50, 50)
}
grid_color = colors[grid_color]


def is_in_area(point, area):
    if area.start_pos[0] < point[0] < area.end_pos[0]:
        if area.start_pos[1] < point[1] < area.end_pos[1]:
            return True
    return False


def is_in(point, area_start_pos, area_end_pos):
    if area_start_pos[0] < point[0] < area_end_pos[0]:
        if area_start_pos[1] < point[1] < area_end_pos[1]:
            return True
    return False