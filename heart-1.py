# Importing Necessary Libraries
import math
from turtle import* 

# Defining the Heart Shape Functions
def heart(k):
    return 15*math.sin(k)**3

def heart1(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)

# Turtle Setup
speed(0)
bgcolor("black")

# Drawing the Heart
for i in range(6000):
    goto(heart(i)*20,heart1(i)*20)
    for j in range(5):
        color("#800080")

# Ending the Drawing
done()