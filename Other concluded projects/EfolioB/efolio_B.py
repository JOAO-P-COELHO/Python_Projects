##### Checkers Game (EN) | Jogo das Damas (PT) ##### 


from os import environ # Disables the console's "Hello from the pygame community" message when the pygame library is used
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Disables the console's "Hello from the pygame community" message when the pygame library is used

# Import of the library used to create the board and pieces (as well as the menus and buttons)
import pygame # Don't forget to: pip install pygame
import sys

# Import the library used to play sounds - Don't forget to: pip install playsound==1.2.2
from playsound import playsound # pip install playsound==1.2.2  ! It is very important that this is the version of this library - the most recent one has bugs. Downgrade to this version is required!

# Import datetime - used to store the days at the games were played
from datetime import date, datetime

# Import the image/icon used in the windows, next to caption and the image used in the principal menu
logo_path = 'images/logo.tif'
main_path = 'images/main.tif'
pygame_icon = pygame.image.load(logo_path)
pygame_main_menu = pygame.image.load(main_path)
pygame_main_menu = pygame.transform.scale(pygame_main_menu, (300, 300))

pygame.display.set_icon(pygame_icon) # Setting that icon


# Classes definition
class Tile: # Defines the properties of the squares used to create the game board.
	def __init__(self, x, y, tile_width, tile_height): # Defines the color, size of the squares, etc.
     
		# Variables that define the color of the game squares (tiles)
		bege = (249, 228, 183)
		brown = (101, 67, 33)
		possible_moves_color = (255,255,102)
  		
		# Methods that define the position of tiles
		self.x = x
		self.y = y
		self.pos = (x, y)
		self.tile_width = tile_width
		self.tile_height = tile_height
		self.abs_x = x * tile_width
		self.abs_y = y * tile_height
		self.abs_pos = (self.abs_x, self.abs_y)
        
        # Defines the color of the piece, depending on its position
		self.color = bege if (x + y) % 2 == 0 else brown
		self.draw_color = bege if self.color == bege else brown
		self.highlight_color = possible_moves_color if self.color == bege else possible_moves_color
		self.occupying_piece = None
		self.coord = self.get_coord()
		self.highlight = False
		self.rect = pygame.Rect(
			self.abs_x,
			self.abs_y,
			self.tile_width,
			self.tile_height)

	def get_coord(self): # Defines a coordinate matrix
		columns = 'abcdefgh'
		return columns[self.x] + str(self.y + 1)

	def draw(self, display): # Draws the squares using pygame
		if self.highlight:
			pygame.draw.rect(display, self.highlight_color, self.rect)
		else:
			pygame.draw.rect(display, self.draw_color, self.rect)

		if self.occupying_piece != None:
			centering_rect = self.occupying_piece.img.get_rect()
			centering_rect.center = self.rect.center
			display.blit(self.occupying_piece.img, centering_rect.topleft)

class Piece: # Defines the general appearance and behavior of the game pieces.
	def __init__(self, x, y, color, board): # Defines the position of the pieces
		self.x = x
		self.y = y
		self.pos = (x, y)
		self.board = board
		self.color = color

    # Using Encapsulation - the method is only accessible within the class and sub-classes:
	def _move(self, tile): # Defines how pieces can move around the board and how they are promoted to queen
		for i in self.board.tile_list:
			i.highlight = False

		if tile in self.valid_moves() and not self.board.is_jump:
			prev_tile = self.board.get_tile_from_pos(self.pos)
			self.pos, self.x, self.y = tile.pos, tile.x, tile.y

			prev_tile.occupying_piece = None
			tile.occupying_piece = self
			self.board.selected_piece = None
			self.has_moved = True
   
			# Pawn promotion
			if self.notation == 'p':
				if self.y == 0 or self.y == 7:
					tile.occupying_piece = King(self.x, self.y, self.color, self.board)
					playsound('sounds/' + "king.wav")
			return True

		elif self.board.is_jump:
			for move in self.valid_jumps():
				if tile in move:
					prev_tile = self.board.get_tile_from_pos(self.pos)
					jumped_piece = move[-1]
					self.pos, self.x, self.y = tile.pos, tile.x, tile.y

					prev_tile.occupying_piece = None
					jumped_piece.occupying_piece = None
					tile.occupying_piece = self
					self.board.selected_piece = None
					self.has_moved = True

					# Pawn promotion
					if self.notation == 'p':
						if self.y == 0 or self.y == 7:
							tile.occupying_piece = King(self.x, self.y, self.color, self.board)
							playsound('sounds/' + "king.wav")
					return True
		else:
			self.board.selected_piece = None
			return False

class King(Piece): # Defines the general appearance and behavior of pieces promoted to queen.
	def __init__(self, x, y, color, board): # Defines the appearance of pieces promoted to queen
		super().__init__(x, y, color, board)
		img_path = f'images/{color}-king.tif'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (50, 50))
		self.notation = 'k'

	def _possible_moves(self): # Defines the possible movements of a piece promoted to king
		possible_moves = ((-1, -1), (+1, -1), (-1, +1), (+1, +1))
		return possible_moves

	def valid_moves(self): # Defines the movements that a piece promoted to king can do
		tile_moves = []
		moves = self._possible_moves()
		for move in moves:
			tile_pos = (self.x + move[0], self.y + move[-1])
			if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
				pass
			else:
				tile = self.board.get_tile_from_pos(tile_pos)
				if tile.occupying_piece == None:
					tile_moves.append(tile)
		return tile_moves

	def valid_jumps(self): # Defines the actual jumps that a piece promoted to king can do
		tile_jumps = []
		moves = self._possible_moves()
		for move in moves:
			tile_pos = (self.x + move[0], self.y + move[-1])
			if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
				pass
			else:
				tile = self.board.get_tile_from_pos(tile_pos)
				if self.board.turn == self.color:
					if tile.occupying_piece != None and tile.occupying_piece.color != self.color:
						next_pos = (tile_pos[0] + move[0], tile_pos[-1] + move[-1])
						next_tile = self.board.get_tile_from_pos(next_pos)		
						if next_pos[0] < 0 or next_pos[0] > 7 or next_pos[-1] < 0 or next_pos[-1] > 7:
							pass
						else:
							if next_tile.occupying_piece == None:
								tile_jumps.append((next_tile, tile))
		return tile_jumps

class Pawn(Piece): # Defines the general appearance and behavior of pieces not promoted to queen ("normal pieces").
	def __init__(self, x, y, color, board):
		super().__init__(x, y, color, board)
		img_path = f'images/{color}-pawn.tif'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (50, 50))
		self.notation = 'p'

	def _possible_moves(self): # Defines the possible movements of a "normal piece"
		# (x, y) define the left and right movements
		if self.color == "red":
			possible_moves = ((-1, -1), (+1, -1)) 
		else:
			possible_moves = ((-1, +1), (+1, +1))
		return possible_moves

	def valid_moves(self): # Defines the movements that a "normal piece" can do
		tile_moves = []
		moves = self._possible_moves()
		for move in moves:
			tile_pos = (self.x + move[0], self.y + move[-1])
			if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
				pass
			else:
				tile = self.board.get_tile_from_pos(tile_pos)
				if tile.occupying_piece == None:
					tile_moves.append(tile)
		return tile_moves

	def valid_jumps(self): # Defines the actual jumps that a "normal piece" can do
		tile_jumps = []
		moves = self._possible_moves()
		for move in moves:
			tile_pos = (self.x + move[0], self.y + move[-1])
			if tile_pos[0] < 0 or tile_pos[0] > 7 or tile_pos[-1] < 0 or tile_pos[-1] > 7:
				pass
			else:
				tile = self.board.get_tile_from_pos(tile_pos)
				if self.board.turn == self.color:
					if tile.occupying_piece != None and tile.occupying_piece.color != self.color:
						next_pos = (tile_pos[0] + move[0], tile_pos[-1] + move[-1])
						next_tile = self.board.get_tile_from_pos(next_pos)		
						if next_pos[0] < 0 or next_pos[0] > 7 or next_pos[-1] < 0 or next_pos[-1] > 7:
							pass
						else:
							if next_tile.occupying_piece == None:
								tile_jumps.append((next_tile, tile))
		return tile_jumps

class Board: # Defines the properties of the game board itself.
	def __init__(self,tile_width, tile_height, board_size):
		self.tile_width = tile_width
		self.tile_height = tile_height
		self.board_size = board_size
		self.selected_piece = None

		self.turn = "red" # This oOption sets who starts the game "red" or "black" 
		self.is_jump = False

		self.config = [
			['', 'bp', '', 'bp', '', 'bp', '', 'bp'],
			['bp', '', 'bp', '', 'bp', '', 'bp', ''],
			['', 'bp', '', 'bp', '', 'bp', '', 'bp'],
			['', '', '', '', '', '', '', ''],
			['', '', '', '', '', '', '', ''],
			['rp', '', 'rp', '', 'rp', '', 'rp', ''],
			['', 'rp', '', 'rp', '', 'rp', '', 'rp'],
			['rp', '', 'rp', '', 'rp', '', 'rp', '']
		]

		self.tile_list = self._generate_tiles()
		self._setup()

	def _generate_tiles(self): # Defines how tiles are generated
		output = []
		for y in range(self.board_size):
			for x in range(self.board_size):
				output.append(
					Tile(x,  y, self.tile_width, self.tile_height)
				)
		return output

	def get_tile_from_pos(self, pos): # Defines the tile position
		for tile in self.tile_list:
			if (tile.x, tile.y) == (pos[0], pos[1]):
				return tile

	def _setup(self): # Defines their setup
		for y_ind, row in enumerate(self.config):
			for x_ind, x in enumerate(row):
				tile = self.get_tile_from_pos((x_ind, y_ind))
				if x != '':
					if x[-1] == 'p':
						color = 'red' if x[0] == 'r' else 'black'
						tile.occupying_piece = Pawn(x_ind, y_ind, color, self)

	def handle_click(self, pos): # Defines what pieces can be clicked on
		x, y = pos[0], pos[-1]
		if x >= self.board_size or y >= self.board_size:
			x = x // self.tile_width
			y = y // self.tile_height
		clicked_tile = self.get_tile_from_pos((x, y))

		if self.selected_piece is None:
			if clicked_tile.occupying_piece is not None:
				if clicked_tile.occupying_piece.color == self.turn:
					self.selected_piece = clicked_tile.occupying_piece
		elif self.selected_piece._move(clicked_tile):
			if not self.is_jump:
				self.turn = 'red' if self.turn == 'black' else 'black'
			else:
				if len(clicked_tile.occupying_piece.valid_jumps()) == 0:
					self.turn = 'red' if self.turn == 'black' else 'black'
		elif clicked_tile.occupying_piece is not None:
			if clicked_tile.occupying_piece.color == self.turn:
				self.selected_piece = clicked_tile.occupying_piece

	def draw(self, display): # Draws highlights of the pieces clicked on
		if self.selected_piece is not None:
			self.get_tile_from_pos(self.selected_piece.pos).highlight = True
			if not self.is_jump:
				for tile in self.selected_piece.valid_moves():
					tile.highlight = True
			else:
				for tile in self.selected_piece.valid_jumps():
					tile[0].highlight = True

		for tile in self.tile_list:
			tile.draw(display)

class Game: # Defines the general rules of the game and what actions should be triggered when events such as the end of the game happen.
    def __init__(self): # Sets that at the beginning, there's no winner and no available pieces to jump
        self.winner = None
        self.is_jump = False

    def reset_game(self): # When the game is resetted, self.winner it's defined again to "None"
        self.winner = None

    def check_piece(self, board):
        red_piece = 0
        black_piece = 0
        for y in range(board.board_size):
            for x in range(board.board_size):
                tile = board.get_tile_from_pos((x, y))
                if tile.occupying_piece is not None:
                    if tile.occupying_piece.color == "red":
                        red_piece += 1
                    else:
                        black_piece += 1
        return red_piece, black_piece

    def is_game_over(self, board): # Check if the game is over
        red_piece, black_piece = self.check_piece(board)
        if red_piece == 0 or black_piece == 0:
            self.winner = "Red" if red_piece > black_piece else "Black"
            return True
        else:
            return False
        
    def check_jump(self, board): # Check if a piece can jump
        piece = None
        for tile in board.tile_list:
            if tile.occupying_piece is not None:
                piece = tile.occupying_piece
                if len(piece.valid_jumps()) != 0 and board.turn == piece.color:
                    board.is_jump = True
                    break
                else:
                    board.is_jump = False
        if board.is_jump:
            board.selected_piece = piece
            board.handle_click(piece.pos)
        return board.is_jump

    def message(self, winner_name, loser_name, screen): # Defines what to do when the game ends - it shows a message in the screen and in the console
        playsound('sounds/' + "game_end.wav") 
        print(f"{winner_name} Wins! \U0001F4AA \n")
        self.save_winner_to_file(winner_name, loser_name)

        font = pygame.font.Font("fonts/font.ttf", 50)
        text_surface = font.render(f"{winner_name} Wins!", True, (255, 255, 255))
        pygame.draw.rect(screen, (186, 196, 200), (70, 230, 625, 300))
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        pygame.time.wait(4000)

    def save_winner_to_file(self, winner_name, loser_name): # It stores the date of the winner and loser && day + hour when the game occurred
        with open("winner.txt", "a") as file:
            today = date.today()
            formatted_date = today.strftime("%d-%m-%Y")  # Format the date as day-month-year
            c = datetime.now()
            current_time = c.strftime('%H:%M:%S')
            file.write(f" In the day {formatted_date}, at {current_time}, '{winner_name}' beat '{loser_name}'!\n")

class Checkers: # Defines how the game runs, using pygame.
    def __init__(self, screen): # Initial defitions of the screen
        self.screen = screen
        self.running = True
        self.FPS = pygame.time.Clock()
        self.game = None 

    def _draw(self, board): # Draw the screen with the parameters set
        board.draw(self.screen)
        pygame.display.update()

    def main(self, window_width, window_height = None): # Establishes the game flow on the screen and how it should be updated
        if window_height == None:
            window_height = window_width
        
        self.game = Game()
        board_size = 8
        tile_width, tile_height = window_width // board_size, window_height // board_size
        board = Board(tile_width, tile_height, board_size)
        while self.running:
            self.game.check_jump(board)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if not self.game.is_game_over(board):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board.handle_click(event.pos) 
                else:
                    self.game.message(player1_name if self.game.winner == 'Red' else player2_name,
                                    player2_name if self.game.winner == 'Red' else player1_name, screen)
                    self.game.reset_game()
                    main_menu(self.screen)

            self._draw(board)
            self.FPS.tick(60)


# Starting the game - and menu "creators"

print("\nGame started! \U0001F60E \n")
player1_name, player2_name = "", ""

def exit_game(): # Quit the game, when it is clicked on the "quit" option or on the cross in the window
    playsound('sounds/' + "click.wav") # Together with the sound of the exit click it makes a different sound (there is duplication of sounds) - I liked the effect, that's why the invocation of the sound appears repeated
    pygame.quit() # Uninitialize all pygame modules
    sys.exit() # Exit the script and stop the Python program
    
def main_menu(screen): # The first menu appearing
    pygame.display.set_caption("Checkers game | made by JC") # Set the caption title
    clock = pygame.time.Clock() # Controls the game's FPS

    while True: # To select options with a mouse click, the mouse coordinates are used
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game() # Calls the exit_game function, which calls another, "pygame.quit()" - if you click on the window to close, the game closes.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # If something it's clicked, the event it's activated:
                    x, y = event.pos # Assign x and y to the tuple "event.pos"
                    if 230 <= x <= 530 and 200 <= y <= 250:
                        playsound('sounds/' + "click.wav")
                        print ("\nLet's play! \U0001F3AE\n")
                        second_menu(screen) # Go to the second menu (call the second_menu method)
                    elif 230 <= x <= 530 and 300 <= y <= 350:
                        playsound('sounds/' + "click.wav")
                        exit_game() # The game closes because the area corresponding to the "quit" button has been clicked
                    elif 600 <= x <= 800 and 500 <= y <= 800:
                        playsound('sounds/' + "click.wav")
                        stats_menu(screen)

        screen.fill((255, 255, 255)) # Fill the screen created in the main method (__name__) with a solid color (in this case, 255,255, 255 - which is the RGB code for the color white)
        font = pygame.font.Font("fonts/font.ttf", 50) # Import the text font contained in the folder
        my_text = font.render("Jogo das Damas | made by JC", True, "black") # Create the game title (appears in the menu window)
        screen.blit(my_text, (75, 90)) # "Draw" the name with the my_text object, which has its own font and its own message, (x, position)


        pygame.draw.rect(screen, (186, 196, 200), (230, 200, 300, 50)) # Draw the first box, (R,G,B), X,Y, size horizontally, size vertically)
        draw_text(screen, "Start the game!", 30, 380, 225, (10, 20, 110)) # (Surface you will draw on, string to display, font size, x position, y position, (colors, in rgb) )

        pygame.draw.rect(screen, (186, 196, 200), (230, 300, 300, 50))
        draw_text(screen, "Quit", 30, 380, 325, (10, 20, 110))
        screen.blit(pygame_main_menu, (230, 407)) # (image source, (movement along x, movement along y))
        
        pygame.draw.rect(screen, (186, 196, 200), (590, 625, 100, 50)) # Where will you draw, (R,G,B) (X,Y, size horizontally, size vertically)
        draw_text(screen, "Stats", 30, 640, 650, (10, 20, 110)) # (Surface you will draw on, string to display, font size, x position, y position, (colors, in rgb) )

        pygame.display.flip() # This will update the contents of the entire display
        clock.tick(60)  # Game's FPS - it's used to refresh the frame in given second
      
def get_player_names(player): # This get the names of the players, by creating input boxes
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Defining player's names")

    font_title = pygame.font.Font("fonts/font.ttf", 36)
    font_input = pygame.font.Font("fonts/font.ttf", 24)
    
    if player=="player1":
    	title_text = font_title.render("Player 1: Choose a nickname and press ENTER.", True, "black")

    if player=="player2":
    	title_text = font_title.render("Player 2: Choose a nickname and press ENTER.", True, "black")	

    input_rect = pygame.Rect(275, 200, 300, 50)
    color_inactive = pygame.Color("black")
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((255, 255, 255))
        screen.blit(title_text, (50, 50))
        txt_surface = font_input.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_rect.w = width
        screen.blit(txt_surface, (input_rect.x+5, input_rect.y+5))
        pygame.draw.rect(screen, color, input_rect, 2)

        pygame.display.flip()
        clock.tick(30)

def second_menu(screen): # Sets the second menu
    pygame.display.set_caption("Checkers game | made by JC - Pick up a mode. ;)")
    clock = pygame.time.Clock()

    global player1_name, player2_name 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if 230 <= x <= 530 and 200 <= y <= 250:
                        print("\U0001F9B8 vs. \U0001F9B9 it is!\n")
                        playsound('sounds/' + "click.wav")
                        # Obtem os nomes dos jogadores
                        player1_name = get_player_names("player1")
                        player2_name = get_player_names("player2")
                        playsound('sounds/' + "game_start.wav")
                        board(screen)
                    elif 230 <= x <= 530 and 300 <= y <= 350:
                        print("\U0001F9B8 vs. \U0001F916 it is!\n")
                        # Obtem os nomes dos jogadores
                        player1_name = get_player_names("player1")
                        player2_name = "Computer"
                        playsound('sounds/' + "game_start.wav")
                        board(screen)
                    elif 230 <= x <= 530 and 400 <= y <= 450:
                        playsound('sounds/' + "click.wav")
                        main_menu(screen)  # Back to main_menu

        screen.fill((255, 255, 255))
        draw_text(screen, "Pick up a mode!", 50, window_width // 2, 100, (0, 0, 0))

        pygame.draw.rect(screen, (186, 196, 200), (230, 200, 300, 50))
        draw_text(screen, "1 vs. 1", 30, 380, 225, (10, 20, 110))

        pygame.draw.rect(screen, (186, 196, 200), (230, 300, 300, 50))
        draw_text(screen, "1 vs. Computer", 30, 380, 325, (10, 20, 110))

        pygame.draw.rect(screen, (186, 196, 200), (230, 400, 300, 50))
        draw_text(screen, "Back", 30, 380, 425, (10, 20, 110))

        pygame.display.flip()
        clock.tick(60)
 
def stats_menu(screen): # Creates a stats screen

    font_title = pygame.font.Font("fonts/font.ttf", 36)
    font_menu = pygame.font.Font("fonts/font.ttf", 16)

    with open("winner.txt", "r") as file: # Reading the .txt file
        data = file.readlines()
    
    tela_dados = pygame.display.set_mode((window_width, window_height))# Windows configuration
    pygame.display.set_caption("Game stats")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    x, y = event.pos 
                    if 600 <= x <= 800 and 500 <= y <= 800:
                        playsound('sounds/' + "click.wav")
                        main_menu(screen)		

        tela_dados.fill((255, 255, 255))  # Fills the screen with white

        for i, linha in enumerate(data):
            texto = font_menu.render(f"{i}. {linha.strip()}", True, (0, 0, 0))
            tela_dados.blit(texto, (50, 90 + i * 40)) 
        

        my_text = font_title.render("Stats of the latest games", True, "black")
        tela_dados.blit(my_text, (190, 20))

        pygame.draw.rect(tela_dados, (186, 196, 200), (590, 625, 100, 50)) 
        draw_text(tela_dados, "Back", 30, 640, 650, (10, 20, 110)) 
        pygame.display.flip()
    
def board(screen):
    pygame.init()

    window_size = (760, 760)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Jogo das Damas | made by JC")

    checkers = Checkers(screen)
    checkers.main(window_size[0], window_size[1]) # Read checkers as tupple so window_size must be given as (x,y)
    # Here, after the game ends, it restarts the game before returning to the main menu
    checkers.game.reset_game()
    main_menu(screen) 
    
def draw_text(surface, text, size, x, y, color): # Draw the "first screen"
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

if __name__ == '__main__': # The if __name__ == "__main__": statement checks if the script is being run as the main program.
    pygame.init()
    window_width, window_height = 760, 760 # Defines the width and height of the screen
    screen = pygame.display.set_mode((window_width, window_height)) # This function will create a display Surface. set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
    pygame.display.set_caption("Checkers game | made by JC") 
    main_menu(screen) # Call/create the main menu