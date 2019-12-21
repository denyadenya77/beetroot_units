import pygame, random

class Round:

    def __init__(self):
        self.round = None


    def create_round_1(self):
        round = []
        level = 1
        while len(round) < 10:
            block_x = 0
            block_y = 0
            round