import pygame
from turtle import Screen, Turtle

screen = Screen()
turtle = Turtle()

screen.colormode(255)
turtle.speed(10)

left = False
right = False
forward = False
backward = False


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()


def move_tur():

    while True:
        if left == True:
            turtle.left(2)

        if right == True:
            turtle.right(2)

        if forward == True:
            turtle.forward(2)

        if backward == True:
            turtle.backward(2)


main()
