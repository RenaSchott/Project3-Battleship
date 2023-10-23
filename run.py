import pyfiglet
from random import randint
import sys

# Inspired by https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
WELCOME = pyfiglet.figlet_format("Welcome to Battleship!")


# Inspired by https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/
def display_homepage():
    """Starting question asked"""
    start = input("Do you want to start the game (y/n)?")
    try:
        if start == "y":
            print(f"Have fun!")
        elif start == "n":
            print("Sadly, you won't play the game")
            sys.exit(0)
        elif start == "":
            print ("You had to answer the question. Please restart the game.")
            sys.exit(0)
    except ValueError as e: 
        print("Only y or n are allowed") 
        sys.exit(0)
    return start


def get_username():
    """Ask for the username"""
    username = input("A name is needed for playing the game. What is your name?")
    if username == "":
        print ("A username is needed for playing the game. Please restart the game.")
        sys.exit(0)
    return username


# Inspired by https://www.youtube.com/watch?v=RqCZBbfd9Fw
def create_board():
    """Create boards for the game battleship"""
    board = [
        [" ", 1, 2, 3, 4, 5, 6], 
        ["a", " ", " ", " ", " ", " ", " ",],
        ["b", " ", " ", " ", " ", " ", " ",],
        ["c", " ", " ", " ", " ", " ", " ",],
        ["d", " ", " ", " ", " ", " ", " ",],
        ["e", " ", " ", " ", " ", " ", " ",],
        ["f", " ", " ", " ", " ", " ", " ",],
        ]
    return board


# Inspired by https://www.youtube.com/watch?v=RqCZBbfd9Fw
def print_board(board):
    """Give game boards the proper styling"""
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]} | {board[0][5]} | {board[0][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]} | {board[1][5]} | {board[1][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]} | {board[2][5]} | {board[2][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]} | {board[3][5]} | {board[3][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]} | {board[4][5]} | {board[4][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[5][0]} | {board[5][1]} | {board[5][2]} | {board[5][3]} | {board[5][4]} | {board[5][5]} | {board[5][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[6][0]} | {board[6][1]} | {board[6][2]} | {board[6][3]} | {board[6][4]} | {board[6][5]} | {board[6][6]} ")
    

# Inspired by https://www.youtube.com/watch?v=tF1WRCrd_HQ
def generate_ships(board):
    """Create random ships for the game"""
    for ship in range(6):
        ship_row, ship_column = randint(1, 6), randint(1,6)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(1, 6), randint(1,6)
        board[ship_row][ship_column] = "X"
    return board


# Inspired by https://www.youtube.com/watch?v=tF1WRCrd_HQ
def run_game():
    """Player guess for their move"""
    row = input("Make a guess for the row (a-f): ").lower()
    while row not in "abcdef":
        print("Invalid input. Please redo.")
        row = input("Make a guess for the row (a-f): ").lower()
    column = input("Make a guess for the column (1-6): ")
    while column not in "123456":
        print("Invalid input. Please redo.")
        column = input("Make a guess for the column (1-6): ")
    return convert_guess_to_numbers[row], int(column)


convert_guess_to_numbers = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}


# Inspired by https://www.youtube.com/watch?v=tF1WRCrd_HQ
def move_validation():
    moves = []
    turns = 15
    sunken1 = 0
    while turns > 0:
        style_board(board1)
        row, column = user_guess()
        guess = str(row) + str(column)
        if board1[row][column] == "X":
            print(f"You hit one battleship and it sunk. Congratulations!")
            board1[row][column] = "*"
            moves.append(guess)
            sunken1 += 1
            turns -= 1
        elif guess not in moves:
            print(f"There is no battleship!")
            board1[row][column] = "O"
            moves.append(guess)
            turns -= 1
        else:
            print(f"You already tried this one. Please try again.")     
        if sunken1 == 6:
            print(f"Congratulations! You won.") 
            break    
        print("You can try " + str(turns) + " more times.")
        if turns == 0:
            print("Sorry! Game over! You lost.")
            break
    

def main():
    print(WELCOME)
    display_homepage()
    user = get_username()
    #global board1
    board1 = create_board()
    #global board2
    #board2 = board_creation()
    board1 = generate_ships(board1)
    print(f"{user}'s board")
    print_board(board1)
    #print(f"Guess board")
    #style_board(board2)
    run_game()
    
main()