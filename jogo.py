from partida import Partida
import os
from readchar import readkey, key
from tela import Tela
from peca import Peca


class Jogo:
    def new_game(self):
        pass

    def continue_game(self):
        pass

    def top_10_scores(self):
        pass

    def play(self, game_instance: Partida):
        while True:
            tecla = readkey()

            game_instance.screen.remove_tetromino(game_instance.current_tetromino)
            updated_position = [0, 0]
            old_blocks = game_instance.current_tetromino.get_blocks()

            if tecla == key.LEFT:
                game_instance.move_left()
            elif tecla == key.RIGHT:
                game_instance.move_right()
            elif tecla == key.DOWN:
                game_instance.move_down()
            elif tecla == key.PAGE_DOWN:
                game_instance.rotate_anticlockwise()

            elif tecla == key.PAGE_UP:
                game_instance.rotate_clockwise()
            elif tecla == "s":
                break
            elif tecla == "g":
                break

            game_instance.screen.draw_tetromino(game_instance.current_tetromino)
            os.system("cls||clear")
            game_instance.screen.show_screen()
            print(f"Pontuação: {game_instance.score}")
            print(f"Teclas do jogo:")
            print(f"← move esquerda | → move direita | ↓ move baixo")
            print(f"<Page Down> rotaciona esquerda | <Page Up> rotaciona direita")
            print(f"<s> sai da partida, <g> grava e sai da partida")

    def exit(self):
        pass

    def __init__(self):
        pass
