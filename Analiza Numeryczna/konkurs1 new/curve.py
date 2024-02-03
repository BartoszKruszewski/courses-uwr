from pygame.draw import aalines, lines
from const import DRAW_PRECISION_MULT, ACTIVE_COLOR, BASE_COLOR, MASTER_COLOR, AA
from nifs3 import get_s
from point import Point

class Curve:
    def __init__(self):
        self.points = []
    
    def sample_range(self, n):
        return [i / (n - 1) for i in range(n)]

    def draw(self, surface, active_point, selected = False, show_points = True):
        n = len(self.points)
        if n > 1:
            ts = self.sample_range(n)
            sx = get_s(ts, [p.x for p in self.points])
            sy = get_s(ts, [p.y for p in self.points])
            us = self.sample_range(DRAW_PRECISION_MULT * len(self.points))
            draw_points = [(sx(u), sy(u)) for u in us]
            if AA:
                aalines(surface, ACTIVE_COLOR if selected else BASE_COLOR, False, draw_points)
            else:
                lines(surface, ACTIVE_COLOR if selected else BASE_COLOR, False, draw_points)

            if show_points:
                for point in self.points:
                    point.draw(
                        surface, 
                        (MASTER_COLOR if point is active_point else ACTIVE_COLOR) if selected else BASE_COLOR
                    )

    def save(self, path, id):
        with open(f'{path}/{id}_x.txt', 'w') as file:
            file.write(', '.join([str(int(p.x)) for p in self.points]))
        with open(f'{path}/{id}_y.txt', 'w') as file:
            file.write(', '.join([str(int(p.y)) for p in self.points]))
        with open(f'{path}/{id}_t.txt', 'w') as file:
            file.write(', '.join([str(t) for t in self.sample_range(len(self.points))]))
        with open(f'{path}/{id}_u.txt', 'w') as file:
            file.write(', '.join([str(u) for u in self.sample_range(DRAW_PRECISION_MULT * len(self.points))]))

    def load(self, path, id):
        with open(f'{path}/{id}_x.txt', 'r') as file:
            xs = [int(x) for x in file.read().split(', ')]
        with open(f'{path}/{id}_y.txt', 'r') as file:
            ys = [int(y) for y in file.read().split(', ')]
        self.points = [Point(x, y) for x, y in zip(xs, ys)]
            