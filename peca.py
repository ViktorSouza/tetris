import numpy as np

colors = {""}


class Peca:
    def __init__(self, initial_row, initial_col):
        # Por convenção, row e col definem a posição do centro
        self.row = initial_row
        self.col = initial_col
        self.symbol = "$"
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": -1, "col": 0},
            {"row": 0, "col": 1},
            {"row": 1, "col": 1},
        ]

    def update_position(self, dy, dx):
        self.row += dy
        self.col += dx

    def rotate_left(self):
        self._rotate(clockwise=False)

    def rotate_right(self):
        self._rotate(clockwise=True)

    def _rotate(self, clockwise: bool):
        for block in self.blocks:
            # Translate block to origin

            # Apply rotation
            if clockwise:
                block["col"], block["row"] = block["row"], -block["col"]
            else:
                block["col"], block["row"] = -block["row"], block["col"]

    def is_tetromino_inside_border(self, screen):
        for block in self.blocks:
            block_row = block["row"] + self.row
            block_col = block["col"] + self.col
            # Não será checado o chão
            if block_row < 0 or block_col < 0 or block_col >= screen.cols:
                return False
        return True

    def is_tetromino_collided(self, screen):
        for block in self.blocks:
            block_row = block["row"] + self.row
            block_col = block["col"] + self.col
            print(block_row, screen.rows)
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

    def rotate_left(self):
        """Como o quadrado não é modificado após uma rotação, a função não fará nada"""
        pass

    def rotate_right(self):
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


class J(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": 0, "col": 1},
            {"row": 0, "col": -1},
            {"row": 1, "col": 1},
        ]


class L(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": 0, "col": 1},
            {"row": 0, "col": -1},
            {"row": 1, "col": -1},
        ]


class T(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": 0, "col": 1},
            {"row": 0, "col": -1},
            {"row": 1, "col": 0},
        ]


class Z(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": 0},
            {"row": 1, "col": 1},
            {"row": 0, "col": -1},
            {"row": 1, "col": 0},
        ]


class I(Peca):
    def __init__(self, initial_row, initial_col):
        super().__init__(initial_row, initial_col)
        self.blocks = [
            {"row": 0, "col": -1},
            {"row": 0, "col": 0},
            {"row": 0, "col": 1},
            {"row": 0, "col": 2},
        ]
