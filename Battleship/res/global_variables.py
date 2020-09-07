WIDTH, HEIGHT = (1000, 600)
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