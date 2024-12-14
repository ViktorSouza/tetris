from partida import Partida
import pickle
import os
from readchar import readkey, key
from tela import Tela
from peca import Peca


class Jogo:
    def __init__(self):
        self.current_game = None
        pass

    def display_options(self):
        print("- <i> para iniciar uma nova partida")
        print("- <c> para carregar uma partida gravada e continuá-la")
        print("- <p> para ver as 10 melhores pontuações")
        print("- <s> para sair do jogo")
        tecla = readkey()
        if tecla == "i":
            self.new_game()
        elif tecla == "c":
            self.continue_game()

    def new_game(self):
        name = input("Digite o nome do jogador:")
        rows = int(input("Digite o número de linhas da tela do jogo:"))
        cols = int(input("Digite o número de colunas da tela do jogo:"))
        self.current_game = Partida(name, rows, cols)
        self.play()

    def continue_game(self):
        # Carregando o objeto do arquivo
        with open("partida.pkl", "rb") as arquivo:
            pessoa_carregada = pickle.load(arquivo)
            self.current_game = pessoa_carregada
        self.play()

    def save_game(self):
        # Salvando o objeto em um arquivo
        with open("partida.pkl", "wb") as arquivo:
            pickle.dump(self.current_game, arquivo)

    def top_10_scores(self):
        pass

    def play(self):
        while True:
            if self.current_game.is_game_complete:
                break
            tecla = readkey()

            self.current_game.screen.remove_tetromino(
                self.current_game.current_tetromino
            )
            updated_position = [0, 0]
            old_blocks = self.current_game.current_tetromino.get_blocks()

            if tecla == key.LEFT:
                self.current_game.move_left()
            elif tecla == key.RIGHT:
                self.current_game.move_right()
            elif tecla == key.DOWN:
                self.current_game.move_down()
            elif tecla == key.PAGE_DOWN:
                self.current_game.rotate_anticlockwise()

            elif tecla == key.PAGE_UP:
                self.current_game.rotate_clockwise()
            elif tecla == "s":
                break
            elif tecla == "g":
                self.save_game()
                break

            self.current_game.full_line_check()

            self.current_game.screen.draw_tetromino(self.current_game.current_tetromino)
            os.system("cls||clear")
            self.current_game.screen.show_screen()
            print(f"Pontuação: {self.current_game.score}")
            print(f"Teclas do jogo:")
            print(f"← move esquerda | → move direita | ↓ move baixo")
            print(f"<Page Down> rotaciona esquerda | <Page Up> rotaciona direita")
            print(f"<s> sai da partida, <g> grava e sai da partida")
        self.display_options()

    def exit(self):
        pass
