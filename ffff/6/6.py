from turtle import *
ms = 25
a = Screen()
screensize(1000, 1000)
tracer(0)
left(90)
for i in range(4):
    forward(5*ms)
    right(90)
    forward(10*ms)
    right(90)
pu()
for x in range(0, 15):
    for y in range(0, 15):
        goto(x*ms, y*ms)
        dot(6)
done()
