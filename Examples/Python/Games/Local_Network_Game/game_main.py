import pygame as pg
import sys
from network import Network

from player import Player


def main():
    pg.init()
    width = 500
    height = 500
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Client")
    clock = pg.time.Clock()
    network = Network()
    start_pos = read_pos(network.get_pos())
    player = Player(start_pos[0], start_pos[1], 100, 100, pg.Color("green"))
    player2 = Player(0, 0, 100, 100, pg.Color("green"))

    game_running = True

    while game_running:
        player2_pos = read_pos(network.send(make_pos((player.x, player.y))))
        player2.x = player2_pos[0]
        player2.y = player2_pos[1]
        player2.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

        player.move()

        screen.fill(pg.Color("black"))
        player.draw(screen)
        player2.draw(screen)

        pg.display.update()
        clock.tick(60)

    pg.quit()
    sys.exit()


def read_pos(data):
    data = data.split(",")
    return int(data[0]), int(data[1])


def make_pos(position):
    return f"{position[0]},{position[1]}"


if __name__ == "__main__":
    main()