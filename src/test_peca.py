import pytest
from peca import *
import numpy as np
from tela import Tela


@pytest.fixture
def screen():
    return Tela(20, 10)


@pytest.fixture
def p():
    return Peca(5, 5)


def test_initialization(p):
    assert p.row == 5
    assert p.col == 5
    assert p.symbol == "$"
    assert np.array_equal(
        p.blocks,
        [
            {"row": 0, "col": 0},
            {"row": -1, "col": 0},
            {"row": 0, "col": 1},
            {"row": 1, "col": 1},
        ],
    )


def test_is_inside_screen_left(screen, p):
    assert p.is_inside_screen(screen) == True
    p.update_position(0, -60)
    assert p.is_inside_screen(screen) == False


def test_is_inside_screen_left(screen, p):
    assert p.is_inside_screen(screen) == True
    p.update_position(0, 60)
    assert p.is_inside_screen(screen) == False


def test_update_position(p):
    p.update_position(2, -1)
    assert p.row == 7
    assert p.col == 4


def test_is_collided(screen, p):
    new_peca = Peca(5, 5)
    screen.draw_tetromino(new_peca)
    assert p.is_collided(screen) == True
    p.update_position(2, 2)
    assert p.is_collided(screen) == False


def test_rotation_undo(p):
    original_blocks = p.get_blocks()
    p.rotate_clockwise()
    p.rotate_anticlockwise()
    assert all(
        block == original for block, original in zip(p.get_blocks(), original_blocks)
    )


def full_rotation_clockwise(p):
    original_blocks = p.get_blocks()
    p.rotate_clockwise()
    p.rotate_clockwise()
    p.rotate_clockwise()
    p.rotate_clockwise()
    assert all(
        block == original for block, original in zip(p.get_blocks(), original_blocks)
    )


def full_rotation_anticlockwise(p):
    original_blocks = p.get_blocks()
    p.rotate_anticlockwise()
    p.rotate_anticlockwise()
    p.rotate_anticlockwise()
    p.rotate_anticlockwise()
    assert all(
        block == original for block, original in zip(p.get_blocks(), original_blocks)
    )


def test_o_piece_no_rotation():
    o = O(5, 5)
    original_blocks = o.blocks[:]
    o.rotate_clockwise()
    assert o.blocks == original_blocks
    o.rotate_anticlockwise()
    assert o.blocks == original_blocks
