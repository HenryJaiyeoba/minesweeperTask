import random
import re

class Minesweeper:
    def __init__(self, mine_size,bomb_no):
        self.mine_size = mine_size
        self.bomb_no = bomb_no
        
        self.dug = set()
        self.board = self.make_board()
        self.assign_values()
        
    def make_board(self):
        board = [[None for _ in range(self.mine_size)]for _ in range(self.mine_size)]

            # plant bombs
        mine_planted = 0
        while mine_planted < self.bomb_no:
            pos = random.randint(0,self.mine_size**2-1)
            row = pos // self.mine_size
            col = pos % self.mine_size
            if board[row][col] == "*":
                continue
            board[row][col] = "*"
            mine_planted+=1
        return board
    
    def assign_values(self):
        for rid in range(self.mine_size):
            # print("------------")
            for cid in range(self.mine_size):
                if self.board[rid][cid] != "*":
                    self.board[rid][cid] = self.no_of_neighbour_mines(rid,cid)
                    # print(x[rid][cid], end=",")
                else:
                    self.board[rid][cid] = "*"
                    # print(x[rid][cid], end=",")
        # print("")
    
    def no_of_neighbour_mines(self,row,col):
        no_of_mines = 0
        for r in range(max(0,row-1),min(self.mine_size-1,row+1)+1):
            for c in range(max(0,col-1),min(self.mine_size-1,col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == "*":
                    no_of_mines+=1
        return no_of_mines

    def dig(self, row, col):
        self.dug.add((row,col))
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        else:
            for r in range(max(0,row-1),min(self.mine_size-1,row+1)+1):
                for c in range(max(0,col-1),min(self.mine_size-1,col+1)+1):
                    if (r,c) in self.dug:
                        continue
                    else:
                        self.dig(r,c)

            return True
    
    def current_board(self):
        play_board = [[None for _ in range(self.mine_size)]for _ in range(self.mine_size)]
        for row in range(self.mine_size):
            for col in range(self.mine_size):
                if (row,col) in self.dug:
                    play_board[row][col] = self.board[row][col]
                else:
                    play_board[row][col] = "x"
        return play_board
    
    def answer(self):
        for r in self.board:
            for c in r:
                print(c, end=",")
            print("")

game_size = int(input("Please the size for the minesweeper: "))
no_of_bombs = int(input("Please input the number of bombs you want in the minesweeper: "))
def play(size=9,bomb_no=10):
    # initialize the game 
    game = Minesweeper(size,bomb_no)
    board = game.board
    correct = True
    while len(game.dug) < game.mine_size **2-bomb_no:
        # print(game)
        current_board = game.current_board()
        for r in current_board:
            for c in r:
                print(c, end=",")
            print("")
        # print(board)
        user_input = input("Please input the position youd like to play in (sample: r,c):")
        inputed = re.split(",(\\s)*", user_input)
        # print(inputed)
        first_value = int(inputed[0])
        last_value = int(inputed[-1])
        user_row, user_col = first_value, last_value
        # print(user_row,user_col)
        # Check if valid
        if user_row < 0 or user_row > game.mine_size or user_col < 0 or user_col > game.mine_size:
            print("❗️INVALID LOCATION")
            continue
        # if valid
        correct = game.dig(user_row,user_col)
        if not correct:
            # print("💥GAME OVER, YOU DUG A BOMB")
            break
    if correct:
        print("🎉 CONGRATULATIONS YOU WON")
    else:
        print("💥GAME OVER, YOU DUG A BOMB")
        game.answer()


play(game_size, no_of_bombs)
        
         