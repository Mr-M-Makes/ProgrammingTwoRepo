from pygame import image, transform
from directions import Direction


class Snake:
    """ Classes that manages the snake controlled by the player. """

    def __init__(self, x, y, segment_size):
        self.segment_size = segment_size
        self.segments = [Segment(x, y, (0, 1))]

        self.head = image.load("images/snake_head.png")
        self.body = image.load("images/snake_body.png")
        self.tail = image.load("images/snake_tail.png")

    def draw_snake(self, screen):
        """ Render snake to the screen. """
        for index, segment in enumerate(self.segments):
            if index == 0:
                if segment.direction == Direction.UP:
                    head = self.head
                elif segment.direction == Direction.DOWN:
                    head = transform.rotate(self.head, 180)
                elif segment.direction == Direction.RIGHT:
                    head = transform.rotate(self.head, 270)
                else:
                    head = transform.rotate(self.head, 90)                
                screen.blit(head, [segment.x, segment.y, self.segment_size, self.segment_size])
            elif index == len(self.segments) - 1:
                if segment.direction == Direction.UP:
                    tail = self.tail
                elif segment.direction == Direction.DOWN:
                    tail = transform.rotate(self.tail, 180)
                elif segment.direction == Direction.RIGHT:
                    tail = transform.rotate(self.tail, 270)
                else:
                    tail = transform.rotate(self.tail, 90)                
                screen.blit(tail, [segment.x, segment.y, self.segment_size, self.segment_size])
            else:
                if segment.direction == Direction.UP or segment.direction == Direction.DOWN:
                    body = self.body
                else:
                    body = transform.rotate(self.body, 90) 
                screen.blit(body, [segment.x, segment.y, self.segment_size, self.segment_size])

    def move_snake(self):
        """ Move each segment one size unit in its current direction and
        then update their current heading.
        """

        for segment in self.segments:
            segment.x += self.segment_size * segment.direction[0]
            segment.y += self.segment_size * segment.direction[1]
        
        self.update_segment_directions()

    def update_segment_directions(self):
        """ Update the direction of each segment, beyond the first, to the direction
        of the segment of the index before.
        """

        for segment_index in range(len(self.segments) - 1, 0, -1):
            segment_before = self.segments[segment_index - 1]
            new_direction = segment_before.direction
            self.segments[segment_index].direction = new_direction

    def add_segment(self):
        """ Add a new segment to the end of the snake. """

        last_segment = self.segments[-1]
        x_location = last_segment.x + self.segment_size * -last_segment.direction[0]
        y_location = last_segment.y + self.segment_size * -last_segment.direction[1]

        self.segments.append(Segment(x_location, y_location, last_segment.direction))

    def colliding_with_body(self):
        """ Check if the head of the snake is colliding with any segment in its body. """

        head_segment = self.segments[0]
        for index, body_segment in enumerate(self.segments):
            if index > 2 and head_segment.x == body_segment.x and head_segment.y == body_segment.y:
                return True
        return False

    def colliding_with_food(self, food):
        """ Check if the head of the snake is colliding with Food. """

        head_segment = self.segments[0]
        return head_segment.x == food.x and head_segment.y == food.y

    def colliding_with_walls(self, screen):
        """ Check if the head of the snake is colliding with the borders of the screen. """

        head_segment = self.segments[0]
        return head_segment.x < 0 or head_segment.x >= screen.get_width() or head_segment.y < 0 or head_segment.y >= screen.get_height()


class Segment:
    """ A class to represent a segment of the snake. """

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
