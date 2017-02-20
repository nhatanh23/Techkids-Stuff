from turtle import*
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(-1)
##for i in range (3,7):
##    color(colors[i-2])
##    for j in range (i):    
##        forward(100)
##        left(360/i)

for i in range (5):
    color(colors[i], colors[i])
    begin_fill()
    for j in range (2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
