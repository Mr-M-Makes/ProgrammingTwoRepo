import pygame as pg
import sys

from input_box import InputBox
from label import Label


def main():
    pg.init()
    pg.display.set_caption("Base Converter")

    screen_width = 450
    screen_height = 210

    screen = pg.display.set_mode((screen_width, screen_height))
    clock = pg.time.Clock()

    app_running = True
    gui_font = pg.font.SysFont("Console", 30)
    input_boxes = {}

    input_label_2 = Label(
        10, 10, 140, 41,
        pg.Color("grey"),
        pg.Color("white"),
        "Base 2:",
        gui_font,
        align="right"
    )
    input_box_2 = InputBox(
        150, 10, 290, 40,
        pg.Color("grey"),
        pg.Color("cyan"),
        gui_font,
        action=lambda: convert(input_boxes, "binary")
    )
    input_boxes["binary"] = input_box_2

    input_label_8 = Label(
        10, 60, 140, 41,
        pg.Color("grey"),
        pg.Color("white"),
        "Base 8:",
        gui_font,
        align="right"
    )
    input_box_8 = InputBox(
        150, 60, 290, 40,
        pg.Color("grey"),
        pg.Color("cyan"),
        gui_font,
        action=lambda: convert(input_boxes, "octal")
    )
    input_boxes["octal"] = input_box_8

    input_label_10 = Label(
        10, 110, 140, 41,
        pg.Color("grey"),
        pg.Color("white"),
        "Base 10:",
        gui_font,
        align="right"
    )
    input_box_10 = InputBox(
        150, 110, 290, 40,
        pg.Color("grey"),
        pg.Color("cyan"),
        gui_font,
        action=lambda: convert(input_boxes, "decimal")
    )
    input_boxes["decimal"] = input_box_10

    input_label_16 = Label(
        10, 160, 140, 41,
        pg.Color("grey"),
        pg.Color("white"),
        "Base 16:",
        gui_font,
        align="right"
    )
    input_box_16 = InputBox(
        150, 160, 290, 40,
        pg.Color("grey"),
        pg.Color("cyan"),
        gui_font,
        action=lambda: convert(input_boxes, "hexidecimal")
    )
    input_boxes["hexidecimal"] = input_box_16

    while app_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                app_running = False
            input_box_2.process_event(event)
            input_box_8.process_event(event)
            input_box_10.process_event(event)
            input_box_16.process_event(event)

        screen.fill(pg.Color("black"))
        input_label_2.draw(screen)
        input_box_2.draw(screen)
        input_label_8.draw(screen)
        input_box_8.draw(screen)
        input_label_10.draw(screen)
        input_box_10.draw(screen)
        input_label_16.draw(screen)
        input_box_16.draw(screen)

        pg.display.update()
        clock.tick(60)
        
    pg.quit()
    sys.exit()


def convert(input_boxes, system):
    """ Updates value in input box to all other input boxes in correct base system. """

    try:
        value = input_boxes[system].text

        # Convert value into decimal based on input base system
        if system == "binary":
            value = int(value, 2)
        elif system == "octal":
            value = int(value, 8)
        elif system == "decimal":
            value = int(value)
        elif system == "hexidecimal":
            value = int(value, 16)

        # Updates all other input box values to reflect current value
        for key in input_boxes:
            if key == "binary":
                input_boxes[key].text = bin(value)[2:]
            elif key == "octal":
                input_boxes[key].text = oct(value)[2:]
            elif key == "decimal":
                input_boxes[key].text = str(value)
            elif key == "hexidecimal":            
                input_boxes[key].text = hex(value)[2:]
    
    except ValueError:
        for input_box in input_boxes.values():
            input_box.text = "INVALID"


if __name__ == "__main__":
    main()
