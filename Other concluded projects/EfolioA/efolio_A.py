# Jogo das Damas 

# Importação da biblioteca utilizada na criação do tabuleiro e das peças (assim com dos menus e botões)
import pygame

# Definição das classes

# Class Initializer/Inicializadora | Inicializa o jogo (e parâmetros que configuram a janela de jogo, etc) e invoca o tabuleiro e as peças
class Initializer:
    def __init__(self):
        pygame.init()
        self.window_width = 700  # Define a largura da janela do jogo
        self.window_height = 700  # Define a altura da janela
                
    def game_start(self): # Inicializa o jogo e invoca o tabuleiro e as peças, posicionando-as de acordo com as regras
        self.board_initialize()
        self.run_game_loop()
        
    def board_initialize(self):  # Inicializa o tabuleiro e as peças nas respetivas posições
        pass   
    
    def game_run(self): # Neste método existirá a lógica que incorporá as ações do user, neste caso, unicamente feitas com recurso ao rato
        pass
    
    def game_update(self): # Este método actulizará o estado aparente do jogo, tendo em conta, por exemplo, jogadas.
        pass

    

# Class Board/tabuleiro | Define o tabuleiro e como este
class Board:
    def __init__(self, columns, rows): # Os parâmetros columns e rows vão definir as propriedades do tabuleiro (número de quadrados do jogo, por exemplo) 
        self.rows = rows
        self.cols = cols
        self.tiles = self.tile_defining()
    
    def tile_defining(self): # Gera os quadrados consoante os parâmetros anteriormente introduzidos
        pass
    
    def clicked(self, mouse): # Este método verfica onde ocorreu o clique do utilizador, necessariamente com recurso à posição do rato (será necessário adquirir as coordenadas)
        pass
    
    def draw_board(self): # Este método desenha o tabuleiro - envolve/invoca a biblioteca pygame
        pass 
    

# Class Tile/Quadrado | Define as propriedades quadriculares
class Tile:
    def __init__(self, c_x, c_y, parametro_quadrado1, parametro_quadrado2, parametro_quadrado3): # Os parâmetros_quadrado 1,2, etc, são os parâmetros que vão definir as propriedades dos próprios quadrados (largura, cor, etc) 
        self.c_x = c_x # Coordenada x inicial do
        self.c_y = c_y # Coordenada y inicial
        self.parametro_quadrado1 = parametro_quadrado1 
        self.parametro_quadrado2 = parametro_quadrado2 
        self.parametro_quadrado3 = parametro_quadrado3
        pass 

    def get_coord(self): # Método utilizado obter coordenadas das peças movidas
        pass
    
    def draw_tile(self): # Este método desenha o próprio quadrado - envolve/invoca a biblioteca pygame
        pass 

# Class Peça | Define as propriedades das peças
class Piece:
    def __init__(self, color, grid_num, parametro_peca1, parametro_peca2): # Cada peça inicializa com determinado conjunto de parâmeros(por exemplo, cor, posição no tabuleiro)
        self.color = color # Cor da peça
        self.grid_num = grid_num # Onde está localizada a peça
        self.parametro_peca1 = parametro_peca1;
        self.parametro_peca2 = parametro_peca2;
    
    def movement(self, new_grid_num): # Lógica utilizada no movimento da peça para outro tile
        # Adicione lógica para mover a peça para um novo quadrado no tabuleiro
        self.grid_num = new_grid_num
    
    def draw_piece(self): # Este método desenha a peça - envolve/invoca a biblioteca pygame
        pass 
  
# Subclass Peão | Define as propriedades das peças-peão
class Pawn(Piece):
    def __init__(self, color, grid_num): # Inicialização 
        super().__init__(color, grid_num) # Vai buscar à classe "mãe" alguns parâmetros
        pass
    
    def movements_possible(self, current_position, new_position): # Método que descreve as jogadas possíveis para um peão
        pass
 
# Subclass Dama | Define as propriedades das peças-Dama
class Dame(Piece):
    def __init__(self, color, grid_num): # Inicialização 
        super().__init__(color, grid_num) # Vai buscar à classe "mãe" alguns parâmetros
        pass
    
    def movements_possible(self, current_position, new_position): # Método que descreve as jogadas possíveis para uma Dama (é necessariamente diferente do método "possible()"" na subclass Peão)
        pass

# Class Regras/Rules | Verifica o cumprimento das regras do jogo e define o final do mesmo
class Rules:
    def __init__(self):
        self.winner = None # Descreve que o jogo (ainda) não tem vencedores
            
    def movement(self, piece, current_position, new_position):
        pass # Verifica o movimento da peça selecionada - se o movimento é válido e se tem de fazer esse movimento (por se ser obrigatório "capturar" nas damas)
    
    def checking(self):
        pass # Verifica se ainda existem peças do jogador 1 e/ou peças do jogador 2
    
    def game_over(self):
        pass # Compara o número de peças obtidos com o método checking() e apresenta um vencedor, caso checking retorne que jogador 1 ou jogador 2 tem zero peças
    
    
# ______________________________________________________________________________________________________________________________  
    
# Fase mais avançada do projeto
# Inicia o jogo

print("\n Game started! \U0001F60E \n")

def start_game():
    pass

def exit_game():
    pygame.quit()
    
def main_menu(screen):
    clock = pygame.time.Clock() # Controlo dos FPS do jogo

    while True: # Para selecionar opções com o clique do rato, são utilizadas as suas coordenadas do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if 300 <= x <= 600 and 200 <= y <= 250:
                        print ("\n Let's play! \U0001F3AE")
                        second_menu(screen) # Vai para o segundo menu
                    elif 300 <= x <= 600 and 300 <= y <= 350:
                        exit_game()

        screen.fill((255, 255, 255))
        draw_text(screen, "Jogo das Damas | made by JC", 50, window_width // 2, 100, (0, 0, 0))

        pygame.draw.rect(screen, (186, 196, 200), (300, 200, 300, 50))
        draw_text(screen, "Start the game!", 30, 450, 225, (0, 0, 0))

        pygame.draw.rect(screen, (186, 196, 200), (300, 300, 300, 50))
        draw_text(screen, "Quit", 30, 450, 325, (0, 0, 0))

        pygame.display.flip()
        clock.tick(60)  # Nr. de FPS do jogo

def second_menu(screen):
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if 300 <= x <= 600 and 200 <= y <= 250:
                        print("\U0001F9B8 vs. \U0001F9B9 it is!")
                        board(screen)
                    elif 300 <= x <= 600 and 300 <= y <= 350:
                        print("\U0001F9B8 vs. \U0001F916 it is!")
                        
                        board(screen)
                    elif 300 <= x <= 600 and 400 <= y <= 450:
                        main_menu(screen)

        screen.fill((255, 255, 255))
        draw_text(screen, "Pick up a mode!", 50, window_width // 2, 100, (0, 0, 0))

        pygame.draw.rect(screen, (200, 200, 200), (300, 200, 300, 50))
        draw_text(screen, "1 vs. 1", 30, 450, 225, (0, 0, 0))

        pygame.draw.rect(screen, (200, 200, 200), (300, 300, 300, 50))
        draw_text(screen, "1 vs. Computer", 30, 450, 325, (0, 0, 0))

        pygame.draw.rect(screen, (200, 200, 200), (300, 400, 300, 50))
        draw_text(screen, "Back", 30, 450, 425, (0, 0, 0))

        pygame.display.flip()
        clock.tick(60)

def board(screen):
    pygame.init()

    # Definições da janela de jogo
    window_width, window_height = 700, 700 # Definições da tela de jogo
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Jogo das Damas")

    # Variáveis cor
    bege = (249, 228, 183)
    brown = (101, 67, 33)
    player_1 = (255, 255, 255)
    player_2 = (0, 0, 0)

    # Definição do número de tiles
    board_size = 8
    cell_size = window_width // board_size

    # Desenho do tabuleiro
    def draw_board():
        for row in range(board_size):
            for col in range(board_size):
                color = brown if (row + col) % 2 == 0 else bege
                pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    # Preenchimento com as peças
    def draw_pieces():
        for row in range(board_size):
            for col in range(board_size):
                if (row + col) % 2 != 0:
                    piece_color = player_1 if row < 4 else player_2  # Primeiras 3 linhas são amarelas, próximas 3 são castanhas
                    pygame.draw.circle(screen, piece_color, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), cell_size // 2 - 5)

    # Loop do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        # Limpa a tela
        screen.fill(bege)

        # Desenha o tabuleiro e as peças ao invocar estes métodos
        draw_board()
        draw_pieces()

        # Atualiza a tela
        pygame.display.flip()
    

def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

if __name__ == '__main__':
    pygame.init()
    window_width, window_height = 900, 700
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Jogo das Damas | made by JC")
    main_menu(screen)