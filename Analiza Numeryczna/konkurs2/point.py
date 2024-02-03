from pygame.gfxdraw import filled_circle
from const import POINT_RADIUS, RESOLUTION

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, color, w):
        if all((
                POINT_RADIUS + w < self.x < RESOLUTION[0] - POINT_RADIUS - w,
                POINT_RADIUS + w < self.y < RESOLUTION[1] - POINT_RADIUS - w,
            )):
            filled_circle(surface, int(self.x), int(self.y), POINT_RADIUS + int(w), color)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def __mul__(self, a):
        return Point(self.x * a, self.y * a)
    
    def __truediv__(self, a):
        return Point(self.x / a, self.y / a)
    
    def __floordiv__(self, a):
        return Point(int(self.x // a), int(self.y // a))
    
    def __iter__(self):
        return iter([self.x, self.y])

    def __str__(self):
        return f'<Point: {self.x}, {self.y}>'
    
