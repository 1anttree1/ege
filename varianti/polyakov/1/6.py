from turtle import *
a = Screen()
left(90)
tracer(0)
m = 25
for i in range(2):
    forward(16*25)
    right(90)
    forward(9*m)
    right(90)
pu()
forward(5*m)
right(90)
forward(11*m)
right(90)
pd()
for i in range(2):
    forward(20 * 25)
    right(90)
    forward(8 * m)
    right(90)
pu()
for x in range(-15, 15):
    for y in range(-15, 18):
        goto(x*m, y*m)
        dot(6)
done()
