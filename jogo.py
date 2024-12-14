## @file jogo.py
## Implementação da classe Jogo, que gerencia o funcionamento geral de um jogo estilo Tetris.
#
# Este arquivo define a classe Jogo, que oferece funcionalidades como iniciar novas partidas,
# carregar partidas salvas, salvar pontuações e interagir com o usuário.

from partida import Partida
import json
import pickle
import os
from readchar import readkey, key
from tela import Tela
from peca import Peca


class Jogo:
    ## Constrói um objeto Jogo.
    # Inicializa o jogo tendo, como a partida atual, None.
    def __init__(self):
        # Partida que será jogada pelo usuário
        self.current_game = None

    ## Imprime as opções disponíveis para o jogo, tais como iniciar uma partida ou sair do jogo.
    #  @param self Ponteiro para o próprio objeto.
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
            self.exit()

    ## Inicia uma nova partida.
    # Para iniciar uma nova partida, é necessário que o usuário digite, em linhas diferentes, o nome que será utilizado para salvar a partida e o número de linhas e colunas para o jogo.
    #  @param self Ponteiro para o próprio objeto.
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

    ## Salva a partida atual em um arquivo.
    # A partida atual será salvada em um arquivo, possibilitando que o usuário continue a jogar a última partida mesmo que o terminal seja fechado.
    #  @param self Ponteiro para o próprio objeto.
    def save_game(self):
        # Salvando o objeto em um arquivo
        with open("partida.pkl", "wb") as arquivo:
            pickle.dump(self.current_game, arquivo)

    ## Imprime as dez melhores pontuações.
    # Imprime, em ordem decrescente, as dez melhores pontuações dos usuários. Nota-se que um mesmo jogador pode aparecer no placar diversas vezes.
    #  @param self Ponteiro para o próprio objeto.
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

    ## Salva o placar da partida atual.
    # Após o jogador finalizar a partida, a sua pontuação é salva em um arquivo, no qual se encontra todas as pontuações de todos os jogadores. Este arquivo será utilizado para imprimir as melhores pontuações.
    #  @param self Ponteiro para o próprio objeto.
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

    ## Executa o loop principal de uma partida.
    # Responsável por exibir o estado atual do jogo e capturar as ações do jogador. Além disso, a função é responsável pela detecção da finalização de uma partida.
    #  @param self Ponteiro para o próprio objeto.
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

    ## Sai do jogo.
    # Função responsável pelo tratamendo da saída do usuário, isto é, a finalização do jogo no terminal.
    # @param self Ponteiro para o próprio objeto.
    def exit(self):
        print("Saindo do jogo...")
        os.abort()
