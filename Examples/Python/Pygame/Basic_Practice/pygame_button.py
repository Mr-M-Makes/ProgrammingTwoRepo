import pygame as pg

def main():
    pg.init()
    screen = pg.display.set_mode((500, 500), 0, 32)

    pg.display.set_caption("Hello Button")

    # Button setup
    text_color = (255, 255, 255)
    button_color = (120, 120, 120)
    button_over_color = (200, 200, 200)
    button_width = 100
    button_height = 50
    button_rect = [
        (screen.get_width() - button_width) / 2, 
        (screen.get_height() - button_height) / 2, 
        button_width, button_height
    ]

    button_font = pg.font.SysFont("Arial", 20)
    button_text = button_font.render("Quit", True, text_color)
    screen.fill((100, 100, 100))

    game_over = False
    x, y = 0, 0

    while not game_over:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button_rect[0] <= x <= button_rect[0] + button_rect[2] and button_rect[1] <= y <= button_rect[1] + button_rect[3]:
                    game_over = True
            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
        
        if button_rect[0] <= x <= button_rect[0] + button_rect[2] and button_rect[1] <= y <= button_rect[1] + button_rect[3]:
            pg.draw.rect(screen, button_over_color, button_rect)
        else:
            pg.draw.rect(screen, button_color, button_rect)

        screen.blit(button_text, 
            (
                button_rect[0] + (button_width - button_text.get_width()) / 2, 
                button_rect[1] + (button_height - button_text.get_height()) / 2,
            )
        )
        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()

