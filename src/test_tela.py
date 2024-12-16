from tela import Tela
import numpy as np
from peca import S
import pytest


@pytest.fixture
def screen():
    return Tela(4, 4)


def test_init_screen(screen):
    assert screen.cols == 4
    assert screen.rows == 4
    assert np.array_equal(screen.grid, np.empty(shape=(4, 4), dtype=str))


def test_remove_row(screen):
    screen.grid[3] = np.array(["#"] * 4)
    screen.remove_row(3)
    assert (screen.grid[-1] == "#").sum() == 0
    assert len(screen.grid) == 4


def test_draw_tetromino(screen):
    tetromino = S(1, 1)
    screen.draw_tetromino(tetromino)

    assert np.array_equal(
        screen.grid,
        [["", "", "", ""], ["", "%", "%", ""], ["%", "%", "", ""], ["", "", "", ""]],
    )


def test_remove_tetromino(screen):
    tetromino = S(1, 1)
    screen.draw_tetromino(tetromino)
    screen.remove_tetromino(tetromino)
    assert np.array_equal(screen.grid, [[""] * 4] * 4)


def test_clean_screen(screen):
    screen.clean_screen()
    assert np.array_equal(screen.grid, np.empty(shape=(4, 4), dtype=str))
