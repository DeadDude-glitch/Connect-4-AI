from game import *
import pygame
import math
from AI import *
from sys import exit
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
			if g.board.slots[row][col] == player.P1_piece:
				pygame.draw.circle(screen, RED, (int(col*SQUARESIZE+SQUARESIZE/2), height-int(row*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif g.board.slots[row][col] == player.P2_piece: 
				pygame.draw.circle(screen, YELLOW, (int(col*SQUARESIZE+SQUARESIZE/2), height-int(row*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

# game initialization
pygame.init()
draw_board(game)
pygame.display.update()

# game loop
while not game.over:

# interactive GUI on the player's turn
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if game.currentPlayer() is player.P1_piece:
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

		pygame.display.update()

		# input action is taken from user
		if event.type == pygame.MOUSEBUTTONDOWN:
			# draw black box 
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			# Ask for Player Input
			if game.currentPlayer() is player.P1_piece:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if game.turn(col):
					if game.winning_move():
						label = myfont.render("Player 1 wins!!", 1, RED)
						screen.blit(label, (40,10))
						game.over = True

					game.board.show()
					draw_board(game)


	# # Non reactive AI player turn
	if game.currentPlayer() is player.P2_piece and not game_over:				
		col, minimax_score = minimax(game, 5, -math.inf, math.inf, True)

		if game.turn(col):
			if game.winning_move(player.P2_piece):
				label = myfont.render("Player 2 wins!!", 1, YELLOW)
				screen.blit(label, (40,10))
				game_over = True

			game.board.show()
			draw_board(game)

	if game_over:
		pygame.time.wait(3000)
