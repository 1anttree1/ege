from turtle import *
a = Screen()
screensize(10000, 10000)
left(90)
tracer(0)
m = 25
for i in range(3):
    left(90)
    for j in range(4):
        forward(5*m)
        right(90)

pu()
for x in range(-16, 16):
    for y in range(-16, 16):
        goto(x*m, y*m)
        dot(6)
done()

