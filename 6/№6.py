from turtle import *
ms = 35
a = Screen()
a.screensize(10000, 10000)
tracer(0)
left(90)
for i in range(7):
    forward(10*ms)
    right(120)
pu()
for x in range(0, 10):
    for y in range(0, 12):
        goto(x*ms, y*ms)
        dot(5)
done()