import pygame as pg
from pygame.constants import K_SPACE
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE

pg.init()
width = 800
height = 600
screen = pg.display.set_mode((width, height), 0, 32)
clock = pg.time.Clock()

sprite_bug = pg.image.load("images/butterfly.png")
bug_size = 32
sprite_bug = pg.transform.scale(sprite_bug, (bug_size, bug_size))
bug_x, bug_y = 0, 0
bug_speed = 0.5

game_over = False

pg.display.set_caption("Practice")
screen.fill((0, 0, 0))

while not game_over:
    dt = clock.tick(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        elif event.type == pg.MOUSEMOTION:
            bug_x = event.pos[0] - bug_size / 2
            bug_y = event.pos[1] - bug_size / 2
    pressed = pg.key.get_pressed()
    if pressed[K_UP]:
        bug_y -= bug_speed * dt
    if pressed[K_DOWN]:
        bug_y += bug_speed * dt
    if pressed[K_LEFT]:
        bug_x -= bug_speed * dt
    if pressed[K_RIGHT]:
        bug_x += bug_speed * dt
    if pressed[K_SPACE]:
        bug_x = 0
        bug_y = 0

    if bug_x > width - bug_size:
        bug_x = width - bug_size
    if bug_x < 0:
        bug_x = 0
    if bug_y > height - bug_size:
        bug_y = height - bug_size
    if bug_y < 0:
       bug_y = 0


    screen.fill((0, 0, 0))
    screen.blit(sprite_bug, (bug_x, bug_y))
    pg.display.update()


pg.quit()