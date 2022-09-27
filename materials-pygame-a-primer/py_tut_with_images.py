# Import the pygame module
import pygame
import time
# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
# from pygame.locals import *
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
# Setup for sounds, defaults are good
pygame.mixer.init()

# Initialize pygame
pygame.init()

font = pygame.font.SysFont("Helvetica", 24)
dead_font = pygame.font.SysFont("ariel", 72)
# Define constants for the screen width and height

size = pygame.display.get_desktop_sizes()

SCREEN_WIDTH = size[0][0]-50
SCREEN_HEIGHT = size[0][1]-100


# Define the Player object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("super.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
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


# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(slow, fast//40)

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()




# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create custom events for adding a new enemy and cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Create our 'player'
player = Player()

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites isused for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load and play our background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)

# Load all our sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")

# Set the base volume for all sounds
move_up_sound.set_volume(0.5)
move_down_sound.set_volume(0.5)
collision_sound.set_volume(0.5)

# Variable to keep our main loop running
running = True
score = 0
lives = 3
slow = 1
fast=40
# Our main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

        # Should we add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy, and add it to our sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Should we add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud, and add it to our sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update the position of our enemies and clouds
    enemies.update()
    clouds.update()

    # Fill the screen with sky blue
    screen.fill((135, 206, 250))

    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    #lives
    if lives >0:
        life1 = pygame.image.load("super.png").convert_alpha()
        
        life1_rect = life1.get_rect()
        screen.blit(life1, (105,5))
    if lives >1:
        life2 = pygame.image.load("super.png").convert_alpha()
        life2.set_colorkey((0, 0, 0), RLEACCEL)
        life2_rect = life2.get_rect()
        screen.blit(life2, (205,5))
    if lives >2:
        life3 = pygame.image.load("super.png").convert_alpha()
        life3.set_colorkey((255, 255, 255), RLEACCEL)
        life3_rect = life3.get_rect()
        screen.blit(life3, (305,5))

    #score
    score_display = (("Score: ") + str(score))
    img = font.render(score_display, True, (100,100, 255))
    rect = img.get_rect()
    pygame.draw.rect(img,(150,200,255),rect,1)
    screen.blit(img, (((SCREEN_WIDTH/2)+5),0))
    fast +=1


    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, remove the player
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()
        player.kill()
        screen.fill((255,255,255))
        you_died = "You Are Dead !"
        minus50 = "Lose 100 Points !"
        died = font.render(you_died, True, (0,0,0))
        minus = font.render(minus50, True, (0,0,0))
        
        screen.blit(died, (((SCREEN_WIDTH/2)-35),((SCREEN_HEIGHT/2)-20)))
        screen.blit(minus, (((SCREEN_WIDTH/2)-35),((SCREEN_HEIGHT/2)+20)))
        pygame.display.flip()
     
        time.sleep(1)   

        fast = 80

        score = score - 100
        if score <0:
            score = 0
        # Stop any moving sounds and play the collision sound
        if lives > 1:
            lives -=1
        else:
            dead = "Game Over"
            screen.fill((255,255,255))
            pygame.display.flip()

            GO = font.render(dead, True, (0,0,0))
            screen.blit(GO, (((SCREEN_WIDTH/2)-35),((SCREEN_HEIGHT/2)-20)))
            pygame.display.flip()
            time.sleep(2)
            running = False

        # Stop the loop
        #running = False
        screen.fill((135, 206, 250))
        player = Player()
        all_sprites.add(player)
        pygame.display.flip()
        continue



    # Flip everything to the display
    pygame.display.flip()
    score += 1
    # Ensure we maintain a 30 frames per second rate
    clock.tick(30)

# At this point, we're done, so we can stop and quit the mixer
pygame.mixer.music.stop()
pygame.mixer.quit()
