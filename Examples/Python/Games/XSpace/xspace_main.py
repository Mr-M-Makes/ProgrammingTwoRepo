import pygame as pg
import sys

from game_settings import Settings


def main():
    pg.init()
    pg.display.set_caption("Project X-Space")

    settings = Settings()    
    screen = pg.display.set_mode((settings.window_width, settings.window_height))
    clock = pg.time.Clock()

    game_running = True

    level_map = [
        'XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X               XXXX      X',
        'X      P                  X',
        'X     XXXXXX              X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'X                         X',
        'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ]

    tile_size = 30
    tiles = []

    for row_index, row in enumerate(level_map):
        for col_index, cell in enumerate(row):
            x = col_index * tile_size
            y = row_index * tile_size

            if cell == "X":
                tiles.append([x, y, tile_size, tile_size])

    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

        screen.fill(pg.Color("black"))

        for tile in tiles:            
                pg.draw.rect(screen, pg.Color("white"), tile)
        pg.display.update()

    pg.quit()
    sys.exit()
    


if __name__ == "__main__":
    main()