import numpy as np
from peca import Peca


class Tela:
    ## Cria uma instância de uma Tela.
    #  @param self Ponteiro para o próprio objeto.
    #  @param rows número de linhas que a tela possuirá.
    #  @param cols número de colunas que a tela possuirá.
    def __init__(self, rows: int, cols: int):
        # número de linhas que a tela possuirá.
        self.rows = rows
        # número de colunas que a tela possuirá.
        self.cols = cols
        # grid que será composto pelas peças.
        self.grid = np.empty(shape=(rows, cols), dtype=str)

    ## Remove uma coluna específica.
    # Dado um inteiro i, remove a i-ésima coluna da partida. Para manter a mesma quantidade de linhas, adiciona-se uma linha no topo da tela.
    #  @param self Ponteiro para o próprio objeto.
    # @param i Posição da linha que será removida.
    def remove_row(self, i: int):
        self.grid = np.delete(self.grid, (i), axis=0)
        self.grid = np.insert(self.grid, 0, np.full(self.cols, ""), axis=0)

    ## Desenha um tetromino.
    # Dado um tetromino, imprime-o na tela. É necessário destacar que a função assume que o tetromino não viola nenhuma regra do jogo, isto é, o tetromino não está em colisão e nem fora da tela.
    #  @param self Ponteiro para o próprio objeto.
    # @param peca Peça a ser desenhada.
    def draw_tetromino(self, peca: Peca):
        for block in peca.blocks:
            self.grid[peca.row + block["row"]][peca.col + block["col"]] = peca.symbol

    ## Remove um tetromino.
    # Dado um tetromino, remove-o da tela. É necessário destacar que a função assume que o tetromino não viola nenhuma regra do jogo, isto é, o tetromino não está em colisão e nem fora da tela.
    #  @param self Ponteiro para o próprio objeto.
    # @param peca Peça a ser desenhada.
    def remove_tetromino(self, peca: Peca):
        for block in peca.blocks:
            block_row = peca.row + block["row"]
            block_col = peca.col + block["col"]
            self.grid[block_row][block_col] = ""

    ## Mostra a tela.
    # Após a função ser invocada, imprime tudo o que está na tela, com uma borda em todos os lados.
    def show_screen(self):
        char_color = {
            "$": "\033[31m",  # Vermelho
            "%": "\033[32m",  # Verde
            "*": "\033[34m",  # Azul
            "@": "\033[36m",  # Ciano
            "#": "\033[33m",  # Amarelo
        }
        print("", "-" * self.cols)
        for row in self.grid:
            print("|", end="")
            for col in row:
                print(f"{char_color.get(col,'')}{col or " "}\033[0m", end="")
            print("|", end="")
            print()
        print("", "-" * self.cols)

    ## Remove tudo que está na tela.
    # Após a função ser invocada, a tela voltará aos padrões na qual se encontrava logo após a criação.
    # @param
    def clean_screen(self):
        self.grid = np.empty(shape=(self.rows, self.cols), dtype=str)
