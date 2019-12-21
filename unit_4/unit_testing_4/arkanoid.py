import pygame, random


class Round:

    def __init__(self):
        self.set = None

    def create_first_round(self):
        round = []
        y = 0
        level = 1
        while level is not 4:
            if level % 2 == 0:
                list_of_x = list(range(60, 600, 120))
                for x in list_of_x:
                    new_block_pos = (x, y)
                    round.append(new_block_pos)
                y += 40
                level += 1
            else:
                list_of_x = list(range(0, 600, 120))
                for x in list_of_x:
                    new_block_pos = (x, y)
                    round.append(new_block_pos)
                y += 40
                level += 1
        self.set = round

    def create_second_round(self):
        round = []
        y = 0
        level = 1
        while level is not 6:
            if level % 2 == 0:
                list_of_x = list(range(60, 600, 120))
                for x in list_of_x:
                    new_block_pos = (x, y)
                    round.append(new_block_pos)
                y += 40
                level += 1
            else:
                list_of_x = list(range(0, 600, 120))
                for x in list_of_x:
                    new_block_pos = (x, y)
                    round.append(new_block_pos)
                y += 40
                level += 1
        self.set = round

    def create_third_round(self):
        round = []
        y = 0
        level = 1
        while level is not 6:
            list_of_x = list(range(0, 600, 60))
            for x in list_of_x:
                new_block_pos = (x, y)
                round.append(new_block_pos)
            y += 40
            level += 1
        self.set = round

    def del_block(self, block):
        for in_block in self.set:
            if in_block[0] == block[0] and in_block[1] == block[1]:
                self.set.remove(in_block)

    def check_ball_contact(self, ball):
        for block in self.set:
            if ball.ball_y + ball.ball_radius == block[1] + 40 and ball.ball_x in range(block[0], block[0] + 60) and ball.ball_direction == 'move_up_and_left':
                ball.ball_direction = 'move_down_and_left'
                self.del_block(block)
            elif ball.ball_y + ball.ball_radius == block[1] + 40 and ball.ball_x in range(block[0], block[0] + 60) and ball.ball_direction == 'move_up_and_right':
                ball.ball_direction = 'move_down_and_right'
                self.del_block(block)

            elif ball.ball_x + ball.ball_radius == block[0] and ball.ball_y in range(block[1], block[1] + 40) and ball.ball_direction is 'move_up_and_right':
                ball.ball_direction = 'move_up_and_left'
                self.del_block(block)
            elif ball.ball_x + ball.ball_radius == block[0] + 60 and ball.ball_y in range(block[1], block[1] + 40) and ball.ball_direction is 'move_up_and_left':
                ball.ball_direction = 'move_up_and_right'
                self.del_block(block)

            elif ball.ball_x + ball.ball_radius == block[0] and ball.ball_y in range(block[1], block[1] + 40) and ball.ball_direction is 'move_down_and_right':
                ball.ball_direction = 'move_down_and_left'
                self.del_block(block)
            elif ball.ball_x + ball.ball_radius == block[0] + 60 and ball.ball_y in range(block[1], block[1] + 40) and ball.ball_direction is 'move_down_and_left':
                ball.ball_direction = 'move_down_and_right'
                self.del_block(block)

            elif ball.ball_y + ball.ball_radius == block[1] and ball.ball_x in range(block[0], block[0] + 60) and ball.ball_direction is 'move_down_and_right':
                ball.ball_direction = 'move_up_and_right'
                self.del_block(block)
            elif ball.ball_y + ball.ball_radius == block[1] and ball.ball_x in range(block[0], block[0] + 60) and ball.ball_direction is 'move_down_and_left':
                ball.ball_direction = 'move_up_and_left'
                self.del_block(block)



class Paddle:

    def __init__(self):
        self.paddle_x = 280
        self.paddle_y = 790
        self.paddle_width = 60
        self.paddle_height = 10
        self.paddle_speed = 10
        self.collor = (255, 255, 255)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle_x = self.paddle_x - self.paddle_speed
        elif keys[pygame.K_RIGHT]:
            self.paddle_x = self.paddle_x + self.paddle_speed

    def check_screen_borders(self, screen_width):
        if self.paddle_x < 0:
            self.paddle_x = 0
        if self.paddle_x + self.paddle_width > screen_width:
            self.paddle_x = screen_width - self.paddle_width


class Ball:

    def __init__(self):
        self.ball_x = 200
        self.ball_y = 300
        self.ball_radius = 5
        self.ball_speed = 5
        self.color = (255, 255, 255)
        self.ball_direction = random.choice(['move_up_and_left', 'move_down_and_right',
                                             'move_up_and_right', 'move_down_and_left'])

    def move(self):
        if self.ball_direction is 'move_up_and_left':
            self.ball_x = self.ball_x - self.ball_speed
            self.ball_y = self.ball_y - self.ball_speed
        elif self.ball_direction is 'move_down_and_right':
            self.ball_x = self.ball_x + self.ball_speed
            self.ball_y = self.ball_y + self.ball_speed
        elif self.ball_direction is 'move_up_and_right':
            self.ball_x = self.ball_x + self.ball_speed
            self.ball_y = self.ball_y - self.ball_speed
        elif self.ball_direction is 'move_down_and_left':
            self.ball_x = self.ball_x - self.ball_speed
            self.ball_y = self.ball_y + self.ball_speed

    def check_screen_borders(self, screen_width):
        if self.ball_x - self.ball_radius <= 0 and self.ball_direction is 'move_up_and_left':
            self.ball_direction = 'move_up_and_right'
        elif self.ball_x - self.ball_radius <= 0 and self.ball_direction is 'move_down_and_left':
            self.ball_direction = 'move_down_and_right'
        elif self.ball_y - self.ball_radius <= 0 and self.ball_direction is 'move_up_and_right':
            self.ball_direction = 'move_down_and_right'
        elif self.ball_y - self.ball_radius <= 0 and self.ball_direction is 'move_up_and_left':
            self.ball_direction = 'move_down_and_left'
        elif self.ball_x + self.ball_radius >= screen_width and self.ball_direction is 'move_down_and_right':
            self.ball_direction = 'move_down_and_left'
        elif self.ball_x + self.ball_radius >= screen_width and self.ball_direction is 'move_up_and_right':
            self.ball_direction = 'move_up_and_left'

    def check_paddle_hit(self, paddle):
        if self.ball_y + self.ball_radius == paddle.paddle_y and self.ball_x in range(paddle.paddle_x, paddle.paddle_x + paddle.paddle_width) and \
                self.ball_direction is 'move_down_and_right':
            self.ball_direction = 'move_up_and_right'
        elif self.ball_y + self.ball_radius == paddle.paddle_y and self.ball_x in range(paddle.paddle_x, paddle.paddle_x + paddle.paddle_width) and \
                self.ball_direction is 'move_down_and_left':
            self.ball_direction = 'move_up_and_left'


class Game:

    def run(self, round, paddle, ball):

        SCREEN_WIDTH = 600
        SCREEN_HIGHT = 800

        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))

        # current_round = 1
        round.create_third_round()

        while True:
            pygame.time.delay(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()


            round.check_ball_contact(ball)

            ball.check_screen_borders(SCREEN_WIDTH)
            ball.move()
            ball.check_paddle_hit(paddle)

            paddle.move()
            paddle.check_screen_borders(SCREEN_WIDTH)


            screen.fill((0, 0, 0))

            for block in round.set:
                pygame.draw.rect(screen, (255, 255, 255), (block[0], block[1], 60, 40))
                pygame.draw.rect(screen, (230, 230, 230), (block[0] + 1, block[1] + 1, 58, 38))

            pygame.draw.rect(screen, paddle.collor, (paddle.paddle_x, paddle.paddle_y, paddle.paddle_width, paddle.paddle_height))
            pygame.draw.circle(screen, ball.color, (ball.ball_x, ball.ball_y), ball.ball_radius)
            pygame.display.update()



if __name__ == '__main__':
    paddle = Paddle()
    ball = Ball()
    this_round = Round()
    game = Game()
    game.run(this_round, paddle, ball)

