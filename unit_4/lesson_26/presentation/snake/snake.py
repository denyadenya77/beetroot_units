import pygame, random


class Snake:

    list_of_directions = ['UP', 'DOWN', 'RIGHT', 'LEFT']

    def __init__(self):
        self.body = [[500, 500], [520, 500], [540, 500]]  # [x, y]
        self.direction = 'UP'


    def move_up(self):
        new_head = self.body.pop()
        old_head_x = self.body[0][0]
        old_head_y = self.body[0][1]

        new_head[0] = old_head_x
        new_head[1] = old_head_y - 20
        self.body.insert(0, new_head)

    def move_down(self):
        new_head = self.body.pop()
        old_head_x = self.body[0][0]
        old_head_y = self.body[0][1]

        new_head[0] = old_head_x
        new_head[1] = old_head_y + 20
        self.body.insert(0, new_head)

    def move_right(self):
        new_head = self.body.pop()
        old_head_x = self.body[0][0]
        old_head_y = self.body[0][1]

        new_head[0] = old_head_x + 20
        new_head[1] = old_head_y
        self.body.insert(0, new_head)

    def move_left(self):
        new_head = self.body.pop()
        old_head_x = self.body[0][0]
        old_head_y = self.body[0][1]

        new_head[0] = old_head_x - 20
        new_head[1] = old_head_y
        self.body.insert(0, new_head)

    def add_tail(self):
        """to do before move method"""
        old_tail = self.body[-1]
        new_tail = old_tail
        self.body.append(new_tail)


class Apple:

    @staticmethod
    def get_new_position():
        x = random.randrange(0, 500, 20)
        y = random.randrange(0, 500, 20)
        return [x, y]


class Game:

    def run(self, snake, apple):
        pygame.init()
        screen = pygame.display.set_mode((1000, 1000))
        # pygame.time.delay(1)

        apple_position = apple.get_new_position()

        while True:

            # quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # stop game
            for elem in snake.body[1:]:
                if snake.body[0] == elem:
                    break

            # apple eating
            if snake.body[0] == apple_position:
                snake.add_tail()
                apple_position = apple.get_new_position()

            # moving
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and snake.direction is not 'DOWN':
                snake.move_up()
                snake.direction = 'UP'
            elif keys[pygame.K_DOWN] and snake.direction is not 'UP':
                snake.move_down()
                snake.direction = 'DOWN'
            elif keys[pygame.K_RIGHT] and snake.direction is not 'LEFT':
                snake.move_right()
                snake.direction = 'RIGHT'
            elif keys[pygame.K_LEFT] and snake.direction is not 'RIGHT':
                snake.move_left()
                snake.direction = 'LEFT'

            print(snake.body)

            # redraw
            screen.fill((0, 0, 0))
            for elem in snake.body:
                pygame.draw.rect(screen, (255, 255, 255), (elem[0], elem[1], 20, 20))
            pygame.draw.rect(screen, (255, 255, 255), (apple_position[0], apple_position[1], 20, 20))
            pygame.display.update()


if __name__ == '__main__':
    snake = Snake()
    apple = Apple()
    game = Game()

    game.run(snake, apple)




