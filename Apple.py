class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, display, image):
        display.blit(image, (self.x, self.y))
