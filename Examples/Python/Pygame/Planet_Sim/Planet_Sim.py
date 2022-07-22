import pygame as pg
from astropy.time import Time
from astroquery.jplhorizons import Horizons

class Color:
    Blue = (40,122,184)
    Font = (200, 255, 255)
    Background = (0,0,0)
    Sun = (249,215,28)

class Constants:
    AU = 149597870700

class SolarObject:
    def __init__(self, id, date, radius, color, mass, sun=False) -> None:
        
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = sun
        self.distance_to_sun = 0

        self.vectors = self.get_starting_vectors(id, date)
        self.x = self.vector["x"][-1]*Constants.AU

    def get_starting_vectors(self, id, date):
        tbd_time = Time(date).jd1
        obj = Horizons(id=id, location="@Sun", epochs = tbd_time)
        return obj.vectors()

    def 

def main():
    pg.init()
    win = pg.display.set_mode((600,600))
    pg.display.set_caption("Planet Sim")
    font = pg.font.SysFont("monospace", 40)
    clock = pg.time.Clock()
    start_date = "2022-07-22"
    elasped_time = 0

    sun = SolarObject("0", start_date, 30, Color.Sun, 1.98847*10**30, True)

    running = True
    while running:
        clock.tick(2)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        win.fill(Color.Background)
        elasped_time += 1
        label = font.render(f"Day: {elasped_time}", 1, Color.Font)
        win.blit(label, (10,10))
        pg.display.update()

main()