from partida import Partida
import pygame
import json
import pickle
import datetime
import os
from readchar import readkey, key
from tela import Tela
from peca import Peca

songs = ["./sounds/"]


class Jogo:
    ## Constrói um objeto Jogo.
    # Inicializa o jogo tendo, como a partida atual, None.
    def __init__(self):
        ## Partida que será jogada pelo usuário
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

    def choose_pkl_file(self):
        # Diretório onde os arquivos estão
        directory = "./data/"

        # Lista de arquivos .pkl no diretório
        pkl_files = [f for f in os.listdir(directory) if f.endswith(".pkl")]

        if not pkl_files:
            print("Não há jogos salvos.")
            return

        # Exibe a lista de arquivos
        print("Escolha um arquivo:")
        for i, filename in enumerate(pkl_files):
            player, date, time = filename.split("_")
            time = time[:-4]  # Remover o .pkl
            date = date.replace("-", "/")
            time = time.replace("-", ":")
            print(f"{i + 1}. {player}, {date} {time}")

        # Espera o usuário escolher uma opção
        choice = input("Digite o número do arquivo que deseja escolher: ")

        try:
            choice = int(choice)
            if 1 <= choice <= len(pkl_files):
                chosen_file = pkl_files[choice - 1]
                print(f"Você escolheu o arquivo: {chosen_file}")
                return chosen_file
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Por favor, insira um número válido.")

    def continue_game(self):
        # Carregando o objeto do arquivo
        choosen_file = self.choose_pkl_file()
        if choosen_file == None:
            self.display_options()
        with open(f"./data/{choosen_file}", "rb") as arquivo:
            pessoa_carregada = pickle.load(arquivo)
            self.current_game = pessoa_carregada
        self.play()
        self.display_options()

    ## Salva a partida atual em um arquivo.
    # A partida atual será salvada em um arquivo, possibilitando que o usuário continue a jogar a última partida mesmo que o terminal seja fechado.
    #  @param self Ponteiro para o próprio objeto.
    def save_game(self):
        # Salvando o objeto em um arquivo
        date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(
            f"./data/{self.current_game.player}_{date}.pkl",
            "wb",
        ) as arquivo:
            pickle.dump(self.current_game, arquivo)

    ## Imprime as dez melhores pontuações.
    # Imprime, em ordem decrescente, as dez melhores pontuações dos usuários. Nota-se que um mesmo jogador pode aparecer no placar diversas vezes.
    #  @param self Ponteiro para o próprio objeto.
    def top_10_scores(self):
        print("Lista das 10 melhores pontuações:")
        with open("./data/scores.json", "r") as f:
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
        if not os.path.exists("./data/scores.json"):
            # Se o arquivo não existir, será criado com uma lista vazia
            with open("./data/scores.json", "w") as file:
                json.dump([], file)

        data = {
            "player": self.current_game.player,
            "score": self.current_game.score,
        }

        with open("./data/scores.json", "r+") as f:
            res = json.load(f)
            res.append(data)
            f.seek(0)

            json.dump(res, f, indent=4)
            f.truncate()

    ## Desenha, em uma dada tela, os próximos tetrominos
    # Dado uma dela, desenha nesta os próximos tetrominos. A função assume que a tela estará limpa, isto é, não há tetrominos já desenhados nela.
    #  @param self Ponteiro para o próprio objeto.
    #  @param screen Tela na qual serão desenhados os tetrominos.
    def draw_next_tetrominos(self, screen: Tela):
        for i, tetromino in enumerate(self.current_game.next_tretrominos):
            col = 2 + i * 4
            screen.draw_tetromino(tetromino(0, col))

    ## Executa o loop principal de uma partida.
    # Responsável por exibir o estado atual do jogo e capturar as ações do jogador. Além disso, a função é responsável pela detecção da finalização de uma partida.
    #  @param self Ponteiro para o próprio objeto.
    def play(self):
        music = pygame.mixer.Sound("./sounds/music.mp3")
        music.set_volume(0.2)
        music.play()
        next_tetrominos_screen = Tela(2, 14)
        next_tetrominos_position = []
        os.system("cls||clear")
        self.current_game.screen.draw_tetromino(self.current_game.current_tetromino)
        self.draw_next_tetrominos(next_tetrominos_screen)
        self.current_game.screen.show_screen()
        next_tetrominos_screen.show_screen()

        self.display_game_info()

        while True:

            if self.current_game.is_game_complete:
                music.stop()
                print()
                print("Partida finalizada!")
                fail_sound = pygame.mixer.Sound("./sounds/fail.mp3")
                fail_sound.play()
                print(f"Pontuação: {self.current_game.score}")
                print()
                self.save_score()
                break
            tecla = readkey()

            self.current_game.screen.remove_tetromino(
                self.current_game.current_tetromino
            )

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
                music.stop()
                os.system("cls||clear")
                print("Você saiu da partida!")
                break
            elif tecla == "g":
                music.stop()
                os.system("cls||clear")
                print("Você gravou e saiu da partida!")
                self.save_game()
                break

            self.current_game.full_line_check()

            self.current_game.screen.draw_tetromino(self.current_game.current_tetromino)
            os.system("cls||clear")
            self.current_game.screen.show_screen()
            next_tetrominos_screen.clean_screen()
            self.draw_next_tetrominos(next_tetrominos_screen)
            next_tetrominos_screen.show_screen()

            self.display_game_info()
        self.display_options()

    ## Exibe informações sobre o estado atual do jogo e as teclas de controle.
    # Esta função imprime a pontuação atual do jogo e as instruções para controlar o tetromino no terminal. As teclas exibidas incluem movimentos para esquerda, direita, baixo, e rotações, além de comandos para salvar ou sair da partida.
    # @note Esta função utiliza o atributo {@link self.current_game.score} para exibir a pontuação atual.
    # @param self Ponteiro para o próprio objeto.
    # @return void Não possui valor de retorno.
    def display_game_info(self):
        print(f"Pontuação: {self.current_game.score}")
        print("Teclas do jogo:")
        print("← move esquerda | → move direita | ↓ move baixo")
        print("<Page Down> rotaciona esquerda | <Page Up> rotaciona direita")
        print("<s> sai da partida, <g> grava e sai da partida")

    ## Sai do jogo.
    # Função responsável pelo tratamendo da saída do usuário, isto é, a finalização do jogo no terminal.
    # @param self Ponteiro para o próprio objeto.
    def exit(self):
        print("Saindo do jogo...")
        os.abort()
