from board import *
from enum import Enum

# a once initialized object that represent a connect four game
# this module should depend only on board module
# all actions should be simplified in a function

# constant player values
class player(Enum):
    P1_piece =  1   # human
    P2_piece = -1   # machine
    empty_piece = 0 # vacant

# game controlling object
class game:
    # constructor
    def __init__(self) -> None:
        self.over = False
        self.board = Board()
        self.turn_counter = 0

    def currentPlayer(self) -> player:
        if self.turn_counter % 2 == 0: 
            return player.P1_piece
        return player.P2_piece
    
    # let player take his turn and return if turn is taken successfully
    def turn(self, col:int=-1) -> bool:
        if not col in range(0, self.board.columns-1): 
            print(f"Index Out Of Range (0-{self.board.columns-1})")
            return False
        self.board.drop_piece(col, self.currentPlayer())
        if self.winning_move(): 
            print("GAMEOVER")
        self.turn_counter += 1
        return True

    # scans the entire board for 4 consecutive similar pieces
    def winning_move(self) -> bool:
        # Check horizontal win
        piece = self.currentPlayer()
        for c in range(self.board.columns-3):
            for r in range(self.board.rows):
                if (    self.board.slots[r][c]   == piece 
                    and self.board.slots[r][c+1] == piece 
                    and self.board.slots[r][c+2] == piece 
                    and self.board.slots[r][c+3] == piece
                ): return True
        
        # Check vertical win 
        for c in range(self.board.columns):
            for r in range(self.board.rows-3): 
                if (	self.board.slots[r][c]   == piece 
                    and self.board.slots[r+1][c] == piece 
                    and self.board.slots[r+2][c] == piece 
                    and self.board.slots[r+3][c] == piece 
                ): return True
        
        # Check diagonal win
        
        # negative slope  \
        for c in range(self.board.columns-3):
       	    for r in range(self.board.rows-3):
               if (     self.board.slots[r][c]     == piece 
                    and self.board.slots[r+1][c+1] == piece 
                    and self.board.slots[r+2][c+2] == piece 
                    and self.board.slots[r+3][c+3] == piece
                ): return True
		
        # positive slope  /
        for c in range(self.board.columns-3):
            for r in range(3, self.board.rows):
                if (	self.board.slots[r][c]     == piece 
                    and self.board.slots[r-1][c+1] == piece 
                    and self.board.slots[r-2][c+2] == piece 
                    and self.board.slots[r-3][c+3] == piece
                ): return True



if __name__ == "__main__": 
    test = game()
    tmp = 0 
    print(test.board.show())
    while not test.over:
        test.board.show()
        test.turn(int(input("")))
