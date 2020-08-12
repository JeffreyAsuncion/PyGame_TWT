# Jumping and Boundaries
import pygame


# start pygame module
pygame.init()

# make a window
SCREEN_WIDTH = 1000 
SCREEN_HEIGHT = 1000 ## describe top left corner 0,0 and bottom right 500, 500
win = pygame.display.set_mode((SCREEN_WIDTH, 
                               SCREEN_HEIGHT))

pygame.time.delay(100)
pygame.display.set_caption("First Game")

x = 500 #Spawn character
y = 500
width = 40 # size of character
height = 60
vel = 10 # speed of character
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0 

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel: # add and
        x -= vel
    if keys[pygame.K_RIGHT] and (x < (SCREEN_WIDTH-(width + vel))): # add and
        x += vel
    
    
    if not(isJump):
        #TAKE AWAY ABILITY TO WALK UP AND DOWN
        # if keys[pygame.K_UP] and y > vel: # add and
        #     y -= vel
        # if keys[pygame.K_DOWN] and (y < (SCREEN_HEIGHT-(height + vel))):
        #     y += vel
        ###
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            #####
            neg = 1
            if jumpCount < 0:
                neg = -1
            #####
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10




    # this cleans up after the Character
    win.fill((0, 0, 0))

    # Draw our character
    pygame.draw.rect(win, (255, 0, 0), (x, y , width, height) )
    # win = where do you want to draw this rect()
    # (255, 0, 0) = RBG color 
    # (x, y , width, height) = rectangle attributes
    pygame.display.update()



pygame.quit()