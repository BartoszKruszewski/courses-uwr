def get_real(s, e2, e3, e4, e5, c):
    return s * ((2 ** -1) * 1 + (2 ** -2) * e2 + (2 ** -3) * e3 + (2 ** -4) * e4 + (2 ** -5) * e5) * (2 ** c)

real_numbers = []

for s in (-1, 1):
    for e2 in range(2):
        for e3 in range(2):
            for e4 in range(2):
                for e5 in range(2):
                    for c in range(-1, 2):
                        real_numbers.append(get_real(s, e2, e3, e4, e5, c))

print(sorted(real_numbers))
print(min(real_numbers), max(real_numbers))

import turtle
t = turtle.Turtle()
t.speed(0)

SIZE = 150

for number in sorted(real_numbers):
    t.penup()
    t.goto(SIZE * number, 0)
    t.pendown()
    t.pencolor("red")
    t.lt(90)
    t.forward(5)
    t.rt(180)
    t.forward(5)
    t.lt(90)
    t.pencolor("black")  # Przywrócenie koloru czarnego

# Ukrycie turtli
t.hideturtle()

# Zatrzymanie okna
turtle.done()