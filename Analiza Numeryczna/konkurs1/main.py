import matplotlib.pyplot as plt
from nifs3 import get_s
from os import listdir

'''

Set VIEW_ONLY to False to edit points.

Left click - select point, move point
Right click - add new point
Left CTRL - add new curve
DELETE - delete selected point 

Point's positions automaticly load
from POINTS_PATH txt file when program starts,
and automaticly saves when program is closing.

'''

IMAGE_PATH = 'image.png'
POINTS_PATH = 'points.txt'
VIEW_ONLY = True

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** (1 / 2)
    
    def __str__(self):
        return f'{self.x},{self.y}'

class Main:
    def __init__(self, image_path, points_path, view_only):
        
        self.view_only = view_only
        self.points = {0: []}
        if points_path in listdir():
            self.load_points(points_path)
        self.active_group_id = 0
        self.active_point = None
        self.image = plt.imread(image_path)

        if VIEW_ONLY:
            self.image[:, :, :] = 1
        
        self.fig, self.ax = plt.subplots()
        if not VIEW_ONLY:
            self.fig.canvas.mpl_connect('button_press_event', self.on_click)
            self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        
        self.update_plot()
        plt.show()
        self.save_points(points_path)

    def load_points(self, path):
        self.points.clear()
        id = 0
        with open(path, 'r') as file:
            data = (line.rstrip() for line in file.readlines())
        point_group = []
        for line in data:
            if line == ';':
                self.points[id] = point_group.copy()
                point_group = []
                id += 1
            else:
                cords = line.split(',')
                point_group.append(Point(int(cords[0]), int(cords[1])))

    def save_points(self, path):
        with open(path, 'w') as file:
            for point_group in self.points.values():
                for point in point_group:
                    file.write(f'{point}\n')
                file.write(';\n')

    def new_curve(self):
        new_id = max(self.points.keys()) + 1
        self.points[new_id] = []
        self.active_group_id = new_id

    def on_click(self, event):
        mouse_x, mouse_y = int(event.xdata), int(event.ydata)
        if event.button == 1:
            
            active_changed = False

            for id, point_group in self.points.items():
                for point in point_group:
                    if point.distance(mouse_x, mouse_y) < 5:
                        self.active_point = point
                        self.active_group_id = id
                        active_changed = True
                        break

            if not active_changed and self.active_point is not None:
                self.active_point.x = mouse_x
                self.active_point.y = mouse_y

        elif event.button == 3:
            new_point = Point(mouse_x, mouse_y)
            if self.active_point is not None:
                self.points[self.active_group_id] \
                .insert(self.points[self.active_group_id] \
                .index(self.active_point), new_point)
            else:
                if self.active_group_id in self.points:
                    self.points[self.active_group_id].append(new_point)
                    
            self.active_point = new_point
                    
        self.update_plot()

    def on_key(self, event):
        if event.key == 'control':
            self.active_group_id = max(self.points.keys()) + 1
            self.points[self.active_group_id] = []
            self.active_point = None
            self.update_plot()
        elif event.key == 'delete':
            self.points[self.active_group_id].remove(self.active_point)
            self.active_point = None
            self.update_plot()
        
    def draw_nifs3_curve(self, xps, yps, color):
        ts = [k / len(xps) for k in range(len(xps))]
        sx = get_s(ts, xps)
        sy = get_s(ts, yps)
        M = 1000
        us = [k / M for k in range(M)]
        plt.plot(
            [sx(u) for u in us],
            [sy(u) for u in us],
            color = color
        )

    def update_plot(self):
        plt.clf()

        plt.imshow(self.image)
        
        for id, point_group in self.points.items():
            xps = [p.x for p in point_group]
            yps = [p.y for p in point_group]

            if len(point_group) >= 2:

                self.draw_nifs3_curve(
                    xps, yps,
                    'yellow' if id == self.active_group_id else 'blue'
                )

            if not VIEW_ONLY:
                plt.scatter(xps, yps, c='blue', marker='o')

        if not VIEW_ONLY:
            if self.active_point is not None:
                plt.scatter(
                    [self.active_point.x],
                    [self.active_point.y],
                    c='red', marker='o'
                )

        self.fig.canvas.draw()

if __name__ == "__main__":
    Main(IMAGE_PATH, POINTS_PATH, VIEW_ONLY)
    