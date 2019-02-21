class Snake:
    length = 1
    x = [0]
    y = [0]

    def __init__(self, x, y, blockSize):
        self.x[0] = x
        self.y[0] = y
        self.blockSize = blockSize
        self.direction = 0

    def update(self):
        # update body
        if self.length != len(self.x):
            for i in range(self.length - len(self.x)):
                self.x.append(self.x[0])
                self.y.append(self.y[0])
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head
        if self.direction == 0:
            self.x[0] += self.blockSize
        elif self.direction == 1:
            self.x[0] -= self.blockSize
        elif self.direction == 2:
            self.y[0] -= self.blockSize
        elif self.direction == 3:
            self.y[0] += self.blockSize

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def grow(self):
        self.length += 1

    def draw(self, display, image):
        for i in range(self.length):
            display.blit(image, (self.x[i], self.y[i]))
