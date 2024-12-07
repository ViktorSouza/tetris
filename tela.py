import numpy as np
from peca import Peca


class Tela:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def update_screen(self):
        pass

    def draw_tetromino(self, peca: Peca):
        for part in peca.parts:
            self.grid[peca.row + part[1]][peca.col + part[0]] = peca.symbol

    def remove_tetromino(self, peca):
        for part in peca.parts:
            self.grid[peca.row + part[1]][peca.col + part[0]] = None

    def show_screen(self):
        print("", "-" * self.rows)
        for row in self.grid:
            print("|", end="")
            for col in row:
                print(col or " ", end="")
            print("|", end="")
            print()
        print("", "-" * self.rows)
