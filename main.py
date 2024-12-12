import os
import pickle
from readchar import readkey, key
import time
import numpy as np
from tela import Tela
from peca import Peca
from partida import Partida

game = Partida("Viktor", 20, 20)
game.start()
