import pygame, random

class Food(object):

    xpos = 40
    ypos = 200

    foodImg = pygame.image.load('banana.png')

    def __init__(self, screen, scale, snake):
        self.screen = screen
        self.scale = scale
        self.snake = snake

        self.foodImg = pygame.transform.scale(self.foodImg, (scale, scale)) #changes the size of the image to fit onto the grid

    def show(self): #function for displaying food
        self.screen.blit(self.foodImg, (self.xpos, self.ypos))

    def newPos(self): #function for moving the food to a new position
        self.xpos = random.randint(0, 380)
        self.ypos = random.randint(0, 380)

        self.checkPos()

    def checkPos(self): #function for making the position fit on the grid
        if self.xpos % self.scale != 0:
            while self.xpos % self.scale != 0:
                self.xpos -= 1

        if self.ypos % self.scale != 0:
            while self.ypos % self.scale != 0:
                self.ypos -= 1