from tela import Tela
import numpy as np
import peca as pecas
import os
from readchar import readkey, key


tetrominos = [pecas.I, pecas.J, pecas.L, pecas.O, pecas.S, pecas.T, pecas.Z]


class Partida:

    def __init__(self, player, rows, cols):
        self.screen = Tela(rows, cols)
        self.current_tetromino = np.random.choice(tetrominos)(0, cols // 2)
        self.is_game_complete = False
        self.current_tetromino
        self.score = 0

    def new_tetromino(self):
        tetromino = np.random.choice(tetrominos)(0, self.screen.cols // 2)
        return tetromino

    def end_game_instance(self):
        self.is_game_complete = True

    def full_line_check(self):
        lines_removed = 0
        for i, row in enumerate(self.screen.grid):
            if (row == "").sum() == 0:
                self.screen.remove_row(i)
                lines_removed += 1
        # TODO implement the amount of score
        self.score += lines_removed

    def rotate_clockwise(self):
        self.current_tetromino.rotate_clockwise()
        if not self.current_tetromino.is_inside_screen(
            self.screen
        ) or self.current_tetromino.is_collided(self.screen):
            self.current_tetromino.rotate_anticlockwise()

    def rotate_anticlockwise(self):
        self.current_tetromino.rotate_anticlockwise()
        if not self.current_tetromino.is_inside_screen(
            self.screen
        ) or self.current_tetromino.is_collided(self.screen):
            self.current_tetromino.rotate_clockwise()

    def move_left(self):
        self._move_tetromino(0, -1)

    def move_right(self):
        self._move_tetromino(0, 1)

    def move_down(self):
        self._move_tetromino(1, 0)

    def _move_tetromino(self, dy, dx):
        self.current_tetromino.update_position(dy, dx)

        if not self.current_tetromino.is_inside_screen(self.screen):
            self.current_tetromino.update_position(-dy, -dx)

        elif self.current_tetromino.is_collided(self.screen):
            self.current_tetromino.update_position(-dy, -dx)
            self.screen.draw_tetromino(self.current_tetromino)
            self.current_tetromino = self.new_tetromino()
            if self.current_tetromino.is_collided(self.screen):
                ## Caso o novo  tetromino apareça em um local já utilizado por outros tetrominos, então a partida é encerrada.
                self.end_game_instance()
