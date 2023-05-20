from board import *
from enum import Enum

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

    def currentPlayer(self) -> int:
        if self.turn_counter % 2 == 0: 
            return 1
        return -1
    
    def turn(self, col:int=-1):
        if not col in range(0, self.board.columns-1): 
            print(f"Index Out Of Range (0-{self.board.columns-1})")
            return False
        self.board.drop_piece(col, self.currentPlayer())
        if self.winning_move(self.currentPlayer): 
            print("GAMEOVER")
        self.turn_counter += 1
        return True

    def winning_move(self, piece:player) -> bool:
        # Check horizontal win
        for c in range(self.board.columns-3):
            for r in range(self.board.rows):
                if (    self.board[r][c]   == piece 
                    and self.board[r][c+1] == piece 
                    and self.board[r][c+2] == piece 
                    and self.board[r][c+3] == piece
                ): return True
        
        # Check vertical win 
        for c in range(self.board.columns):
            for r in range(self.board.rows-3): 
                if (	self.board[r][c]   == piece 
                    and self.board[r+1][c] == piece 
                    and self.board[r+2][c] == piece 
                    and self.board[r+3][c] == piece 
                ): return True
        
        # Check diagonal win
        
        # negative slope  \
        for c in range(self.board.columns-3):
       	    for r in range(self.board.rows-3):
               if (     self.board[r][c]     == piece 
                    and self.board[r+1][c+1] == piece 
                    and self.board[r+2][c+2] == piece 
                    and self.board[r+3][c+3] == piece
                ): return True
		
  # positive slope  /
        for c in range(self.board.columns-3):
            for r in range(3, self.board.rows):
                if (	self.board[r][c]     == piece 
                    and self.board[r-1][c+1] == piece 
                    and self.board[r-2][c+2] == piece 
                    and self.board[r-3][c+3] == piece
                ): return True



if __name__ == "__main__": 
    test = game()
    tmp = 0 
    print(test.board.show())
    while not test.over:
        test.board.show()
        test.turn(int(input("")))