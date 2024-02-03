from pygame.draw import lines
from const import DRAW_PRECISION, HELPER_COLOR, RESOLUTION, ACTIVE_COLOR, BASE_COLOR, MASTER_COLOR
from point import Point

class Curve:
    def __init__(self, p1 = Point(0, 0), p2 = Point(0, 0)):
        self.p = [p1, (p1 * 0.66 + p2 * 0.33), (p1 * 0.33 + p2 * 0.66), p2]
        self.w = [k for k in range(1, 5)]

    def __value(self, t):
        # hardcoded horner for 3 degree bezier
        a = ((self.p[0] * self.w[0] * (1 - t) + \
            self.p[1] * self.w[1] * 3 * t) * (1 - t) + \
            self.p[2] * self.w[2] * 3 * t * t ) * (1 - t) + \
            self.p[3] * self.w[3] * t * t * t 
        b = ((self.w[0] * (1 - t) + \
            self.w[1] * 3 * t) * (1 - t) + \
            self.w[2] * 3 * t * t ) * (1 - t) + \
            self.w[3] * t * t * t 
        return a / b
    
    def draw(self, surface, active_point, selected = False, show_points = True, draw_precision = DRAW_PRECISION, width = 1):
        us = [k / draw_precision for k in range(draw_precision)]
        draw_points = [tuple(self.__value(u)) for u in us]
        lines(surface, ACTIVE_COLOR if selected else BASE_COLOR, False, draw_points, width)

        if show_points:
            for i, (w, point) in enumerate(zip(self.w, self.p)):
                if i in (0, 3):
                    color = (MASTER_COLOR if point is active_point else ACTIVE_COLOR) if selected else BASE_COLOR
                    point.draw(surface, color, w)
                else:
                    if selected:
                        color = (MASTER_COLOR if point is active_point else HELPER_COLOR)
                        point.draw(surface, color, w)

    def __dict__(self):
        return {'points': [(int(p.x), int(p.y)) for p in self.p], 'weights': self.w}

    def load(points, weights):
        new_curve = Curve()
        new_curve.p = points
        new_curve.w = weights
        return new_curve