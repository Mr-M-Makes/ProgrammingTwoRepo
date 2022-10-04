from numpy import rot90
from pygame import draw


class Segment:
    """ Creates a square segment of a shape. """

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size


    def move_down(self, amount):
        self.y += amount

    
    def move_horizontal(self, amount):
        self.x += amount


    def draw_segment(self, screen):
        draw.rect(screen, (255, 255, 255), [self.x, self.y, self.size - 2, self.size - 2])

    
    def get_position(self):
        return self.x, self.y


class Block:
    """Creates a block for the Tetris game.

    Different Block Types:\n
    \t-Column Shape = 0\n
    \t-Backward L Shape = 1\n
    \t-L Shape = 2\n
    \t-Short T Shape = 3\n
    \t-Square Shape = 4  
    """

    # List of blocks
    # 0 - Column, 1 - Backward L, 2 - L, 3 - T, 4 - Square    
    blocks = [
        [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 1, 1], [0, 1, 0], [0, 1, 0]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
        [[1, 1], [1, 1]]
    ]

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.shape = []


    def move_down(self, speed):
        for row in self.shape:
            for segment in row:
                if segment != None:
                    segment.move_down(speed)

    
    def move_horizontal(self, speed):
        for row in self.shape:
            for segment in row:
                if segment != None:
                    segment.move_horizontal(speed)

    
    def rotate_left(self):
        self.shape = rot90(self.shape).tolist()

    
    def rotate_right(self):
        self.shape = rot90(self.shape, axes=(1,0)).tolist()

    
    def shape(self):
        return self.shape

    
    def draw_shape(self, screen):
        for row in self.shape:
            for segment in row:
                if segment != None:
                    segment.draw_segment(screen)


    def colliding_with_bottom(self, bottom):
        for row in self.shape:
            for segment in row:
                if segment != None:
                    if segment.get_position()[1] + self.size>= bottom:
                        return True
        return False


    def colliding_with_right_side(self, right_side):
        for row in self.shape:
            for segment in row:
                if segment != None:
                    if segment.get_position()[0] + self.size >= right_side:
                        return True
        return False

    def colliding_with_left_side(self, left_side):
        for row in self.shape:
            for segment in row:
                if segment != None:
                    if segment.get_position()[0] <= left_side:
                        return True
        return False


class Column(Block):
    def __init__(self, x, y, size):
        Block.__init__(self, x, y, size)
        self.shape = [
            [None, Segment(self.x + self.size, self.y, self.size), None], 
            [None, Segment(self.x + self.size, self.y + self.size, self.size), None], 
            [None, Segment(self.x + self.size, self.y + self.size * 2, self.size), None]
        ]

class Left_L(Block):
    def __init__(self, x, y, size):
        Block.__init__(self, x, y, size)
        self.shape = [
            [None, Segment(self.x + self.size, self.y, self.size), Segment(self.x + self.size * 2, self.y, self.size)], 
            [None, Segment(self.x + self.size, self.y + self.size, self.size), None], 
            [None, Segment(self.x + self.size, self.y + self.size * 2, self.size), None]
        ]


class Right_L(Block):
    def __init__(self, x, y, size):
        Block.__init__(self, x, y, size)
        self.shape = [
            [Segment(self.x, self.y, self.size), Segment(self.x + self.size, self.y, self.size), None], 
            [None, Segment(self.x + self.size, self.y + self.size, self.size), None], 
            [None, Segment(self.x + self.size, self.y + self.size * 2, self.size), None]
        ]


class T(Block):
    def __init__(self, x, y, size):
        Block.__init__(self, x, y, size)
        self.shape = [
            [Segment(self.x, self.y, self.size), Segment(self.x + self.size, self.y, self.size), Segment(self.x + self.size * 2, self.y, self.size)], 
            [None, Segment(self.x + self.size, self.y + self.size, self.size), None], 
            [None, None, None]
        ]


class Square(Block):
    def __init__(self, x, y, size):
        Block.__init__(self, x, y, size)
        self.shape = [
            [Segment(self.x, self.y, self.size), Segment(self.x + self.size, self.y, self.size), None], 
            [Segment(self.x, self.y + self.size, self.size), Segment(self.x + self.size, self.y + self.size, self.size), None], 
            [None, None, None]
        ]

