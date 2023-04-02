import turtle as t

width = int(input())
height = int(input())
map = []
for i in range(height):
    map.append(list(input()))

distance_map = []
for y in range(height):
    line = []
    for x in range(width):
        line.append(0)
    distance_map.append(line)


def find(point):
    for y in range(height):
        for x in range(width):
            if map[y][x] == point:
                return (x, y)


start_point = find("S")
end_point = find("C")


def move(x, y, path):
    distance_map[y][x] = path
    avalible_points = []
    for step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        tx = x + step[0]
        ty = y + step[1]
        if 0 <= tx < width and 0 <= ty < height and (map[ty][tx] == "." or map[ty][tx] == "C") and (
                distance_map[ty][tx] == 0 or distance_map[ty][tx] > path + 1):
            avalible_points.append((tx, ty))
            distance_map[ty][tx] = path + 1
    for point in avalible_points:
        move(point[0], point[1], path + 1)


move(start_point[0], start_point[1], 0)
print(distance_map[end_point[1]][end_point[0]])

MAP_SCALE = 10
def draw_pixel(x, y, color):
    t.pu()
    t.goto(x * MAP_SCALE, y * MAP_SCALE)
    t.pd()
    t.begin_fill()
    t.color(color)
    for i in range(4):
        t.fd(MAP_SCALE)
        t.rt(90)
    t.end_fill()

t.tracer(0,1)
for y in range(height):
    for x in range(width):
        if map[y][x] == ".":
            color = "green"
        elif map[y][x] == "#":
            color = "black"
        elif map[y][x] == "S":
            color = "blue"
        elif map[y][x] == "C":
            color = "yellow"
        draw_pixel(-x, y, color)
t.tracer(1,1)
input()