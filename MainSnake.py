import pygame, sys, snake, food
from pygame.locals import *

size = 400

pygame.init()
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Snake")
fpsClock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)

fps = 5
scale = 20
maxSeg = ((size / scale) * (size / scale)) - 1
end = False
win = False
playing = False
restartDisplay = font.render("Press any key to restart", False, (255, 255, 255))
winDisplay = font.render("You Win!", False, (255, 255, 255))

snake = snake.Snake(screen, scale, playing)
food = food.Food(screen, scale, snake)

food.newPos()

while True:
    if food.xpos == snake.xpos and food.ypos == snake.ypos: #changes the position of the food if it spawns on top of the snake
        food.newPos()
    else:
        for i in range(snake.seg):
            if food.xpos == snake.xSegments[i] and food.ypos == snake.ySegments[i]:
                food.newPos()

    if snake.seg == maxSeg:
        print(True)
        win = True
        end = True

    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if end: #resets the game if player has lost, and has pressed a key
                snake.xpos = 200
                snake.ypos = 200
                snake.direction = 0
                snake.seg = 2
                snake.xSegments = [180, 180]
                snake.ySegments = [200, 180]
                food.newPos()

                end = False
            elif playing == False:
                playing = True
                snake.playing = True
            else:
                snake.keyDown(event.key)

    snake.show()
    food.show()
    if playing:
        snake.move(size)
        snake.eat(food)

    for i in range(snake.seg): #checks if the snake has hit itself
        if snake.xpos == snake.xSegments[i] and snake.ypos == snake.ySegments[i] and playing:
            if i != 1:
                end = True
            else:
                if snake.direction == 1: #helps fight a glitch where the snake can go backwards if player spams keys
                    snake.direction = 3
                    snake.xpos += scale
                elif snake.direction == 2:
                    snake.direction = 4
                    snake.ypos += scale
                elif snake.direction == 3:
                    snake.direction = 1
                    snake.xpos -= scale
                elif snake.direction == 4:
                    snake.direction = 2
                    snake.ypos -= scale

    if end and not win: #shows death screen
        screen.fill((255, 0, 0))
        screen.blit(restartDisplay, (43, 180))
    elif end and win:
        screen.fill((255, 150, 0))
        screen.blit(winDisplay, (140, 160))
        screen.blit(restartDisplay, (43, 195))
    
    pygame.display.update()
    fpsClock.tick(fps)

