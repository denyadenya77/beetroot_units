# Создать экран
# Создать и отобразить прямоугольник произвольной величины
# Двигать объект прямоугольника если пользователь нажмет кнопку вверх/вниз/влево/вправо
import pygame


class Display:

    BLACK = (0, 0, 0)

    def __init__(self):
        self.display = pygame.display.set_mode((720, 480))
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.display.fill(display.BLACK)


class Ball:

    def __init__(self):
        self.ball = pygame.image.load('intro_ball.gif')
        self.ballrect = pygame.Rect(self.ball.get_rect())


class Game:

    @staticmethod
    def run(display, ball):
        while True:
            pygame.init()
            display.clock.tick(display.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        ball.ballrect.move_ip(0, -10)
                    elif event.key == pygame.K_DOWN:
                        ball.ballrect.move_ip(0, 10)
                    elif event.key == pygame.K_LEFT:
                        ball.ballrect.move_ip(-10, 0)
                    elif event.key == pygame.K_RIGHT:
                        ball.ballrect.move_ip(10, 0)


            display.display.blit(ball.ball, ball.ballrect)
            pygame.display.update()


if __name__ == '__main__':
    display = Display()
    ball = Ball()

    Game.run(display, ball)
