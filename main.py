import os
import sys
import pickle
from readchar import readkey, key
import time
import numpy as np
import pygame

# Simula que o script está na pasta /src
original_dir = os.getcwd()
src_dir = os.path.join(original_dir, "src")
os.chdir(src_dir)
sys.path.append(".")

from partida import Partida
from jogo import Jogo

# Restaura o diretório original ao finalizar o script
try:
    pygame.mixer.init()
    os.system("cls||clear")
    print("Terminal Tetris")
    game = Jogo()
    game.display_options()
finally:
    os.chdir(original_dir)
