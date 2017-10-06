import pygame, food

class Snake(object):
    xpos = 200
    ypos = 200
    direction = 3 #0-null, 1-left, 2-up, 3-right, 4-down
    seg = 2

    xSegments = [180, 180]
    ySegments = [200, 180]

    def __init__(self, screen, scale, playing):
        self.screen = screen
        self.scale = scale
        self.playing = playing

    def show(self): #function for showing snake, and moving the segments forward
        pygame.draw.rect(self.screen, (0, 0, 0), (self.xpos, self.ypos, self.scale, self.scale))
        if self.direction == 1:
            pygame.draw.rect(self.screen, (255, 255, 255), (self.xpos + 1, self.ypos + 1, 2, 2))
            pygame.draw.rect(self.screen, (255, 255, 255), (self.xpos + 1, self.ypos + self.scale - 3, 2, 2))
        elif self.direction == 2:
            pygame.draw.rect(self.screen, (255, 255, 255), (self.xpos + 1, self.ypos + 1, 2, 2))
            pygame.draw.rect(self.screen, (255, 255,255), (self.xpos + self.scale - 3, self.ypos + 1, 2, 2))
        elif self.direction == 3 or self.direction == 0:
            pygame.draw.rect(self.screen, (255, 255, 255), (self.xpos + self.scale - 3, self.ypos + 1, 2, 2))
            pygame.draw.rect(self.screen, (255, 255, 255), (self.xpos + self.scale - 3, self.ypos + self.scale - 3, 2, 2))
        elif self.direction == 4:
            pygame.draw.rect(self.screen, (255, 255, 255), (self.xpos + self.scale - 3, self.ypos + self.scale - 3, 2, 2))
            pygame.draw.rect(self.screen, (255, 255, 255), (self.xpos + 1, self.ypos + self.scale - 3, 2, 2))

        for i in reversed(range(self.seg)): #reversed to prevent segment stacking
            pygame.draw.rect(self.screen, (0, 0, 0), (self.xSegments[i], self.ySegments[i], self.scale, self.scale))
            if self.direction > 0 and self.playing: #stops the segments from updating when the snake isn't moving
                if i > 0:
                    self.xSegments[i] = self.xSegments[i - 1] #updates segment to be in the same place as the one in front of it
                    self.ySegments[i] = self.ySegments[i - 1]
                else:
                    self.xSegments[i] = self.xpos
                    self.ySegments[i] = self.ypos

    def move(self, size): #function for moving the front of the snake
        if self.direction == 1 and self.xpos > 0:
            self.xpos -= self.scale
        elif self.direction == 2 and self.ypos > 0:
            self.ypos -= self.scale
        elif self.direction == 3 and self.xpos < size - self.scale:
            self.xpos += self.scale
        elif self.direction == 4 and self.ypos < size - self.scale:
            self.ypos += self.scale

    def keyDown(self, key): #function for changing direction when an arrow key is pressed
        if key == pygame.K_LEFT and self.direction != 3:
            self.direction = 1
        elif key == pygame.K_UP and self.direction != 4:
            self.direction = 2
        elif key == pygame.K_RIGHT and self.direction != 1:
            self.direction = 3
        elif key == pygame.K_DOWN and self.direction != 2:
            self.direction = 4

    def eat(self, food): #function for telling if the snake ate something
        if self.xpos == food.xpos and self.ypos == food.ypos:
            food.newPos()
            self.seg += 1
            self.xSegments.append(-self.scale) #uses the value -scale to prevent showing a rectangle in the middle of the screen
            self.ySegments.append(-self.scale)
            print(self.seg)