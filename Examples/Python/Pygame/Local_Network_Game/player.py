import pygame as pg

from network import Network


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.velocity = 3

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.x -= self.velocity
        if keys[pg.K_RIGHT]:
            self.x += self.velocity
        if keys[pg.K_UP]:
            self.y -= self.velocity
        if keys[pg.K_DOWN]:
            self.y += self.velocity

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)