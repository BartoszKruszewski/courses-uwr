from point import Point
from curve import Curve
from os import listdir
from json import loads
from pygame import Surface, SRCALPHA

class Char:
    def __init__(self, path, normal_scaling = 1.0):
        self.curves = self.load_curves(path)
        self.normalize_curves(normal_scaling)
        self.cache = None

    def normalize_curves(self, normal_scaling):
        all_points = [point for curve in self.curves for point in curve.p]
        center = Point(min([p.x for p in all_points]), min([p.y for p in all_points]))
        width = max([p.x for p in all_points]) - center.x
        height = max([p.y for p in all_points]) - center.y
        for curve in self.curves:
            normalized_points = []
            for point in curve.p:
                normalized_point = point - center
                normalized_point.x = normalized_point.x / width * normal_scaling + (1 - normal_scaling) / 2
                normalized_point.y = normalized_point.y / height * normal_scaling + (1 - normal_scaling)
                normalized_points.append(normalized_point)
            curve.p = normalized_points

    def draw(self, surface, size, pos, style = 'normal'):
        if self.cache is None or style != self.cache[0] or size != self.cache[1]:
            new_surface = Surface((size, size), SRCALPHA)
            if style == 'italic':
                shift = min([point for curve in self.curves for point in curve.p], key = lambda p: p.y).x
                curves = [
                    Curve.load([Point(min(p.x + (1 - shift) * (1 - p.y), 1), p.y) for p in curve.p], curve.w)
                    for curve in self.curves
                ]
            else:
                curves = self.curves
            scaled_curves = [
                Curve.load([p * size for p in curve.p], curve.w)
                for curve in curves
            ]
            [curve.draw(new_surface, Point(0, 0), False, False, size // 2, 3 if style == 'bold' else 1) for curve in scaled_curves]
            self.cache = (style, size, new_surface)
        surface.blit(self.cache[2], (pos.x, pos.y))

    def load_curves(self, path):
        curves = []
        if 'curves' in listdir() and f'{path}.json' in listdir('curves'):
            with open(f'curves/{path}.json', 'r') as file:
                for data in loads(file.read()):
                    points = [Point(p[0], p[1]) for p in data['points']]
                    weights = data['weights']
                    curves.append(Curve.load(points, weights))
        return curves

