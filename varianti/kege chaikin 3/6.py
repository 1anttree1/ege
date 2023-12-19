from turtle import *
a = Screen()
screensize(10000, 10000)
ms = 25
tracer(0)
left(90)
for i in range(3):
    forward(8*ms)
    left(90)
    forward(14*ms)
    left(90)
pu()
for i in range(4):
    right(90)
    back(3*ms)
    left(90)
pd()
for i in range(2):
    forward(7*ms)
    left(90)
    forward(5*ms)
    left(90)
pu()
for x in range(-16,15):
    for y in range(-16,15):
        goto(x*ms, y*ms)
        dot(6)
done()