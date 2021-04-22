import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))


def redrawGameWindow():
    win.blit(bg, (0, 0))
    p1.draw(win)

    pygame.display.update()

p1 = player(200, 410, 64,64)
run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and p1.x > p1.vel:
        p1.x -= p1.vel
        p1.left = True
        p1.right = False

    elif keys[pygame.K_RIGHT] and p1.x < 500 - p1.vel - p1.width:
        p1.x += p1.vel
        p1.left = False
        p1.right = True

    else:
        p1.left = False
        p1.right = False
        p1.walkCount = 0

    if not (p1.isJump):
        if keys[pygame.K_SPACE]:
            p1.isJump = True
            p1.left = False
            p1.right = False
            p1.walkCount = 0
    else:
        if p1.jumpCount >= -10:
            p1.y -= (p1.jumpCount * abs(p1.jumpCount)) * 0.5
            p1.jumpCount -= 1
        else:
            p1.jumpCount = 10
            p1.isJump = False

    redrawGameWindow()

pygame.quit()