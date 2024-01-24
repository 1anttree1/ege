from turtle import *
a = Screen()
screensize(10000, 10000)
m = 25
tracer(0)
left(90)
for i in range(2):
    forward(5*m)
    left(90)
    back(13*m)
    left(90)
pu()
back(10*m)
right(90)
forward(9*m)
left(90)
pd()
for i in range(2):
    forward(11*m)
    right(90)
    forward(7*m)
    right(90)
pu()
for x in range(17):
    for y in range(-15,15):
        goto(x*m,y*m)
        dot(6)
done()

