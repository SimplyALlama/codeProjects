import math
import random
import time

import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Seeded Platformer"

class MyGame(arcade.Window):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)

		arcade.set_background_color(arcade.color.AMAZON)

		self.ready = False

	def setup(self):
		#    randomly generated seed (based on system time)
		random.seed()
		seed = int(random.random() * (100000))

		#	speed at which the screen scroll by
		self.scrollSpeed = 4
		self.scrolling = False

		#	movement condiition and speed
		self.movementSpeed = 5
		self.grav = 0.3

		#	toggel to make movement more smooth and disallow double jumps
		self.moveLeft = False
		self.moveRight = False
		self.jumping = False
		self.jumpPress = False

		
		self.numPlat = int(math.sqrt(seed) / 3) #   the number of platforms is based on the seed

		print("seed: ", seed)
		print("number of platforms: ", self.numPlat)

		#	sets up the 2d list for the platform data
		rows = (self.numPlat)
		cols = 6
		
		#	set up the array for the platforms
		self.plats = [[0 for i in range(cols)] for j in range(rows)]

		for x in range(self.numPlat):
			height = 0
			width = 0
			leftPos = 0
			rightPos = 0
			heightMod = random.random()

			if x == 0:
				leftPos = 0
				width = 150
				height = 150

			else:
				temp = self.plats[x - 1][3]
				tempH = self.plats[x - 1][0]

				leftPos = int(temp + (math.sqrt(seed) / 2) * (random.randint(1, 2)))
				width = int((math.sqrt(seed) / 2) * (random.randint(1, 2) + 1))
				height = int((tempH + (seed / 400) + 5) * heightMod)

			rightPos = leftPos + width

			self.plats[x][0] = height
			self.plats[x][1] = leftPos
			self.plats[x][2] = width
			self.plats[x][3] = rightPos
			self.plats[x][4] = leftPos + ((rightPos - leftPos) / 2)  # center x
			self.plats[x][5] = height / 2  # center y
		
		self.playerX = 50
		self.playerY = 177
		self.deltaY = 5
		self.touching = False
		self.playerRadius = 25
			
	def on_draw(self):
		arcade.start_render()
		
		arcade.draw_circle_filled(self.playerX, self.playerY, self.playerRadius, arcade.color.BLACK)	#	draw the player
		
		if self.scrolling == True:
			for i in range(self.numPlat):
				self.plats[i][4] -= self.scrollSpeed
				self.plats[i][1] -= self.scrollSpeed
				self.plats[i][3] -= self.scrollSpeed
		
		for i in range(self.numPlat):	#	draw the platforms	
			arcade.draw_rectangle_outline(self.plats[i][4], self.plats[i][5], self.plats[i][2], self.plats[i][0], arcade.color.FERRARI_RED)	
	
	def jump(self):
		for k in range(self.numPlat):
			if (self.playerX - self.playerRadius) < self.plats[k][3] and (self.playerX + self.playerRadius) > self.plats[k][1]:
				self.deltaY += 10
				self.playerY += self.deltaY
					
	def gravity(self):
			self.playerY += self.deltaY
			self.deltaY -= self.grav

	def hitReg(self):
		if (self.playerY < 0):
			self.playerY = 1
			self.grav = 0

		for j in range(self.numPlat):
			if (self.plats[j][1] < self.playerX < self.plats[j][3]):	#	top of platform
				if (self.playerY - self.playerRadius) < self.plats[j][0]:
					self.playerY += 0.5
					self.deltaY = 0

			if self.plats[j - 1][3] < self.playerX < self.plats[j][1]:  #	right edge
				hold = j - 1
				if (self.playerX - self.playerRadius) < self.plats[hold][3] and self.playerY < self.plats[hold][0]:
					self.playerX = self.plats[hold][3] + self.playerRadius
			
			if self.plats[j][3] < self.playerX < self.plats[j + 1][1]:  #	left edge
				hold = j + 1
				if (self.playerX + self.playerRadius) > self.plats[hold][1] and self.playerY < self.plats[hold][0]:
					self.playerX = self.plats[hold][1] - self.playerRadius

	def on_update(self, delta_time):
		self.hitReg()	
		self.gravity()

		if self.playerX > 250:
			self.scrolling = True		

		if self.moveLeft == True:
			self.playerX -= self.movementSpeed

		if self.moveRight == True:
			self.playerX += self.movementSpeed

		if self.moveLeft == False and self.moveRight == False and self.scrolling == True:
			self.playerX -= self.scrollSpeed
		
	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.SPACE and self.jumpPress == False:
			self.jump()

		if key == arcade.key.LEFT:
			self.moveLeft = True

		if key == arcade.key.RIGHT:
			self.moveRight = True

	def on_key_release(self, key, key_modifiers):
		if key == arcade.key.LEFT:
			self.moveLeft = False
	
		if key == arcade.key.RIGHT:
			self.moveRight = False

		if key == arcade.key.SPACE:
			self.jumping = False

def main():
	game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
	game.setup()

	arcade.run()


if __name__ == "__main__":
	main()
