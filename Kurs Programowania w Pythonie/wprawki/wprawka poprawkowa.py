import turtle as t
import random


def get_width(x):
    return x * 3 ** (1 / 2)


def draw_hex(x, y, color, size):
    t.pu()
    t.color(color)
    t.begin_fill()
    t.goto(x, y)
    t.setheading(90)
    for i in range(6):
        t.pu()
        t.fd(size)
        t.pd()
        t.rt(120)
        t.fd(size)
        t.pu()
        t.rt(120)
        t.fd(size)
        t.rt(180)
    t.end_fill()


t.tracer(0, 0)
MAP_SIZE = 10
HEX_SIZE = 20
BORDER_SIZE = 3
GREY_PART_SIZE = 5
HEX_INTERLUDE_X = get_width(HEX_SIZE)
HEX_INTERLUDE_Y = HEX_SIZE * 1.5
HEX_SHIFT = HEX_INTERLUDE_X / 2

for y in range(MAP_SIZE):
    for x in range(MAP_SIZE):
        pos_x = x * HEX_INTERLUDE_X
        pos_y = y * HEX_INTERLUDE_Y
        if y % 2 == 0:
            pos_x += HEX_SHIFT
        draw_hex(pos_x, pos_y, (0, 0, 0), HEX_SIZE)
        draw_hex(pos_x, pos_y, (0.5, 0.5, 0.5), HEX_SIZE - BORDER_SIZE)
        draw_hex(pos_x, pos_y,
                 (random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255),
                 HEX_SIZE - BORDER_SIZE - GREY_PART_SIZE)
t.tracer(1, 0)

input()
