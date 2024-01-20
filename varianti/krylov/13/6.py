from turtle import *
a = Screen()
screensize(10000, 10000)
m = 25
tracer(0)
left(90)
right(30)
for i in range(10):
    forward(30*m)
    right(60)
    forward(30 * m)
    right(120)
pu()
for x in range(45):
    for y in range(45):
        goto(x*m, y*m)
        dot(6)
done()