import pygame as pg
from astropy.time import Time
from astroquery.jplhorizons import Horizons

class Color:
    Blue = (40,122,184)
    Font = (200, 255, 255)
    Background = (0,0,0)
    Sun = (249,215,28)
    Grey = (50,50,50)

class Constants:
    AU = 149597870700
    G = 6.6743e-11
    TIMESTEP = 3600*24
    
    WIDTH = 600
    HEIGHT = 600
    EDGE = 4
    SCALE = WIDTH / 2 / EDGE / AU

class SolarObject:
    def __init__(self, id, date, radius, color, mass, sun=False) -> None:
        
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = sun
        self.distance_to_sun = 0

        self.vectors = self.get_starting_vectors(id, date)
        self.x = self.vectors["x"][-1]*Constants.AU
        self.y = self.vectors["y"][-1] * Constants.AU # meters
        self.x_vel = self.vectors["vx"][-1] * Constants.AU / 24 / 3600 # m/s
        self.y_vel = self.vectors["vy"][-1] * Constants.AU / 24 / 3600 # m/s

    def get_starting_vectors(self, id, date):
        tbd_time = Time(date).jd1
        obj = Horizons(id=id, location="@Sun", epochs = tbd_time)
        return obj.vectors()

    def draw(self, win):
        x = self.x * Constants.SCALE + Constants.WIDTH / 2
        y = self.y * Constants.SCALE + Constants.HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                point_x, point_y = point
                point_x = point_x * Constants.SCALE + Constants.WIDTH / 2
                point_y = point_y * Constants.SCALE + Constants.HEIGHT / 2
                updated_points.append((point_x, point_y))

            pg.draw.lines(win, self.color, False, updated_points, 1)

        pg.draw.circle(win, self.color, (x, y), self.radius / Constants.EDGE)


def main():
    pg.init()
    win = pg.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pg.display.set_caption("Planet Sim")
    font = pg.font.SysFont("monospace", 40)
    clock = pg.time.Clock()
    start_date = "2022-07-22"
    elasped_time = 0

    sun = SolarObject("0", start_date, 30, Color.Sun, 1.98847*10**30, True)
    Merc = SolarObject("1", start_date, 7, Color.Grey, 3.285*10**23, True)

    objects = [sun,Merc]
    running = True
    while running:
        clock.tick(100)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        win.fill(Color.Background)
        elasped_time += 1
        label = font.render(f"Day: {elasped_time}", 1, Color.Font)
        win.blit(label, (10,10))
        for o in objects:
            o.draw(win)
       # sun.draw(win)
        #Merc.draw(win)
        pg.display.update()

main()