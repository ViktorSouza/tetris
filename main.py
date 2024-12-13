import os
import pickle
from readchar import readkey, key
import time
from partida import Partida
import numpy as np
from jogo import Jogo

game = Jogo()
game_instance = Partida("Viktor", 20, 20)
game.play(game_instance)
