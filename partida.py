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
        self.score = 0

    def new_tetromino(self):
        tetromino = np.random.choice(tetrominos)(2, 2)
        return tetromino

    def start(self):
        while True:
            tecla = readkey()

            self.screen.remove_tetromino(self.current_tetromino)
            updated_position = [0, 0]
            old_blocks = self.current_tetromino.get_blocks()

            if tecla == key.LEFT:
                updated_position = [0, -1]
            elif tecla == key.RIGHT:
                updated_position = [0, 1]
            elif tecla == key.DOWN:
                updated_position = [1, 0]
            elif tecla == key.PAGE_DOWN:
                self.current_tetromino.rotate_anticlockwise()

            elif tecla == key.PAGE_UP:
                self.current_tetromino.rotate_clockwise()
            elif tecla == 's':
                break
            elif tecla == 'g':
                
                break

            self.current_tetromino.update_position(
                updated_position[0], updated_position[1]
            )
            if not self.current_tetromino.is_inside_screen(self.screen):
                self.current_tetromino.set_blocks(old_blocks)
                self.current_tetromino.update_position(
                    -updated_position[0], -updated_position[1]
                )
                self.screen.draw_tetromino(self.current_tetromino)
            

            # Se o tetromino está fora da tela ou se há alguma colisão, ele voltará para a posição
            # anterior
            if self.current_tetromino.is_collided(self.screen):
                self.current_tetromino.set_blocks(old_blocks)
                self.current_tetromino.update_position(
                    -updated_position[0], -updated_position[1]
                )
                self.screen.draw_tetromino(self.current_tetromino)
                self.current_tetromino = self.new_tetromino()

            self.screen.draw_tetromino(self.current_tetromino)
            os.system("cls||clear")
            self.screen.show_screen()
            print(f'Pontuação: {self.score}')
            print(f'Teclas do jogo:')
            print(f'← move esquerda | → move direita | ↓ move baixo')
            print(f'<Page Down> rotaciona esquerda | <Page Up> rotaciona direita')
            print(f'<s> sai da partida, <g> grava e sai da partida')
