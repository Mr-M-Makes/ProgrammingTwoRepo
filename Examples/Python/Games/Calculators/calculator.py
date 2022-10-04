import pygame as pg
import sys

from button import Button
from input_box import InputBox
from label import Label


def main():
    pg.init()
    pg.display.set_caption("Base Calculator")

    screen_width = 400
    screen_height = 160

    screen = pg.display.set_mode((screen_width, screen_height))
    clock = pg.time.Clock()

    app_running = True
    gui_font = pg.font.SysFont("Console", 30)

    input_label = Label(
        10, 10, 120, 41,
        pg.Color("grey"),
        pg.Color("white"),
        "Input:",
        gui_font,
        align="right"
    )
    input_box = InputBox(
        130, 10, 260, 40,
        pg.Color("grey"),
        pg.Color("cyan"),
        gui_font,
        acceptable_chars="box"
    )

    output_label = Label(
        10, 110, 380, 40,
        pg.Color("grey"),
        pg.Color("white"),
        "",
        gui_font,
        align="center",
        border=2
    )
    calculate_button = Button(
        10, 60, 380, 40,
        pg.Color("grey"),
        pg.Color("white"),
        "CALCULATE",
        gui_font,
        action=lambda: calculate(input_box, output_label)
    )

    # Images
    bg_image = pg.image.load("images/background.png")

    while app_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                app_running = False
            input_box.process_event(event)

        screen.fill(pg.Color("black"))
        screen.blit(bg_image, (0, 0))
        input_label.draw(screen)
        input_box.draw(screen)
        calculate_button.draw(screen)
        output_label.draw(screen)

        pg.display.update()
        clock.tick(60)
        
    pg.quit()
    sys.exit()


def calculate(input_box, output_label):
    """ Calculates and displayes the result of the entered expression. """
    # potential security issue: eval() ex. eval(pythong code)
    # validating input in input_box.add_char()
    try:
        result = eval(input_box.text)
    except ZeroDivisionError:
        result = "Divide by Zero Error"
    except SyntaxError:
        result = "Invalid Expression"
    except NameError:  # For base calc upgrade "box" and eval no variable
        result = "Invalid Expression"

    output_label.update_text(str(result))
    input_box.clear_text()

if __name__ == "__main__":
    main()
