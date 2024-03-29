import pygame as pg
from pygame.locals import K_LEFT, K_RIGHT, K_SPACE
from math import cos, sin, atan, radians, degrees
from os import getcwd

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Breakout!")

    

    paddle = pg.image.load("Examples/Python/Pygame/Basic_Practice/images/paddle.png")
    paddle = paddle.convert_alpha()
    paddle_rect = paddle.get_rect()
    paddle_rect.top = screen.get_height() - paddle.get_height() - 10
    paddle_rect.left = (screen.get_width() - paddle.get_width()) / 2
    paddle_speed = 0.5

    ball = pg.image.load("Examples/Python/Pygame/Basic_Practice/images/football.png")
    ball = ball.convert_alpha()
    ball_rect = ball.get_rect()
    ball_launched = False
    ball_speed = 10
    ball_motion_angle = 60
    ball_motion = calculate_motion_vector_components(ball_motion_angle, ball_speed)
    ball_rect.topleft = (paddle_rect.left + (paddle_rect.width - ball_rect.width) / 2, paddle_rect.top - ball_rect.height)
    ball_last_pos = ball_rect.topleft




    clock = pg.time.Clock()
    game_over = False

    while not game_over:
        dt = clock.tick(50)
        screen.fill((0, 0, 0))


        screen.blit(paddle, paddle_rect)
        screen.blit(ball, ball_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True

        pressed = pg.key.get_pressed()
        if pressed[K_SPACE]:
            ball_launched = True
        if pressed[K_LEFT]:
            paddle_rect.left -= paddle_speed * dt
        if pressed[K_RIGHT]:
            paddle_rect.left += paddle_speed * dt
        
        if paddle_rect.left > screen.get_width() - paddle_rect.width:
            paddle_rect.left = screen.get_width() - paddle_rect.width
        if paddle_rect.left < 0:
            paddle_rect.left = 0

        if ball_launched:
            ball_rect.left += ball_motion[0]
            ball_rect.top += ball_motion[1]

            # Ball collision with paddle
            if collide_with_paddle(ball_rect, paddle_rect):
                ball_motion[1] *= -1
                ball_rect.top = paddle_rect.top - ball_rect.height
                continue

    

            # Ball collision with sides
            if ball_rect.left < 0:
                ball_motion[0] *= -1
                ball_rect.left = 0
            elif ball_rect.left > screen.get_width() - ball_rect.width:
                ball_motion[0] *= -1
                ball_rect.left = screen.get_width() - ball_rect.width
            if ball_rect.top < 0:
                ball_motion[1] *= -1
                ball_rect.top = 0
            elif ball_rect.top > screen.get_height() - ball_rect.height:
                ball_launched = False

            ball_last_pos = ball_rect
        else:
            ball_rect.topleft = (paddle_rect.left + (paddle_rect.width - ball_rect.width) / 2, paddle_rect.top - ball_rect.height) 

        pg.display.update()
    
    pg.quit()





def collide_with_paddle(ball, paddle):
    if paddle.left < ball.left < paddle.right or paddle.left < ball.right < paddle.right:
        if ball.bottom >= paddle.top:
            return True
    return False


def calculate_motion_vector_components(angle, speed):
    angle = radians(angle)
    x_motion = cos(angle) * speed
    y_motion = sin(angle) * speed

    return [x_motion, -y_motion]


if __name__ == "__main__":
    main()