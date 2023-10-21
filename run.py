# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pyfiglet

WELCOME = pyfiglet.figlet_format("Welcome to Battleship!")
#RULES = You can find the rules for Battleship 

def starting_question():
    start = input("Do you want to start the game (y/n)?")
    return start
 

def board_creation():
    """Create boards for the game battleship"""
    board = [
        [" ", 1, 2, 3, 4, 5, 6], 
        ["a", " ", " ", " ", " ", " ", ],
        ["b", " ", " ", " ", " ", " ", ],
        ["c", " ", " ", " ", " ", " ", ],
        ["d", " ", " ", " ", " ", " ", ],
        ["e", " ", " ", " ", " ", " ", ],
        ["f", " ", " ", " ", " ", " ", ],
        ]
    return board

def print_board(board):
    """Give game boards the proper styling"""
    print(f"|---------------------|")
    print(f"|{board[0][0]}|{board[0][1]}|{board[0][2]}|{board[0][3]}|{board[0][4]}|{board[0][5]}|{board[0][6]}|")
    print(f"|---------------------|")
    print(f"|{board[1][0]}|{board[1][1]}|{board[1][2]}|{board[1][3]}|{board[1][4]}|{board[1][5]}|{board[1][6]}|")
    print(f"|---------------------|")
    print(f"|{board[2][0]}|{board[2][1]}|{board[2][2]}|{board[2][3]}|{board[2][4]}|{board[2][5]}|{board[2][6]}|")
    print(f"|---------------------|")
    print(f"|{board[3][0]}|{board[3][1]}|{board[3][2]}|{board[3][3]}|{board[3][4]}|{board[3][5]}|{board[3][6]}|")
    print(f"|---------------------|")
    print(f"|{board[4][0]}|{board[4][1]}|{board[4][2]}|{board[4][3]}|{board[4][4]}|{board[4][5]}|{board[4][6]}|")
    print(f"|---------------------|")
    print(f"|{board[5][0]}|{board[5][1]}|{board[5][2]}|{board[5][3]}|{board[5][4]}|{board[5][5]}|{board[5][6]}|")
    print(f"|---------------------|")
    print(f"|{board[6][0]}|{board[6][1]}|{board[6][2]}|{board[6][3]}|{board[6][4]}|{board[6][5]}|{board[6][6]}|")
    print(f"|---------------------|")



#def start_game():
    #try:
        #if input == y:

       # else:
    #except:
        

def main():
    print(WELCOME)
    starting_question()
    #print(RULES)
    board = board_creation()
    #board2 = board_creation()
    #print_board(board1)
    print_board(board)
    #print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")


main()
