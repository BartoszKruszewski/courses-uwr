from pygame import init, WINDOWCLOSE, quit, KEYDOWN, Vector2
from pygame.time import Clock
from pygame.display import set_mode, update as update_display
from pygame.event import get as get_event
from pygame.image import load as image_load
from point import Point
from mouse import Mouse
from curve import Curve
from const import FRAMERATE, ACTIVE_COLOR, SELECT_RADIUS, BORDER, \
    CURVES_PATH, IMAGE_PATH, BACKGROUND_COLOR
from os import listdir, mkdir

class Main:
    def __init__(self):
        init()
        self.background = image_load(IMAGE_PATH)
        self.screen = set_mode(Vector2(self.background.get_size()) + Vector2(BORDER) * 2)
        self.clock = Clock()
        self.mouse = Mouse(
            self.on_right_click,
            self.on_right_hold,
            self.on_left_click,
            self.on_left_hold,
            self.on_right_release,
            self.on_left_release
        )
        self.curves = []
        self.active_point = None
        self.active_curve = None
        self.lock = 0

        self.load()
        while not get_event(WINDOWCLOSE):
            self.handle_events()
            if not self.lock:
                self.mouse.update()
            self.update_screen()
        self.save()
        quit()
        
    def handle_events(self):
        for e in get_event():
            if e.type == KEYDOWN:
                if e.key == 1073742048: # left ctrl
                    self.active_point = None
                    self.active_curve = None
                elif e.key == 127: # delete
                    if self.active_curve is not None and self.active_point is not None:
                        self.active_curve.points.remove(self.active_point)
                        self.active_point = None
                        if len(self.active_curve.points) < 2:
                            self.curves.remove(self.active_curve)
                            self.active_curve = None
                elif e.key == 1073742049: # left shift
                    self.lock += 1
                    if self.lock == 3:
                        self.lock = 0

    def on_right_click(self, pos):
        for curve in self.curves:
            for point in curve.points:
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
            if self.active_curve is None:
                curve = Curve()
                curve.points.append(self.active_point)
                self.active_curve = curve
                self.curves.append(curve)
            self.active_curve.points.insert(
                self.active_curve.points.index(self.active_point), point)
        self.active_point = point
            
    def on_left_hold(self, pos):
        pass

    def on_right_release(self, pos):
        pass
    
    def on_left_release(self, pos):
        pass

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        if self.lock in (0, 1):
            self.screen.blit(self.background, Vector2(BORDER))

        if self.active_point is not None and self.active_curve is None:
            self.active_point.draw(self.screen, ACTIVE_COLOR)

        for curve in self.curves:
            curve.draw(self.screen, self.active_point, self.active_curve is curve, self.lock == 0)

    def save(self):
        if CURVES_PATH not in listdir():
            mkdir(CURVES_PATH)
        for i, curve in enumerate(self.curves):
            curve.save(CURVES_PATH, i)

    def load(self):
        if CURVES_PATH in listdir():
            ids = []
            for filename in listdir(CURVES_PATH):
                id = filename.split('_')[0]
                if id not in ids:
                    ids.append(id)
                    curve = Curve()
                    curve.load(CURVES_PATH, id)
                    self.curves.append(curve)

    def update_screen(self):
        self.draw()
        update_display()
        self.dt = self.clock.tick(FRAMERATE) / 1000 * FRAMERATE

if __name__ == '__main__':
    Main()

    