from turtle import Screen, Turtle
import random as rn
import time

seedNum = time.process_time()
rn.seed(seedNum)

print("How many flowers would you like?")
fNum = int(input())

screen = Screen()
turtle = Turtle()

screen.colormode(255)
turtle.speed(1000000000000)

width = 500
height = 500

screen.screensize(width, height)

for i in range(fNum):
    xCon = rn.randint(-(width/2), width/2)
    yCon = rn.randint(-(height/2), height/2)

    R = rn.randint(0, 255)
    G = rn.randint(0, 255)
    B = rn.randint(0, 255)

    turtle.penup()
    turtle.goto(xCon, yCon)
    turtle.pendown()

    turtle.pencolor(R, G, B)

    for i in range(36):
        turtle.left(170)
        turtle.forward(200)

screen.mainloop()
