# Importing Required Modules
import math
from turtle import*

# Defining Heart Shape Functions
def heart1(k):
    return 15*math.sin(k)**3
def heart2(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)

# Setting Up the Turtle Graphics
speed (0)
bgcolor("black")

# Drawing the Heart Shape
for i in range(6000):
    goto(heart1(i)*20,heart2(i)*20)
    for j in range(5):
        color("purple")
    goto(0,0)

# Ending the Program
done()