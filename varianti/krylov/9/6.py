from turtle import *
a = Screen()
screensize(10000, 10000)
tracer(0)
m = 25
left(90)
for i in range(11):
    forward(111*m)
    right(120)
pu()
for x in range(0, 15):
    for y in range(0, 15):
        goto(x*m, y*m)
        dot(6)
done()