import pygame as pg

_ = False
mapalevel2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Classrooms:
    def __init__(self, game):
        self.game = game
        self.mapalevel2 = mapalevel2
        self.world_map = {}
        self.rows = len(self.mapalevel2)
        self.cols = len(self.mapalevel2[0])
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mapalevel2):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]