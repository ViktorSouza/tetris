import os
import datetime
import pytest
from jogo import Jogo
from partida import Partida
from tela import Tela

# ******************
# Tendo em vista que todas as outras funções disponibilizadas
# pela classe jogo dependem da manipulação de arquivos e de entradas e saídas
# pelo terminal, não foi possível criar testes.
# ******************


@pytest.fixture
def jogo():
    return Jogo()


def test_init(jogo):
    assert jogo.current_game == None
