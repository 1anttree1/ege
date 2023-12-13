from turtle import *
ms = 25
a = Screen()
screensize(10000, 10000)
tracer(0)
left(90)
for i in range(2):
    forward(17*ms)
    left(90)
    forward(10*ms)
    left(90)
pu()
back(4*ms)
right(90)
back(3*ms)
left(90)
pd()
for i in range(2):
    forward(40 * ms)
    right(90)
    forward(10 * ms)
    right(90)
pu()
for x in range(-40,40):
    for y in range(-4,37):
        goto(x*ms, y*ms)
        dot(5)
done()