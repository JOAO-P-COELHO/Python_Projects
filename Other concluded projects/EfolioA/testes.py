import pygame

("\n Game started! \U0001F60E \n")
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
    window_width, window_height = 700, 700
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
