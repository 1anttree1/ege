from turtle import *
a = Screen()
screensize(10000, 10000)
tracer(0)
ms = 20
left(90)
forward(100*ms)
right(90)
forward(100*ms)
right(30)
pd()
for i in range(10):
    forward(25*ms)
    left(90)
pu()
for x in range(95, 140):
    for y in range(85, 125):
        goto(x*ms, y*ms)
        dot(6)
done()