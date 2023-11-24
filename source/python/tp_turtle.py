from turtle import *

rayon = 100
n = 10
angle = 360/ n

circle(rayon)
up()
goto(0,rayon)
down()

for i in range(n):
    forward(rayon)
    backward(rayon)
    left(angle)

