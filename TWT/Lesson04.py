# Optimization And OOP - Object Oriented Programming
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

    def draw(self, win):

        if self.walkCount + 1 >= 27:
            self.walkCount = 0
            
        if self.left:  
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1                          
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))
            walkCount = 0

# Global Variables to the class player
# x = 50
# y = 400
# width = 40
# height = 60
# vel = 5
# isJump = False
# jumpCount = 10
# left = False
# right = False
# walkCount = 0



def redrawGameWindow():
    # global walkCount ### this is in player class now
    
    win.blit(bg, (0,0))  

    # step 2 clean up 
    # move this as a method of class player 
    man.draw(win)
    # if walkCount + 1 >= 27:
    #     walkCount = 0
        
    # if left:  
    #     win.blit(walkLeft[walkCount//3], (x,y))
    #     walkCount += 1                          
    # elif right:
    #     win.blit(walkRight[walkCount//3], (x,y))
    #     walkCount += 1
    # else:
    #     win.blit(char, (x, y))
    #     walkCount = 0
        
    pygame.display.update() 
    

# alot of mods add man in front of all player attributes to link to player class
# step 1 clean up
# mainloop
# spawn our player
man = player(300, 410, 64, 64) # size of sprint is 64, 64
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and man.x > man.vel:  
        man.x -= man.vel
        man.left = True
        man.right = False

    elif keys[pygame.K_RIGHT] and man.x < 500 - man.vel - man.width:  
        man.x += man.vel
        man.left = False
        man.right = True
        
    else: 
        man.left = False
        man.right = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
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