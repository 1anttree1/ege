from turtle import *
a = Screen()
screensize(1000, 1000)
ms = 25
tracer(10)
left(90)
for i in range(4):
    forward(5*ms)
    right(90)
    forward(10*ms)
    right(90)
pu()
for x in range(0, 12):
    for y in range(0, 12):
        goto(x*ms, y*ms)
        dot(5)
done()