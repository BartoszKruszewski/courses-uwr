import turtle as t

f = open("obraz.txt","r")
data = f.readlines()
f.close()

def draw_square(size):
    for i in range(4):
        t.fd(size)
        t.rt(90)

def draw_pixel(color,x,y):
    SIZE = 1
    t.goto(x * SIZE,y * SIZE)
    t.color(color)
    t.begin_fill()
    draw_square(SIZE)
    t.end_fill()

t.tracer(0,1)


x = 0
y = 0
for line in data:
    x = 0
    for pixel in line.split(" "):
        color = [x/255 for x in eval(pixel)]
        draw_pixel(color,x,y)
        x += 1
    y += 1

t.tracer(1,1)

input()