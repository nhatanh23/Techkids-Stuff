from turtle import *
speed(-1)
bgcolor("lightgreen")
color("blue")
pensize(3)

def draw(n):
    for i in range(n):
        for x in range(4):
            forward(100)
            lt(90)
        lt(360/n)
draw(20)
