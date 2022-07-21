import pygame as pg
from shapes import Column, Left_L, Right_L, T, Square

def main():
    pg.init()
    screen = pg.display.set_mode((500, 620))
    pg.display.set_caption("Tetris")

    grid_size = 30
    columns = screen.get_width() // grid_size
    rows = screen.get_height() // grid_size    
    row_padding = (screen.get_width() - columns * grid_size) // 2
    column_padding = (screen.get_height() - rows * grid_size) // 2

    game_over = False
    block = Left_L(0 + row_padding, 0 + column_padding, grid_size)
    clock = pg.time.Clock()
    fps = 5

    while not game_over:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                if not block.colliding_with_left_side(row_padding):
                    block.move_horizontal(-1 * grid_size)
            if event.key == pg.K_RIGHT:
                if not block.colliding_with_right_side(screen.get_width() - row_padding):
                    block.move_horizontal(grid_size)
        
        screen.fill((0, 0, 0))

        draw_grid(rows, columns, screen, grid_size, row_padding, column_padding)
        block.draw_shape(screen)
        if not block.colliding_with_bottom(screen.get_height() - column_padding):
            block.move_down(grid_size)

        pg.display.update()

    pg.quit()

def draw_grid(rows, columns, screen, grid_size, row_padding, column_padding):

    for y in range(rows):
        for x in range(columns):
            pg.draw.rect(screen, (100, 100, 100), [x * grid_size + row_padding, y * grid_size + column_padding, grid_size, grid_size], 1)


if __name__ == "__main__":
    main()