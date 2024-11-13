import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # set the containers
    Player.containers = (updatable, drawable)

    # then create the player
    player = Player(player_x, player_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        # update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60))/1000



if __name__ == "__main__":
    main()
