import pygame

pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Change the name")


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), 
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), 
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), 
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


clock = pygame.time.Clock()

# Create a class with all attritubutes for our player
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        ## L5-03
        self.standing = True

    def draw(self, win):

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        ##L5-04
        if not(self.standing):

        # tab this in    
            if self.left:  
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1                          
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            # win.blit(char, (self.x, self.y))
            # walkCount = 0
            ## L5-02
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

## L5-01
# new class for the projectile or bullet
class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

# L06-01
# new class for our enemy
class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), 
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), 
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), 
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3
    
    def draw(self, win):
        pass

    def move(self):
        pass

########5:47


    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def redrawGameWindow():
    # global walkCount ### this is in player class now
    
    win.blit(bg, (0,0))  

    man.draw(win)

    ##L05-12 draw bullets
    for bullet in bullets:
        bullet.draw(win)         
    pygame.display.update() 
    


# mainloop
# spawn our player
man = player(300, 410, 64, 64) # size of sprint is 64, 64

## L05-08
bullets = []

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ## L05-09
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))



    keys = pygame.key.get_pressed()
    
    ## L05-11
    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 100:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height //2), 6, (255, 10, 1), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:  
        man.x -= man.vel
        man.left = True
        man.right = False
        ## L5-05
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < 500 - man.vel - man.width:  
        man.x += man.vel
        man.left = False
        man.right = True
        ## L5-06
        man.standing = False
    else: 
        #L5-07
        man.standing = True
        # man.left = False
        # man.right = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:   ##L05-10 Change jump from SPACE to UP arrow
            man.isJump = True
            man.left = False
            man.right = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
            man.jumpCount -= 1
        else: 
            man.jumpCount = 10
            man.isJump = False

    redrawGameWindow() 
    
    
pygame.quit()