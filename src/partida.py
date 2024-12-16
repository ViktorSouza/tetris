from tela import Tela
import pygame
import numpy as np
import peca as pecas
import os
from readchar import readkey, key

pygame.init()
error_sound = pygame.mixer.Sound("./sounds/error.wav")

channel = pygame.mixer.Channel(1)  # Use channel 0 for error sound


tetrominos = [pecas.I, pecas.J, pecas.L, pecas.O, pecas.S, pecas.T, pecas.Z]


class Partida:
    ## Constrói um objeto Partida.
    # Inicializa uma partida com o nome de usuário, número de linhas e número de colunas dados pelo usuário. É a classe por meio da qual o jogo irá interagir com a tela, movimentação dos tetrominos, etc.
    # @param self Ponteiro para o próprio objeto.
    # @param player Nome do jogador.
    # @param rows Número de linhas que a tela terá.
    # @param cols Quantidade de colunas que haverá na tela.
    def __init__(self, player: str, rows: int, cols: int):
        ## Tela da partida, na qual as peças serão deslocadas e giradas.
        self.screen = Tela(rows, cols)

        ## Peça com a qual o jogador irá interagir.
        self.current_tetromino = np.random.choice(tetrominos)(0, cols // 2)

        ## Valor boleano que indica se a partida foi encerrada.
        self.is_game_complete = False

        ## Nome do jogador
        self.player = player

        ## Lista que possui os próximos três tetrominos disponíveis. O primeiro tetromino é o próximo a aparecer após o usuário confirmar a posição do tetromino atual.
        self.next_tretrominos = [np.random.choice(tetrominos) for _ in range(3)]

        ## Variável que acumula as pontuações feitas pelo usuário.
        self.score = 0

    ## Cria um novo tetromino
    # Retorna um dos tetrominos disponíveis de maneira aleatória.
    # @param self Ponteiro para o próprio objeto.
    def new_tetromino(self):
        tetromino = np.random.choice(tetrominos)
        self.next_tretrominos.append(tetromino)
        return self.next_tretrominos.pop(0)(
            0,
            np.random.random_integers(low=2, high=self.screen.cols - 2),
        )

    ## Finaliza a partida.
    # Marca, utilizando uma variável, que a partida está completa, isto é, a peça gerada começa com colisão.
    # @param self Ponteiro para o próprio objeto.
    def end_game_instance(self):
        self.is_game_complete = True

    ## Checa se existe uma linha completa
    # Checa se há uma linha completa e, caso exista, remove-a, adicionando uma nova linha no topo da tela.
    # @param self Ponteiro para o próprio objeto.
    def full_line_check(self):
        lines_removed = 0
        for i, row in enumerate(self.screen.grid):
            if (row == "").sum() == 0:
                self.screen.remove_row(i)
                lines_removed += 1
        self.score += lines_removed**2
        if lines_removed >= 1:
            pygame.mixer.Sound("./sounds/complete_line.wav").play()

    ## Gira o tetromino em 90 graus no sentido horário.
    # @param self Ponteiro para o próprio objeto.
    def rotate_clockwise(self):
        self.current_tetromino.rotate_clockwise()
        if not self.current_tetromino.is_inside_screen(
            self.screen
        ) or self.current_tetromino.is_collided(self.screen):
            if not channel.get_busy():  # Play only if the channel is not busy
                channel.play(error_sound)
            self.current_tetromino.rotate_anticlockwise()

    ## Gira o tetromino em 90 graus no sentido anti-horário.
    # @param self Ponteiro para o próprio objeto.
    def rotate_anticlockwise(self):
        self.current_tetromino.rotate_anticlockwise()
        if not self.current_tetromino.is_inside_screen(
            self.screen
        ) or self.current_tetromino.is_collided(self.screen):
            if not channel.get_busy():  # Play only if the channel is not busy
                channel.play(error_sound)
            self.current_tetromino.rotate_clockwise()

    ## Move o tetromino um bloco para a esquerda
    # @param self Ponteiro para o próprio objeto.
    def move_left(self):
        self._move_tetromino(0, -1)

    ## Move o tetromino um bloco para a direita
    # @param self Ponteiro para o próprio objeto.
    def move_right(self):
        self._move_tetromino(0, 1)

    ## Move o tetromino um bloco para a direita
    # @param self Ponteiro para o próprio objeto.
    def move_down(self):
        self._move_tetromino(1, 0)

    ## Move o tetromino um bloco para uma dada direção.
    # Move o tetromino um bloco para uma dada direção. Antes de realizar a movimentação, é verificado se o tetromino pode ir para esta direção, isto é, se o tetromino, após movimentar-se, não colide e não está fora da tela.
    # @param self Ponteiro para o próprio objeto.
    # @param dy Distância, em blocos, que o tetromino irá ser deslocado. Número positivo indica que o tetromino irá se locomover para baixo.
    # @param dy Distância, em blocos, que o tetromino irá ser deslocado. Número positivo indica que o tetromino irá se locomover para a direita.
    def _move_tetromino(self, dy: int, dx: int):
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
