import pygame

# initialize pygame
pygame.init()

#  pygame screen
screen = pygame.display.set_mode((800, 600))

# title and Icon window
# image 32 x 32 PNG
# icons made by https://www.freepik.com from https://www.flaticon.com/
pygame.display.set_caption("Space Invaders")
game_icon = pygame.image.load("title.png")
pygame.display.set_icon(game_icon)


# player
player_img = pygame.image.load('ship.png')
# half of width/height + edge room
player_x = 370
player_y = 460
# variable for change in x
player_x_change = 0

# draw the image using parameters
def player(x, y):
    screen.blit(player_img, (x, y))

# main game loop
running = True
# will continue running while set to True
# exit when set to False
while running:
    # screen color (rgb) with tuple
    # https://www.w3schools.com/colors/colors_picker.asp
    screen.fill((255, 204, 204))

    # loop through all events occurring in main window
    for event in pygame.event.get():
        # check if close button has been pressed
        if event.type == pygame.QUIT:
            running = False
    
        # if keystroke is pressed check whether left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
        if event.type == pygame.KEYUP:
            # action when player stops moving
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # player change in x
    player_x += player_x_change
    # call player
    player(player_x, player_y)

    # update game window
    pygame.display.update()