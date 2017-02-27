from turtle import *
speed(-1)
bgcolor("lightgreen")
pensize(3)
color("hotpink")
def draw_square(a):
    for i in range(4):
        forward(a)
        lt(90)
    penup()
    forward(a+20)
    pendown()
num = int(input("Number of Square?: "))
for j in range(num):
    draw_square(20)
input()
