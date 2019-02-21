import pygame
import time
class Game:
    pause = False
    def Collision(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return True

    def Lost(self, blockSize, display):
        print("You Lost")
        font = pygame.font.SysFont("Times New Roman", 72)
        text = font.render("You Lost", True, (255, 255, 255))
        display.blit(text, (blockSize * 25 - 72 * 2, blockSize * 15 - 72))
        pygame.display.flip()

    def Pause(self):
        self.pause = not self.pause
        print("Game Paused (Press R to resume)")
        while (self.pause):
            for event in pygame.event.get():
                if event.key == pygame.K_r:
                    print("Resume Game")
                    self.pause = False

    def Restart(self):
        restart = True
        self.pause = not self.pause
        print("Game Ended (Press R to restart / Q to end)")
        while (self.pause):
            for event in pygame.event.get():
                if event.key == pygame.K_r:
                    print("Game Restarted")
                    self.pause = False
                    return restart == True
                elif event.key == pygame.K_q:
                    print("Quit Game")
                    return restart == False
    def wallCollision(self, x1, y1, length, weight):
	if x1 <= -1 or x1 >= weight or y1 <= -1 or y1 >= length:
	    return True

