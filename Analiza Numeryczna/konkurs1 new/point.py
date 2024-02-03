from pygame.gfxdraw import filled_circle
from const import POINT_RADIUS

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, color):
        filled_circle(surface, int(self.x), int(self.y), POINT_RADIUS, color)

    
