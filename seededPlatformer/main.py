import math
import random
import time

import arcade
import numpy

#   screen width and height
sWidth = 900
sHeight = 600

global plats

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
        print("number of platforms: ", self.numPlat)

        #	sets up the 2d list for the platform data
        rows, cols = (self.numPlat, 6)
        self.plats = [[0 for i in range(cols)] for j in range(rows)]

        for x in range(self.numPlat):
            height = 0
            width = 0
            leftPos = 0
            rightPos = 0
            heightMod = random.random() * 200

            if x == 0:
                leftPos = 0
                width = 75

            else:
                temp = self.plats[x - 1][3]
                leftPos = (temp + int(math.sqrt(seed) / 2))
                width = int(math.sqrt(seed) / 2)

            height = int((seed / 275) + heightMod)
            rightPos = leftPos + width

            self.plats[x][0] = height
            self.plats[x][1] = leftPos
            self.plats[x][2] = width
            self.plats[x][3] = rightPos
            self.plats[x][4] = (rightPos - leftPos) / 2  # center x
            self.plats[x][5] = height / 2  # center y

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        for i in range(self.numPlat):
            arcade.draw_rectangle_filled(
                self.plats[i][4], self.plats[i][5], self.plats[i][2], self.plats[i][0], arcade.color.FERRARI_RED)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(sWidth, sHeight)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
