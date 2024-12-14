from partida import Partida
import json
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
        while tecla not in ["i", "c", "p", "s"]:
            tecla = readkey()
        os.system("cls||clear")
        if tecla == "i":
            self.new_game()
        elif tecla == "c":
            self.continue_game()
        elif tecla == "p":
            self.top_10_scores()
        elif tecla == "s":
            print("Saindo do jogo...")
            os.abort()

    def new_game(self):
        name = input("Digite o nome do jogador:")
        rows = int(input("Digite o número de linhas da tela do jogo:"))
        cols = int(input("Digite o número de colunas da tela do jogo:"))
        self.current_game = Partida(name, rows, cols)
        self.play()
        self.display_options()

    def continue_game(self):
        # Carregando o objeto do arquivo
        with open("partida.pkl", "rb") as arquivo:
            pessoa_carregada = pickle.load(arquivo)
            self.current_game = pessoa_carregada
        self.play()
        self.display_options()

    def save_game(self):
        # Salvando o objeto em um arquivo
        with open("partida.pkl", "wb") as arquivo:
            pickle.dump(self.current_game, arquivo)

    def top_10_scores(self):
        print("Lista das 10 melhores pontuações:")
        with open("scores.json", "r") as f:
            data: list = json.load(f)
            data.sort(key=lambda x: x["score"], reverse=True)
            data = data[:10]
            for play in data:
                print(f"{play['player']}: {play['score']}")
        print()

        self.display_options()

    def save_score(self):
        if not os.path.exists("scores.json"):
            # Se o arquivo não existir, será criado com uma lista vazia
            with open("scores.json", "w") as file:
                json.dump([], file)

        data = {
            "player": self.current_game.player,
            "score": self.current_game.score,
        }

        with open("scores.json", "r+") as f:
            res = json.load(f)
            res.append(data)
            f.seek(0)

            json.dump(res, f, indent=4)
            f.truncate()

    def play(self):
        os.system("cls||clear")
        self.current_game.screen.draw_tetromino(self.current_game.current_tetromino)
        self.current_game.screen.show_screen()
        print(f"Pontuação: {self.current_game.score}")
        print("Teclas do jogo:")
        print("← move esquerda | → move direita | ↓ move baixo")
        print("<Page Down> rotaciona esquerda | <Page Up> rotaciona direita")
        print("<s> sai da partida, <g> grava e sai da partida")
        while True:
            if self.current_game.is_game_complete:
                print()
                print("Partida finalizada!")
                print(f"Pontuação: {self.current_game.score}")
                print()
                self.save_score()
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
            print("Teclas do jogo:")
            print("← move esquerda | → move direita | ↓ move baixo")
            print("<Page Down> rotaciona esquerda | <Page Up> rotaciona direita")
            print("<s> sai da partida, <g> grava e sai da partida")
        self.display_options()

    def exit(self):
        pass
