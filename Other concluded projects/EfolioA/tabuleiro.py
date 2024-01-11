import pygame

# Inicialização do Pygame
pygame.init()

# Definições da janela de jogo
window_width, window_height = 600, 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Jogo das Damas")

# Cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Tamanho do tabuleiro e célula
board_size = 8
cell_size = window_width // board_size

# Função para desenhar o tabuleiro
def draw_board():
    for row in range(board_size):
        for col in range(board_size):
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

# Função para desenhar as damas
def draw_pieces():
    for row in range(board_size):
        for col in range(board_size):
            if (row + col) % 2 != 0:
                pygame.draw.circle(screen, red, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), cell_size // 2 - 5)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    # Limpa a tela
    screen.fill(white)

    # Desenha o tabuleiro e as damas
    draw_board()
    draw_pieces()

    # Atualiza a tela do Pygame
    pygame.display.flip()