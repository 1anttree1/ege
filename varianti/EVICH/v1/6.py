from turtle import *
a = Screen()
screensize(10000, 10000)
m = 25
tracer(0)
left(90)
for i in range(10):
    forward(2*m)
    right(120)
    for j in range(2):
        right(330)
        forward(4*m)
pu()
for x in range(1,18):
    for y in range(1,8):
        goto(x*m, y*m)
        dot(6)
done()