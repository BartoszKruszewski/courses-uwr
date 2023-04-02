import turtle as t
import random

f = open("obraz.txt","r")
data = f.readlines()
f.close()

def draw_square(size):
    for i in range(4):
        t.fd(size)
        t.rt(90)

def draw_pixel(color,x,y):
    SIZE = 5
    t.goto(x * SIZE,y * SIZE)
    t.color(color)
    t.pd()
    t.begin_fill()
    draw_square(SIZE)
    t.end_fill()
    t.pu()

t.speed(0)
t.up()

pixels = []
x = 0
y = 0
for line in data:
    x = 0
    for pixel in line.split(" "):
        color = [x/255 for x in eval(pixel)]
        pixels.append((color,x,y))
        x += 1
    y += 1

for i in range(len(pixels)):
    pixel = random.choice(pixels)
    pixels.remove(pixel)
    draw_pixel(pixel[0],pixel[1],pixel[2])

input()