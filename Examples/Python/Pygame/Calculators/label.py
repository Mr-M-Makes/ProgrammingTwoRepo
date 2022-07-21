import pygame as pg


class Label:
    """ Class for creating a label to display text in the program. """

    def __init__(
        self, 
        position_x,
        position_y,
        width,
        height,
        color,
        text_color,
        text, font,
        align="left",
        border=0
    ):
        self.rect = pg.Rect(position_x, position_y, width, height)
        self.color = color
        self.text_color = text_color
        self.font = font
        self.text = font.render(text, True, text_color)
        self.border = border
        self.align = align

        if self.align == "right":
            self.text_rect = self.text.get_rect(
                right=self.rect.right,
                centery=self.rect.centery
            )
        elif self.align == "center":
            self.text_rect = self.text.get_rect(center=self.rect.center)
        else:
            self.text_rect = self.text.get_rect(
                x=self.rect.x,
                centery=self.rect.centery
            )

    def draw(self, screen):
        """ Draw the label to the screen. """

        pg.draw.rect(screen, self.color, self.rect, self.border)
        screen.blit(self.text, self.text_rect)

    def update_text(self, text):
        """ Change the text displayed by the label. """

        self.text = self.font.render(text, True, self.text_color)
        if self.align == "center":
            self.text_rect = self.text.get_rect(center=self.rect.center)
