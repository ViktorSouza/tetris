import numpy as np
from peca import Peca


class Tela:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = np.empty(shape=(rows, cols), dtype=str)

    def update_screen(self, new_screen):
        self.grid = new_screen

    def remove_row(self, i: int):
        self.grid = np.delete(self.grid, (i), axis=0)
        self.grid = np.insert(self.grid, 0, np.full(self.cols, ""), axis=0)

    def copy_screen(self):
        return self.grid.copy()

    def draw_tetromino(self, peca: Peca):
        for block in peca.blocks:
            self.grid[peca.row + block["row"]][peca.col + block["col"]] = peca.symbol

    def remove_tetromino(self, peca: Peca):
        for block in peca.blocks:
            block_row = peca.row + block["row"]
            block_col = peca.col + block["col"]
            self.grid[block_row][block_col] = ""

    def show_screen(self):
        print("", "-" * self.rows)
        for row in self.grid:
            print("|", end="")
            for col in row:
                print(col or " ", end="")
            print("|", end="")
            print()
        print("", "-" * self.rows)
