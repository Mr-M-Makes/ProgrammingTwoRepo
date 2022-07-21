import pygame as pg


class InputBox:
    """ Allows user enter input into the program from the keyboard. """

    def __init__(
        self, 
        position_x,
        position_y,
        width,
        height,
        color,
        font_color,
        font,
        char_limit=14,
        action=None
    ):
        self.rect = pg.Rect(position_x, position_y, width, height)
        self.color = color
        self.inactive_color = color
        self.active_color = font_color
        self.text = ""
        self.font = font
        self.font_color = font_color
        self.rendered_text = None
        self.text_rect = pg.Rect(position_x, position_y, width, height)
        self.input_active = False
        self.char_limit = char_limit
        self.action = action
    
    def draw(self, screen):
        """ Draw the input box. """

        pg.draw.rect(screen, self.color, self.rect, 2)
        
        self.rendered_text = self.font.render(self.text, True, self.font_color)
        screen.blit(
            self.rendered_text,
            (self.text_rect.x + 5, self.text_rect.y)
        )

    def delete_char(self):
        """ Remove the last character entered into the input box. """

        self.text = self.text[:-1]

    def clear_text(self):
        """ Reset the text of the input box. """

        self.text = ""

    def add_char(self, char):
        """ Add a character to the input box.
        Does not accept alpha characters.
        """

        acceptable_chars = "box"
        if (not char.isalpha() or char in acceptable_chars) and len(self.text) < self.char_limit:
            self.text += char

    def process_event(self, event):
        """Process event to determine if the box should respond."""
        
        # Check for mouse events and respond accordingly.
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):            
                self.input_active = True
                self.color = self.active_color
                self.font_color = self.active_color
            else:
                self.input_active = False
                self.color = self.inactive_color
                self.font_color = self.inactive_color

        # Check for keydown events and respond accordingly.
        if event.type == pg.KEYDOWN and self.input_active:
            if event.key == pg.K_BACKSPACE:
                self.delete_char()
            elif event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                self.input_active = False
                if self.action != None:
                    self.action()
            else:
                self.add_char(event.unicode)
