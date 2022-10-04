# My cool program
import pygame as pg
import sys

from sorter import Sorter
from game_settings import GameSettings
from gui import GUI
from background_scroller import Background


def main():
    pg.init()
    pg.display.set_caption("Visual Sorter")

    settings = GameSettings()
    sorter = Sorter(settings)
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    clock = pg.time.Clock()
    bg = Background("images/space_bg.png", 0, 1, settings)
    # bg = Background("images/background.png", 1, 1, settings)
    # bg = Background("images/test_bg.png", 1, -1, settings)

    gui = GUI(settings, screen, sorter)

    app_running = True

    while app_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                app_running = False
            gui.gui_elements[8].process_event(event)
        
        screen.fill(pg.Color("black"))
        bg.draw(screen)

        for gui_element in gui.gui_elements:
            gui_element.draw(screen)

        if sorter.sorting:
            for sort in sorter.sorts:
                if sort.sorting:
                    sort.sorting = next(sort.generator)
        sort_row = 1
        for sort in sorter.sorts:
            sort.draw(
                screen,
                settings.window_padding * 2 + settings.button_width,
                settings.window_padding + (settings.value_vertical_padding + settings.value_height) * sort_row,
                settings.value_horizontal_padding
            )
            sort_row += 1
        
        pg.display.update()
        clock.tick(settings.sort_speed)
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
