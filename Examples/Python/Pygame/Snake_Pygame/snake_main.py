import pygame as pg
import sys

from game_manager import GameManager
from snake import Snake
from food import Food
from directions import Direction


def main():
    pg.init()
    pg.display.set_caption("Snake")
    
    game_manager = GameManager(pg.time.Clock())
    screen = pg.display.set_mode((game_manager.window_width, game_manager.window_height))

    # Music
    pg.mixer.music.load("audio/tranquil.ogg")
    pg.mixer.music.set_volume(.1)
    pg.mixer.music.play(-1)

    # Game Running Loop
    while game_manager.game_running:
        menu_loop(screen, game_manager)
        game_loop(screen, game_manager)
        game_over_loop(screen, game_manager)

    pg.quit()
    sys.exit()


def menu_loop(screen, game_manager):
    """ Loop that is executed when game is started or after the game over screen. """
    
    main_menu = pg.image.load("images/main_menu.png")

    while game_manager.in_main_menu:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_manager.game_running = False
                game_manager.in_main_menu = False
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                game_manager.in_main_menu = False
                game_manager.playing_game = True
        
        screen.blit(main_menu, (0, 0))

        text_to_be_displayed = [
            "Hello and welcome to the game Snake!",
            "Move the snake with the ARROW keys.",
            "Collect food without collided with the",
            "snakes body or the edges of the screen.",
            "Press 'ENTER' to play the game."
        ]
        display_text(text_to_be_displayed, game_manager, screen, pg.Color("white"), (45, 312))

        pg.display.update()

def game_loop(screen, game_manager):
    """ Loop for when the player is playing and controlling the snake. """
    
    background = pg.image.load("images/background.png")
    snake = Snake(game_manager.window_width / 2, game_manager.window_height / 2, game_manager.segment_size)
    snake.add_segment()
    food = Food(0, 0, game_manager.segment_size)
    food.move_food_random(screen)
    gulp_sound = pg.mixer.Sound("audio/gulp.wav")

    while game_manager.playing_game:
        game_manager.clock.tick(game_manager.game_speed)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_manager.game_running = False
                game_manager.playing_game = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and snake.segments[0].direction != Direction.DOWN:
                    snake.segments[0].direction = Direction.UP                    
                if event.key == pg.K_DOWN and snake.segments[0].direction != Direction.UP:
                    snake.segments[0].direction = Direction.DOWN
                if event.key == pg.K_RIGHT and snake.segments[0].direction != Direction.LEFT:
                    snake.segments[0].direction = Direction.RIGHT
                if event.key == pg.K_LEFT and snake.segments[0].direction != Direction.RIGHT:
                    snake.segments[0].direction = Direction.LEFT
        
        screen.blit(background, (0, 0))
        snake.move_snake()
        
        if snake.colliding_with_body() or snake.colliding_with_walls(screen):
            game_manager.playing_game = False
            game_manager.game_over_screen = True
        elif snake.colliding_with_food(food):
            pg.mixer.Sound.play(gulp_sound)
            snake.add_segment()
            food.move_food_random(screen)

        food.draw_food(screen)
        snake.draw_snake(screen)
        pg.display.update()


def game_over_loop(screen, game_manager):
    """ Loop for the game over screen. """
    
    game_over_menu = pg.image.load("images/game_over.png")

    while game_manager.game_over_screen:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_manager.game_running = False
                game_manager.game_over_screen = False
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                game_manager.game_over_screen = False
                game_manager.in_main_menu = True
        
        screen.blit(game_over_menu, (0, 0))

        text_to_be_displayed = ["", "GAME OVER! Thanks for playing!", "Press 'ENTER' to go to the main menu."]
        display_text(text_to_be_displayed, game_manager, screen, pg.Color("white"), (45, 312))

        pg.display.update()


def display_text(lines_of_text, game_manager, screen, color, position):
    """ Displays a list text to the screen. """

    button_font = pg.font.SysFont("Console", 12)
    for line_number, line_text in enumerate(lines_of_text):
        text = button_font.render(line_text, True, color)
        screen.blit(text, (position[0], position[1] + line_number * 13, game_manager.window_width - 10, game_manager.window_width - 10))


if __name__ == "__main__":
    main()