from pygame import init, WINDOWCLOSE, quit, MOUSEWHEEL, KEYDOWN, Surface
from pygame.time import Clock
from pygame.display import set_mode, update as update_display
from pygame.event import get as get_event
from pygame.image import load as image_load
from pygame.transform import scale
from point import Point
from mouse import Mouse
from curve import Curve
from const import RESOLUTION, FRAMERATE, ACTIVE_COLOR, SELECT_RADIUS, \
    CURVE_NAME, IMAGE_NAME, BACKGROUND_COLOR
from json import dumps, loads
from os import listdir, mkdir

class Main:
    def __init__(self):
        init()
        self.screen = set_mode(RESOLUTION)
        self.clock = Clock()
        self.mouse = Mouse(
            self.on_right_click,
            self.on_right_hold,
            self.on_left_click,
            self.on_left_hold,
            self.on_right_release,
            self.on_left_release
        )
        
        self.running = True
        self.curves = []
        self.active_point = None
        self.active_curve = None
        self.lock = False

        self.background = Surface(RESOLUTION)
        self.load_background()

        self.load_points()
        while self.running:
            self.running = not get_event(WINDOWCLOSE)
            self.handle_events()
            if not self.lock:
                self.mouse.update()
            self.update_screen()
        self.save_points()
        quit()
    
    def load_background(self):
        if 'images' not in listdir():
            mkdir('images')
        if IMAGE_NAME in listdir('images'):
            image = image_load('images/' + IMAGE_NAME)
            size_x, size_y = image.get_size()
            if size_x > size_y:
                r = RESOLUTION[1] / size_y
                image = scale(image, (size_x * r, size_y * r))
                self.background.blit(
                    image, ((RESOLUTION[0] - size_x * r) / 2, 0))
            else:
                r = RESOLUTION[0] / size_x
                image = scale(image, (size_x * r, size_y * r))
                self.background.blit(
                    image, (0, (RESOLUTION[1] - size_y * r) / 2))
        
    def handle_events(self):
        for e in get_event():
            if e.type == KEYDOWN:
                if e.key == 1073742048: # left ctrl
                    self.active_point = None
                    self.active_curve = None
                elif e.key == 127: # delete
                    self.active_point = None
                    self.curves.remove(self.active_curve)
                elif e.key == 1073742049: # left shift
                    self.lock = not self.lock
            elif e.type == MOUSEWHEEL:
                for curve in self.curves:
                    if self.active_point in curve.p:
                        w = curve.w[curve.p.index(self.active_point)]
                        w += e.y / 10
                        w = max(w, 0.1)
                        curve.w[curve.p.index(self.active_point)] = w

    def on_right_click(self, pos):
        for curve in self.curves:
            for point in curve.p:
                if abs(point.x - pos[0]) + abs(point.y - pos[1]) < SELECT_RADIUS:
                    self.active_point = point
                    self.active_curve = curve
                    return

    def on_right_hold(self, pos):
        if self.active_point:
            self.active_point.x, self.active_point.y = pos

    def on_left_click(self, pos):
        point = Point(pos[0], pos[1])
        
        if self.active_point is not None:
            curve = Curve(self.active_point, point)
            self.curves.append(curve)
            self.active_curve = curve
        self.active_point = point

    def on_left_hold(self, pos):
        pass

    def on_right_release(self, pos):
        for curve in self.curves:
            for point in curve.p:
                if point is not self.active_point:
                    if abs(point.x - pos[0]) + abs(point.y - pos[1]) < SELECT_RADIUS:
                        if curve.p.index(point) in (0, 3):
                            self.active_curve.p[
                                self.active_curve.p.index(self.active_point)
                            ] = point
                            return
    
    def on_left_release(self, pos):
        pass

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.screen.blit(self.background, (0, 0))

        if self.active_point is not None and self.active_curve is None:
            self.active_point.draw(self.screen, ACTIVE_COLOR, 1)

        for curve in self.curves:
            curve.draw(self.screen, self.active_point, self.active_curve is curve, not self.lock)

    def save_points(self):
        if 'curves' not in listdir():
            mkdir('curves')
        with open('curves/' + CURVE_NAME, 'w') as file:
            file.write(dumps(
                self.curves,
                default = lambda o: o.__dict__()
            ))

    def load_points(self):
        if 'curves' in listdir() and CURVE_NAME in listdir('curves'):
            with open('curves/' + CURVE_NAME, 'r') as file:
                for data in loads(file.read()):
                    points = data['points']
                    weights = data['weights']
                    point_objects = []
                    for point in points:
                        selected = False
                        for curve in self.curves:
                            for p in curve.p:
                                if p.x == point[0] and p.y == point[1]:
                                    point_objects.append(p)
                                    selected = True
                        if not selected:
                            point_objects.append(Point(point[0], point[1]))
                    self.curves.append(Curve.load(point_objects, weights))

    def update_screen(self):
        self.draw()
        update_display()
        self.dt = self.clock.tick(FRAMERATE) / 1000 * FRAMERATE

if __name__ == '__main__':
    Main()

    