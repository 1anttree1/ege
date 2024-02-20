from turtle import *
a = Screen()
left(90)
tracer(0)
m = 25
for i in range(5):
    left(60)
    forward(4*m)
    left(120)
    forward(4*m)
pu()
for x in range(-5, 15):
    for y in range(-5, 15):
        goto(x*m,y*m)
        dot(6)
done()