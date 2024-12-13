import numpy as np

colors = {""}


class Peca:
    ## Cria uma instância de uma peça.
    #  @param self Ponteiro para o próprio objeto.
    #  @param initial_row posição da linha na qual a peça estará inicialmente.
    #  @param initial_col posição da coluna na qual a peça estará inicialmente.
    def __init__(self, initial_row, initial_col):
        ## Por convenção, row é a posição do centro da peça.
        self.row = initial_row
        ## Por convenção, col é a posição do centro da peça.
        self.col = initial_col
        ## Símbolo que representará a peça no terminal.
        self.symbol = "$"
        ## Lista de tuplas com posições dos blocos de uma peça.
        self.blocks = np.array([
            {"row": 0, "col": 0},
            {"row": -1, "col": 0},
            {"row": 0, "col": 1},
            {"row": 1, "col": 1},
        ])
        self.blocks

    ## Modifica a posição da peça, tanto linhas quanto colunas.
    #  @param self Ponteiro para o próprio objeto.
    #  @param dy número de vezes que a peça deverá ser deslocada em relação às linhas. Um valor positivo indica que a peça será deslocada para baixo dy vezes
    #  @param dx número de vezes que a peça deverá ser deslocada em relação às colunas. Um valor positivo indica que a peça será deslocada para a direita dx vezes
    def update_position(self, dy: int, dx: int):
        self.row += dy
        self.col += dx

    ## Rotaciona, em sentido horário, a peça em 90 graus.
    #  @param self Ponteiro para o próprio objeto.
    def rotate_clockwise(self):
        self._rotate(clockwise=False)

    ## Rotaciona, em sentido anti-horário, a peça em 90 graus.
    #  @param self Ponteiro para o próprio objeto.
    def rotate_anticlockwise(self):
        self._rotate(clockwise=True)

    def _rotate(self, clockwise: bool):
        for block in self.blocks:
            if clockwise:
                block["col"], block["row"] = block["row"], -block["col"]
            else:
                block["col"], block["row"] = -block["row"], block["col"]

    def get_blocks(self):
        return self.blocks

    def set_blocks(self, blocks):
        self.blocks = blocks

    def is_inside_screen(self, screen):
        for block in self.blocks:
            block_row = block["row"] + self.row
            block_col = block["col"] + self.col
            # Não será checado o chão
            if block_row < 0 or block_col < 0 or block_col >= screen.cols:
                return False
        return True

    ## Testa se o tetromino colidiu com outra peça.
    #  @param self Ponteiro para o próprio objeto.
    #  @param screen Instância de uma {@link Tela}.
    #  @returns True caso a peça atual colidiu, False caso contrário.

    def is_collided(self, screen):
        for block in self.blocks:
            block_row = block["row"] + self.row
            block_col = block["col"] + self.col
            # Teste para decidir se o tetromino está no chão.
            if block_row >= screen.rows:
                return True
            # Teste para decidir se o tetromino colidiu com outra peça.
            if screen.grid[block_row][block_col] != "":
                return True

        return False


class O(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": 1, "col": 0},
            {"row": 0, "col": 1},
            {"row": 1, "col": 1},
        ]
        self.symbol = "+"

    def rotate_clockwise(self):
        """Como o quadrado não é modificado após uma rotação, a função não fará nada"""
        pass

    def rotate_anticlockwise(self):
        pass


class S(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": 1, "col": 0},
            {"row": 0, "col": 1},
            {"row": 1, "col": -1},
        ]
        self.symbol = "%"


class J(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": 0, "col": 1},
            {"row": 0, "col": -1},
            {"row": 1, "col": 1},
        ]
        self.symbol = "#"


class L(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": 0, "col": 1},
            {"row": 0, "col": -1},
            {"row": 1, "col": -1},
        ]
        self.symbol = "@"


class T(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": 0, "col": 1},
            {"row": 0, "col": -1},
            {"row": 1, "col": 0},
        ]
        self.symbol = "#"


class Z(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": 1, "col": 1},
            {"row": 0, "col": -1},
            {"row": 1, "col": 0},
        ]
        self.symbol = "*"


class I(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": -1},
            {"row": 0, "col": 0},
            {"row": 0, "col": 1},
            {"row": 0, "col": 2},
        ]
        self.symbol = "%"
