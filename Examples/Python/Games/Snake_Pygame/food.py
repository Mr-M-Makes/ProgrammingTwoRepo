from random import randrange
from pygame import image

class Food:
    """ Food object to be consumed by snake. """

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.egg = image.load("images/egg.png")


    def move_food_random(self, screen):
        """ Move food item at random location on screen. """

        self.x = randrange(0, int(screen.get_width()) - self.size, self.size)
        self.y = randrange(0, int(screen.get_height()) - self.size, self.size)

    
    def draw_food(self, screen):
        """ Render food to the screen. """

        screen.blit(self.egg, [self.x, self.y, self.size, self.size])

