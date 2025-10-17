import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init() #Initializes all pygame modules

    # Displaying a GUI window
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    # screen is an instance of Surface type
    # Pygame draws everything on a surface

    # Pygame clock object : to track time
    clock = pygame.time.Clock()
    dt = 0 # delta : amt of time till last variable was drawn

    # creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Adding Classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Player Object
    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    # Game Loop
    while True:
        # for closing the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black") # color the "screen" instance fully black 
        

        for d in drawable:
            d.draw(screen) # render player shape on screen
        
        
        updatable.update(dt) # check for any user input and update acc
        pygame.display.flip() # update the full display surface

        # Pausing game for 1/60 of a second
        dt = clock.tick(60) / 1000 # returns the amt of time since it was last called in miliseconds



if __name__ == "__main__":
    main()
