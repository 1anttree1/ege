from turtle import *
a = Screen()
screensize(10000, 10000)
left(90)
m = 25
tracer(0)
right(90)
for i in range(8):
    forward(4*m)
    left(72)
pu()
for x in range(20):
    for y in range(20):
        goto(x*m, y*m)
        dot(6)
done()