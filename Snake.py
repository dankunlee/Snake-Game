import pygame
import time
from pygame.locals import *
from random import randint
from Apple import Apple
from Player import Snake
from Game import Game

class App:
    def __init__(self):
        self._running = True
        self._display = None
        self._appleImage = None
        self.gameSpeed = 0.12  # smaller value corresponds to faster speed
        self.blockSize = 15  # pixel size: (0 to blockSize-1) by (0 to blockSize-1)
        self.size = self.weight, self.height = self.blockSize * 50, self.blockSize * 30  # window pixel size: (0,0) is the top left starting point
        self.reset()

    def reset(self):
        self._apple = Apple(self.blockSize * randint(1, self.weight // self.blockSize - 1), # column 0 is reserved for snake's starting point
                            self.blockSize * randint(0, self.height // self.blockSize - 1))
        self._snake = Snake(0, self.blockSize * randint(0, self.height // self.blockSize - 1), self.blockSize)
        self._snake.length = 1
        self._game = Game()

    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Snake")
        self._running = True
        self._appleImage = pygame.image.load("apple.png").convert()
        self._appleImage = pygame.transform.scale(self._appleImage, (self.blockSize, self.blockSize))
        self._snakeImage = pygame.image.load("snake.png").convert()
        self._snakeImage = pygame.transform.scale(self._snakeImage, (self.blockSize, self.blockSize))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self._snake.update()
        # when the snake eats the apple
        if self._game.Collision(self._apple.x, self._apple.y, self._snake.x[0], self._snake.y[0]):
            self._apple.x = self.blockSize * randint(0, self.weight // self.blockSize - 1)  # random apple x point
            self._apple.y = self.blockSize * randint(0, self.height // self.blockSize - 1)  # random apple y point
            self._snake.grow()
            self._snake.update()
        for i in range(1, self._snake.length):
            if self._game.Collision(self._snake.x[i], self._snake.y[i], self._snake.x[0], self._snake.y[0]) or \
                    self._game.Collision(-15, 15, self._snake.x[0], self._snake.y[0]):
                self._game.Lost(self.blockSize, self._display)
                if self._game.Restart() == False:
                    self._running = False
                else: #restart the game (initialize all parameters)
                    self.reset()

    def on_render(self):
        self._display.fill((0, 0, 0))  # empty(initialize) the screen
        self._apple.draw(self._display, self._appleImage)
        self._snake.draw(self._display, self._snakeImage)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while (self._running):
            ##          keys = pygame.key.get_pressed() #get keys that are currently pressed down
            for event in pygame.event.get():
                self.on_event(event)
                if (event.type == pygame.KEYDOWN):  # get which keys were pressed down on that frame
                    if event.key == pygame.K_RIGHT:
                        self._snake.moveRight()
                        print("Right")
                    if event.key == pygame.K_LEFT:
                        self._snake.moveLeft()
                        print("Left")
                    if event.key == pygame.K_UP:
                        self._snake.moveUp()
                        print("Up")
                    if event.key == pygame.K_DOWN:
                        self._snake.moveDown()
                        print("Down")
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        self._running = False
                    if event.key == pygame.K_p:
                        self._game.Pause()
            self.on_loop()
            self.on_render()
            time.sleep(self.gameSpeed)  # speed of the game
        self.on_cleanup()

if __name__ == "__main__":
    app = App()
    app.on_execute()
