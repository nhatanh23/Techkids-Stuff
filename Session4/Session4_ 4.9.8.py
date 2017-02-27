from math import pi

def area_of_circle(r):
    a = round((pi* r**2),2)
    return a
while True:
    radius = float(input("Radius?: "))
    print(area_of_circle(radius))  
