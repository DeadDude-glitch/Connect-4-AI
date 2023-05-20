from game import *
import pygame
import math

# one time initialized object
game = game()

# GUI Parameters
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
width = game.board.columns * SQUARESIZE
height = (game.board.rows+1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 75)

# GUI colors
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)


def draw_board(g: game):
	for col in range(g.board.columns):
		for row in range(g.board.rows):
			pygame.draw.rect(screen, BLUE, (col*SQUARESIZE, row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(col*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for col in range(g.board.columns):
		for row in range(g.board.rows):		
			if g.board[row][col] == player.P1_piece:
				pygame.draw.circle(screen, RED, (int(col*SQUARESIZE+SQUARESIZE/2), height-int(row*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif g.board[row][col] == player.P2_piece: 
				pygame.draw.circle(screen, YELLOW, (int(col*SQUARESIZE+SQUARESIZE/2), height-int(row*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

# game initialization
pygame.init()
draw_board(game)
pygame.display.update()

# game loop
while not game.over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == PLAYER:
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			#print(event.pos)
			# Ask for Player 1 Input
			if turn == PLAYER:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, PLAYER_PIECE)

					if winning_move(board, PLAYER_PIECE):
						label = myfont.render("Player 1 wins!!", 1, RED)
						screen.blit(label, (40,10))
						game_over = True

					turn += 1
					turn = turn % 2

					print_board(board)
					draw_board(board)


	# # Ask for Player 2 Input
	if turn == AI and not game_over:				
		col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

		if is_valid_location(board, col):
			row = get_next_open_row(board, col)
			drop_piece(board, row, col, AI_PIECE)

			if winning_move(board, AI_PIECE):
				label = myfont.render("Player 2 wins!!", 1, YELLOW)
				screen.blit(label, (40,10))
				game_over = True

			print_board(board)
			draw_board(board)

			turn += 1
			turn = turn % 2

	if game_over:
		pygame.time.wait(3000)