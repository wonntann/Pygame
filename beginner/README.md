## Steps
1. Initialize
* Setup the game window
* Change the title, logo and background color


2. Add images into the game
3. Player movements
    - Will move the player horizontally on the x-axis
    '''
     #move the player horizontally
     player_x += 0.05
    '''

4. Key controls for movement
    - first print it out
    '''
     #if keystroke is pressed check whether left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow pressed")
            if event.key == pygame.K_RIGHT:
                print("right arrow pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("released")
    '''

add the change in x to 0 and initialize the variable
stop in key up set change back to 0

Add boundaries for player to not go off the screen
calculate the edge

Create the enemy
Movement mechanics of the enemy
Add background image
Create image for shooting
Shooting multiple bullets at player
Setup collision detection
Create multiple enemies
Add text to display the score
**optional  add sounds and background music
Game Over
