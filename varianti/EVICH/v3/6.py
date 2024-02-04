from turtle import *
a =Screen()
screensize(10000, 10000)
m = 25
tracer(0)
left(90)
for i in range(9):
    forward(8*m)
    right(120)
pu()
for x in range(15):
    for y in range(16):
        goto(x*m,y*m)
        dot(6)
done()