import numpy as np
from actor import player
# an numpy array that represent a connect four board
# this module should be independent

class Board:
    # board creation
    def __init__(self, rows:int=6, columns:int=7) -> None:
        self.rows = int(rows)
        self.columns = int(columns)
        self.slots = np.full((self.rows,self.columns), fill_value=player.empty_piece)

    def is_full(self) -> bool:
        # loop on the top column (inverted)
        # find one empty slot
        for value in self.slots[-1]:
            if value == 0: return False
        return True 

    def is_valid_location(self, col:int) -> bool:
        return self.slots[self.rows-1][col] == 0
    
    
    # find the index of the next open row
    def get_next_open_row(self, col:int) -> int:
        for row in range(0,self.rows):
            if self.slots[row][col] == 0: 
                return int(row)
    
    def drop_piece(self, col:int, value:player) -> bool: 
        if self.is_valid_location(col):
            self.slots[self.get_next_open_row(col)][col] = value
            return True
        return False
    
    # veiw the board on the CLI
    def show(self):
        print(np.flip(self.slots, 0))
        
        
if __name__ == "__main__":
    print(Board().slots)
