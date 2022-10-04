import pygame as pg


class Button:
    """Class to creat a button for the program."""

    def __init__(
        self,
        position_x,
        position_y,
        width,
        height,
        color,
        text_color,
        text,
        font,
        action=lambda: None
    ):

        self.rect = pg.Rect(position_x, position_y, width, height)
        self.color = color
        self.text_color = text_color
        self.action = action
        self.text = font.render(text, True, text_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.font = font
        self.pressed = False
        self.elevation = 6
        self.dynamic_elevation = self.elevation
        self.original_y_pos = position_y
        self.bottom_rect = pg.Rect(
            position_x,
            position_y,
            width,
            self.elevation
        )

    def draw(self, screen):
        """Draw the button to the screen and check if button is clicked.
        Checking for the button being clicked allows for the click animation.
        """

        self.rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.rect.center

        self.bottom_rect.midtop = self.rect.midtop
        self.bottom_rect.height = self.rect.height + self.dynamic_elevation

        pg.draw.rect(
            screen,
            pg.Color("darkgrey"),
            self.bottom_rect,
            border_radius=12
        )
        pg.draw.rect(screen, self.color, self.rect, border_radius=12)
        screen.blit(self.text, self.text_rect)
        self.check_if_clicked()

    def check_if_clicked(self):
        """Check if the button has been clicked."""

        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    self.action()
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation

    def update_text(self, text):
        """ Changes the displayed text of the button. """   

        self.text = self.font.render(text, True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)
