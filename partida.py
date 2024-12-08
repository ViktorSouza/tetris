from tela import Tela
import numpy as np
import peca as pecas
import os
from readchar import readkey, key


tetrominos = [pecas.I, pecas.J, pecas.L, pecas.O, pecas.S, pecas.T, pecas.Z]


class Partida:
    def __init__(self, player, rows, cols):
        self.screen = Tela(rows, cols)
        self.current_tetromino = np.random.choice(tetrominos)(2, 2)
        self.current_tetromino

    def new_tetromino(self):
        tetromino = np.random.choice(tetrominos)(2, 2)
        return tetromino

    def start(self):
        while True:
            tecla = readkey()

            self.screen.remove_tetromino(self.current_tetromino)
            updated_position = [0, 0]

            if tecla == key.LEFT:
                updated_position = [0, -1]
            elif tecla == key.RIGHT:
                updated_position = [0, 1]
            elif tecla == key.DOWN:
                updated_position = [1, 0]
            elif tecla == key.PAGE_DOWN:
                self.current_tetromino.rotate_left()
            elif tecla == key.PAGE_UP:
                self.current_tetromino.rotate_right()

            self.current_tetromino.update_position(
                updated_position[0], updated_position[1]
            )

            if not self.current_tetromino.is_tetromino_inside_border(self.screen):
                self.current_tetromino.update_position(
                    -updated_position[0], -updated_position[1]
                )

            elif self.current_tetromino.is_tetromino_collided(self.screen):
                self.current_tetromino.update_position(
                    -updated_position[0], -updated_position[1]
                )
                self.screen.draw_tetromino(self.current_tetromino)
                self.current_tetromino = self.new_tetromino()

            self.screen.draw_tetromino(self.current_tetromino)
            os.system("cls||clear")
            self.screen.show_screen()
