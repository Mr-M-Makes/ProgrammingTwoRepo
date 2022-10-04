
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()
screen = pygame.display.set_mode((100,100))
store = {}
eventlister = {}
newdict = {"key":"value"}
while True:
    for eve in pygame.event.get():
        #print(eve)
        if eve.type == KEYDOWN:
            print(eve)
            store = eve.__dict__
            eventlister.update(store)
            print(eventlister["unicode"]," = ", eventlister["key"])
            store = {eventlister["unicode"]:eventlister["key"]}
            newdict.update({eventlister["unicode"]:eventlister["key"]})
            print(newdict)


