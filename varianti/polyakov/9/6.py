from turtle import *
a = Screen()
screensize(10000, 10000)
left(90)
m = 25
tracer(0)
left(40)
for i in range(5):
    right(-95)
    forward(12*m)
    left(45)
    forward(8*m)
    left(40)
pu()
for x in range(-15, 15):
    for y in range(-20, 15):
        goto(x*m, y*m)
        dot(6)
done()