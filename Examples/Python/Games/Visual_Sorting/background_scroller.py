import pygame as pg
import math
import random


class Background:
    """Class that creates a seamless background scrolling effect."""

    def __init__(self, image, dir_x, dir_y, settings):        
        self.settings = settings
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.background = pg.image.load(image)
        self.tile_rect = self.background.get_rect()
        self.bg_tiles = []
        self.generate_background_tiles()

    def draw(self, screen):
        """ Draw the background to the screen. """
        
        for tile in self.bg_tiles:
            if self.dir_x > 0 and tile[0] > self.settings.screen_width:
                tile[0] = -self.tile_rect.width
            elif self.dir_x < 0 and tile[0] < -self.tile_rect.width:
                tile[0] = self.settings.screen_width
            else:
                tile[0] += self.dir_x

            if self.dir_y > 0 and tile[1] > self.settings.screen_height:
                tile[1] = -self.tile_rect.height
            elif self.dir_y < 0 and tile[1] < -self.tile_rect.height:
                tile[1] = self.settings.screen_height
            else:
                tile[1] += self.dir_y

            screen.blit(self.background, tile)

    def generate_background_tiles(self):
        """Generate background tiles to cover entire screen area."""

        self.bg_tiles.clear()
        self.number_of_tiles_y = math.ceil(self.settings.screen_height / self.tile_rect.height) + 1
        self.number_of_tiles_x = math.ceil(self.settings.screen_width / self.tile_rect.width) + 1

        for row_i in range(self.number_of_tiles_y):
            for column_i in range(self.number_of_tiles_x):
                tile = self.tile_rect[:]
                tile[0] = column_i * tile[2]
                tile[1] = row_i * tile[3]
                self.bg_tiles.append(tile)
