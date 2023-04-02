import turtle as t

def draw_branch(n):
    if n > 0:
        t.lt(30)
        t.fd(n)
        draw_branch(n - 5)
        t.bk(n)
        t.rt(60)
        t.fd(n)
        draw_branch(n - 5)
        t.bk(n)
        t.lt(30)

t.tracer(0,0)

t.lt(90)
draw_branch(35)

t.tracer(1,1)

input()