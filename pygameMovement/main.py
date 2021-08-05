import pygame

# initialize pygame
pygame.init()

# display pygame window width and height; tuple
win = pygame.display.set_mode((500, 500))

# display caption
pygame.display.set_caption("First Game")

# 3. add screen width
screenWidth = 500

x = 50
y = 50
width = 40
height = 50
vel = 20

# 5. jumping
isJump = False
jumpCount = 10

run = True
# main loop check for collision
while run:
    pygame.time.delay(100)             # delay in milliseconds

    for event in pygame.event.get():
        # 1. check if click exit button
        if event.type == pygame.QUIT:
            run = False

    # 3. key pressed 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:    # add 2nd condition to not go off screen
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width:        # screen width - the character width
        x += vel
    # 5. jumping
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenWidth - vel:
            y += vel
        if keys[pygame.K_SPACE]:        # 5. jumping
            isJump = True
    else:   # 5. jumping
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # 4. draw over the rectangles once move
    win.fill((0,0,0))

    # 2. draw shape; parameter ==> ((surface, color, rect)
    pygame.draw.rect(win, (233, 255, 0), (x, y, width, height))
    pygame.display.update()


pygame.quit()