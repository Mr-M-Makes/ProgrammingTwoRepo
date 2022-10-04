# Simple pygame program

# Import and initialize the pygame library
import pygame

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
# Setup the window we'll use for drawing
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Poop(pygame.sprite.Sprite):
    def __init__(self):
        super(Poop, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(player_pos)
        )

clock = pygame.time.Clock()
# Run until the user asks us to quit
list_of_poop = pygame.sprite.Group()
count = 0
running = True
player = Player()
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                player_pos = player.rect.topleft
                new_poop = Poop()
                list_of_poop.add(new_poop)
                new_poop = 0
            
    # Fill the background with white
    screen.fill((10, 20, 30))

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    for poops in list_of_poop:
        screen.blit(poops.surf, poops.rect)
    screen.blit(player.surf,player.rect)
    # Flip the display
    pygame.display.flip()
        # Ensure we maintain a 30 frames per second rate
    clock.tick(30)


# We're done, so we can quit now.
pygame.quit()
