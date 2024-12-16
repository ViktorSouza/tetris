# Autor

Nome: João Viktor Souza Almeida

NUSP: 15521614

E-mail: viktoralmeida@usp.br

# Introdução

O projeto é uma implementação clássica do popular jogo de quebra-cabeças Tetris,
projetado para ser executado diretamente no terminal. Neste jogo, os jogadores
devem rotacionar, mover e alinhar tetrominos para preencher linhas horizontais.
A versão do jogo adiciona recursos modernos, como cores distintas para cada
peça, efeitos sonoros e uma trilha musical inspirada no original.

# Como executar

Antes de rodar o programa, é necessário instalar as bibliotecas externas que o
projeto utiliza.

O projeto utiliza quatro bibliotecas externas essenciais para garantir o
funcionamento adequado do jogo. Estas bibliotecas precisam ser instaladas antes
que o programa seja executado. Para instalar as bibliotecas necessárias, o
usuário deve executar o seguinte comando no terminal:

```console
pip install numpy pickle readchar pygame
```

### Numpy

O Numpy é uma biblioteca fundamental para manipulação de arrays e matrizes em
Python. No contexto deste projeto, o Numpy é utilizado para operações
matemáticas e para a geração de uma escolha pseudoaleatória de peças do jogo,
como tetrominos.

### Pickle

O pickle é uma biblioteca para serialização e desserialização de objetos Python.
Ela é utilizada neste projeto para salvar e carregar estados do jogo, como o
status atual das peças no tabuleiro, pontuações e configurações de configuração.

### Readchar

O readchar é uma biblioteca que facilita a captura de entrada do teclado em
tempo real, essencial para a interatividade do jogo. Ele permite que o programa
detecte rapidamente qual tecla foi pressionada pelo usuário, proporcionando uma
resposta dinâmica às ações do jogador.

### Pygame

O pygame é uma das bibliotecas mais populares para desenvolvimento de jogos em
Python. Neste projeto, o Pygame foi utilizado para adicionar efeitos sonoros ao
jogo, melhorando a imersão e a jogabilidade. A biblioteca em questão permite a
utilização de efeitos sonoros que sinalizam ações, como a rotação de uma peça ou
a eliminação de uma linha, e uma música de fundo, que contribui para a atmosfera
do jogo.

Após ter instalado as dependências, clone o repositório do projeto (utilizando
git clone) ou faça o download do código-fonte, navegue até o diretório do
projeto no terminal, e execute o programa usando o seguinte comando:

```console
python main.py
```

Após a execução, espera-se que seja impressa a mensagem "Terinal Tetris",
seguida dos atalhos para iniciar uma nova partida, ver melhores pontuações, etc.

# Make

Para facilitar a execução de funções recorrentes, utilizou-se o Make. No arquivo
Makefile, estão as seguintes funções:

- doc: gera a documentação do código.
- tests: executa os testes criados.
- all: gera a documentação e executa os testes.
- clean: limpa todos os arquivos intermediários gerados pelos outros alvos acima

# Funcionalidades adicionais

Além das solicitações para o jogo, foi adicionado colorações para cada
tetromino, permitindo uma melhor visualização das peças durante as partidas.
Além disso, foi adicionado efeitos sonoros para sinalizar ocorrências, tais como
o impedimento da rotação de uma peça ou o preenchimento de uma linha, durante
uma partida.

Por fim, adicionou-se uma música durante uma partida. Esta música, chamada de
Korobeiniki, é uma música russa, do século 19, que inspirou a criação da famosa
melodia do Tetris. A versão escolhida é cantada pelo coro do Exército Vermelho.

# Versão

É necessário destacar que o programa foi criado visando um bom funcionamento
para o Python na versão 3.12.7. Consequentemente, nota-se que não se assegurar a
ausência de erros em versões anteriores. Por fim, o programa foi desenvolvido,
testado e executado no sistema operacional Windows 11.
