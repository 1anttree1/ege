from turtle import *
a = Screen()
screensize(10000, 10000)
ms = 25
left(90)
tracer(0)
for i in range(4):
    forward(12*ms)
    right(90)
for i in range(3):
    forward(8*ms)
    right(60)
    forward(8 * ms)
    right(120)
pu()
for x in range(25):
    for y in range(25):
        goto(x*ms,y*ms)
        dot(6)
done()