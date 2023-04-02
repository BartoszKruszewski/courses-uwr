import turtle as t

t.speed(0)

def square(n):
    for i in range(4):
        t.fd(n)
        t.rt(90)

def polkole(n):
    E = 10
    for i in range(E):
        t.fd(n)
        t.rt(180/E)

def spirala(n):
    def xxx():
        for i in range(n + n % 2):
            polkole(Fibonacci(i))

    return xxx


def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    a = 1
    b = 1
    x = a + b
    for i in range(n-3):
        b = a
        a = x
        x = a + b
    return x

def repeatOnCircle(figure,r,n):
    for i in range(n):
        t.pu()
        t.rt(360/n)
        t.fd(r)
        t.pd()
        figure()
        t.pu()
        t.bk(r)

repeatOnCircle(lambda :repeatOnCircle(spirala(8),80,5),200,8)
input()