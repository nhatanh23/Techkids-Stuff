from turtle import *
speed(-1)
num = int(input("Number of Square?: "))
bgcolor("lightgreen")
pensize(3)
color("hotpink")
a = 20
def draw_square(a,num):
    for n in range(num):
        for i in range(4):
            forward(a*(n + 1))
            lt(90)
        pst=a/2*(n + 1)
        penup()
        setposition(-pst,-pst)
        pendown()
draw_square(a,num)
input()
