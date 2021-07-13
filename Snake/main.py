import pygame

class Cube(object):
    def __init__(self,position):
        pass

class Snake(object):
    body = []
    turns = {}
    def __init__(self,color,pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dx = 0
        self.dy = 1
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dx = -1
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]
                elif keys[pygame.K_RIGHT]:
                    self.dx = 1
                    self.dy = 0
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]
                elif keys[pygame.K_UP]:
                    self.dx = 0
                    self.dy = 1
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]
                elif keys[pygame.K_DOWN]:
                    self.dx = 0
                    self.dy = -1
                    self.turns[self.head.pos[:]] = [self.dx, self.dy]

def drawGrid(w,rows,surface):
    n = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x += n
        y += n
        pygame.draw.line(surface,(255,255,255),(x,0),(x,w))
        pygame.draw.line(surface,(255,255,255),(0,y),(w,y))
    pass

def reDrawWindow(surface):
    global len, rows, win
    surface.fill((0,0,0))
    drawGrid(len,rows,surface)
    pygame.display.update()

len = 500
rows = 20
wn = pygame.display.set_mode((len,len))
snake = Snake((255,0,0),(10,10))
isPlaying = True
clock = pygame.time.Clock()
while isPlaying:
    pygame.time.delay(50)
    clock.tick(10)
    reDrawWindow(wn)




