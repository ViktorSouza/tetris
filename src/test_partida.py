from partida import Partida
import numpy as np
import pytest
from unittest.mock import Mock, patch
from tela import Tela
from peca import O, Peca


@pytest.fixture
def partida():
    return Partida("Viktor", 10, 10)


@pytest.fixture
def peca():
    return O(5, 5)  # Initial row and column of the piece


def test_init(partida):
    assert isinstance(partida.current_tetromino, Peca)
    assert isinstance(partida.screen, Tela)
    assert partida.player == "Viktor"


def test_screen_resolution(partida):
    assert partida.screen.rows == 10
    assert partida.screen.cols == 10


def test_new_tetromino(partida):
    partida.new_tetromino()
    assert isinstance(partida.current_tetromino, Peca)


def test_end_game_instance(partida):
    partida.end_game_instance()
    assert partida.is_game_complete == True


def test_full_line_check(partida):
    partida.screen.grid[-1] = np.array(["#"] * 10)
    partida.full_line_check()
    assert (partida.screen.grid[-1] == "#").sum() == 0
