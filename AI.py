from game import *
import random
import math

WINDOW_LENGTH = 4

def get_valid_locations(game:game):
        valid_locations = []
        for col in range(game.board.columns):
            if game.board.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

def is_terminal_node(game:game):
	return game.winning_move(player.P1_piece) or game.winning_move(player.P2_piece) or len(get_valid_locations(game)) == 0

def score_position(game:game, piece:player):
	score = 0

	## Score Center Column
	center_array = [int(i) for i in list(game.board.slots[:, game.board.columns//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(game.board.rows):
		row_array = [int(i) for i in list(game.board.slots[r,:])]
		for c in range(game.board.columns-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(game.board.columns):
		col_array = [int(i) for i in list(game.board.slots[:,c])]
		for r in range(game.board.rows-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Posiive Sloped Diagonal
	for r in range(game.board.rows-3):
		for c in range(game.board.columns-3):
			window = [game.board.slots[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	for r in range(game.board.rows-3):
		for c in range(game.board.columns-3):
			window = [game.board.slots[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	return score
 

def evaluate_window(piece:player, window:int=4):
	score = 0
	opp_piece = player.P1_piece
	if piece == player.P1_piece:
		opp_piece = player.P2_piece

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(player.empty_piece) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(player.empty_piece) == 2:
		score += 2
	if window.count(opp_piece) == 3 and window.count(player.empty_piece) == 1:
		score -= 4
	return score
 
def pick_best_move(game:game, piece:player):
	valid_locations = get_valid_locations(game.board)
	best_score = -10000
	best_col = random.choice(valid_locations)
	for col in valid_locations:
		row = game.board.get_next_open_row(col)
		temp_board = game.board.copy()
		game.board.drop_piece(temp_board, row, col, piece)
		score = score_position(temp_board, piece)
		if score > best_score:
			best_score = score
			best_col = col
	return best_col



def minimax(game:game, depth:int, alpha, beta, maximizingPlayer):
	valid_locations = get_valid_locations(game)
	is_terminal = is_terminal_node(game)
	if depth == 0 or is_terminal:
		if is_terminal:
			if game.winning_move(player.P2_piece):
				return (None, 100000000000000)
			elif game.winning_move(player.P1_piece):
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_position(game, player.P2_piece))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = game.board.get_next_open_row(col)
			b_copy = game
			game.board.drop_piece(b_copy, row, col, player.P2_piece)
			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value
