import turtle as t
import random

def prostokat(a,b):
    t.fd(a)
    t.rt(90)
    t.fd(b)
    t.rt(90)
    t.fd(a)
    t.rt(90)
    t.fd(b)
    t.rt(90)

a = 10
b = 10
c = 5
liczba_prostokatow = 30

t.pu()
t.setposition(-250,0)
t.pd()
t.speed("fastest")
t.lt(90)

for i in range(liczba_prostokatow):
    a += random.randint(0,10)
    prostokat(a,b)
    t.rt(90)
    t.pu()
    t.fd(b + c)
    t.pd()
    t.lt(90)

input()
