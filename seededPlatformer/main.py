import arcade
import time
import math
import random
import numpy

#   screen width and height
sWidth = 900
sHeight = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        #    randomly generated seed (based on system time)
        random.seed()
        seed = int(random.random() * (100000))

        #	speed at which the screen scroll by
        scrollSpeed = 50

        #   the number of platforms is based on the seed
        self.numPlat = int(math.sqrt(seed) / 3)

        print("seed: ", seed)
        print("number of platforms: ", numPlat)

        #	sets up the 2d list for the platform data
        rows, cols = (numPlat, 6)
        self.plats = [[0 for i in range(cols)] for j in range(rows)]

        for x in range(numPlat):
            height = 0
            width = 0
            leftPos = 0
            rightPos = 0
            heightMod = random.random() * 200

            if x == 0:
                leftPos = 0
                width = 75

            else:
                temp = plats[x - 1][3]
                leftPos = (temp + int(math.sqrt(seed) / 2))
                width = int(math.sqrt(seed) / 2)

            height = int((seed / 275) + heightMod)
            rightPos = leftPos + width

            plats[x][0] = height
            plats[x][1] = leftPos
            plats[x][2] = width
            plats[x][3] = rightPos
            plats[x][4] = (rightPos - leftPos) / 2  # center x
            plats[x][5] = height / 2  # center y

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        for i in range(numPlat):
            arcade.create_rectangle_filled(
                plats[i][4], plats[i][5], plats[i][2], plats[i][0], arcade.color.red)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(sWidth, sHeight)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
