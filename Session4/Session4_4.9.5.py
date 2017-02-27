from turtle import *
speed(-1)
##pensize(2)
bgcolor("lightgreen")
color("blue")
rt(180)
def draw_maze(n):
    a=0
    for i in range(n):
        forward(5+a)
        rt(90)
        forward(5+a)
        rt(90)
        a+=5
##draw_maze(50)
##
def draw_maze(n):
    a=0
    b=n
    for i in range(n):
        forward(5+a)
        rt(90)
        forward(5+a)
        rt(90)
        a+=5
        lt(360/(b+200))
draw_maze(50)
