from turtle import Turtle, Screen, colormode
import random


colormode(255)

colours = ['DeepSkyBlue', 'orange', 'IndianRed', 'green', 'DarkOrchid', 'wheat', 'SlateGray', 'Seagreen']
direction = [0,90,180,270]
t = Turtle()



def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

t.speed("fastest")

def size(gap):
    for _ in range(int(360/gap)):
        t.color(rand_color())
        t.circle(80)
        t.setheading(t.heading() + gap)
    
size(5)




screen = Screen()
screen.exitonclick()