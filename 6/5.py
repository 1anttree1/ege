from turtle import *
a = Screen()
screensize(100000, 100000)
ms = 20
left(90)
tracer(0)

pu()
forward(100*ms)
right(90)
forward(100 * ms)
right(30)
pd()
for i in range(10):
    forward(25*ms)
    right(90)
pu()
for x in range(150):
    for y in range(150):
        goto(x*ms, y*ms)
        dot(6)
done()