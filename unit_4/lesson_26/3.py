# Написать игру Bounce

import pygame


class Display:

    BLACK = (0, 0, 0)

    def __init__(self):
        self.display = pygame.display.set_mode((720, 480))
        self.clock = pygame.time.Clock()
        self.FPS = 60


class Paddle:

    WHITE = (255, 255, 255)

    def __init__(self):
        self.rect = pygame.Rect((0, 0), (32, 32))
        self.image = pygame.Surface((32, 32))

        self.image.fill(self.WHITE)
