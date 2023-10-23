# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pyfiglet
from random import randint

# Inspired by https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
WELCOME = pyfiglet.figlet_format("Welcome to Battleship!")

def starting_question():
    """Starting question asked"""
    start = input("Do you want to start the game (y/n)?")
    return start


def username():
    """Ask for the username"""
    username = input("What is your name?")
    return username


# Inspired by https://www.youtube.com/watch?v=RqCZBbfd9Fw
def board_creation():
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
def style_board(board):
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
def ship_generation(board):
    """Create random ships for the game"""
    for ship in range(6):
        ship_row, ship_column = randint(1, 6), randint(1,6)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(1, 6), randint(1,6)
        board[ship_row][ship_column] = "X"


# Inspired by https://www.youtube.com/watch?v=RqCZBbfd9Fw
def user_guess(board, player):
    """Player guess for their move"""
    guess = input("Make a guess(e.g. a1 or f3): ")
    if guess == "a1":
        board[1][1] = player
    elif guess == "a2":
        board[1][2] = player
    elif guess == "a3":
        board[1][3] = player
    elif guess == "a4":
        board[1][4] = player
    elif guess == "a5":
        board[1][5] = player
    elif guess == "a6":
        board[1][6] = player
    elif guess == "b1":
        board[2][1] = player
    elif guess == "b2":
        board[2][2] = player
    elif guess == "b3":
        board[2][3] = player
    elif guess == "b4":
        board[2][4] = player
    elif guess == "b5":
        board[2][5] = player
    elif guess == "b6":
        board[2][6] = player
    elif guess == "c1":
        board[3][1] = player
    elif guess == "c2":
        board[3][2] = player
    elif guess == "c3":
        board[3][3] = player
    elif guess == "c4":
        board[3][4] = player
    elif guess == "c5":
        board[3][5] = player
    elif guess == "c6":
        board[3][6] = player
    elif guess == "d1":
        board[4][1] = player
    elif guess == "d2":
        board[4][2] = player
    elif guess == "d3":
        board[4][3] = player
    elif guess == "d4":
        board[4][4] = player
    elif guess == "d5":
        board[4][5] = player
    elif guess == "d6":
        board[4][6] = player
    elif guess == "e1":
        board[5][1] = player
    elif guess == "e2":
        board[5][2] = player
    elif guess == "e3":
        board[5][3] = player
    elif guess == "e4":
        board[5][4] = player
    elif guess == "e5":
        board[5][5] = player
    elif guess == "e6":
        board[5][6] = player
    elif guess == "f1":
        board[6][1] = player
    elif guess == "f2":
        board[6][2] = player
    elif guess == "f3":
        board[6][3] = player
    elif guess == "f4":
        board[6][4] = player
    elif guess == "f5":
        board[6][5] = player
    elif guess == "f6":
        board[6][6] = player
    else:
        print(f"Invalid guess: '{guess}'. Please try again.")
    return guess


# Inspired by https://www.youtube.com/watch?v=tF1WRCrd_HQ
def move_validation(guess, board):
    moves = []
    turns = 15
    while turns > 0:
        print(board)
        row, column = user_guess(board, player)
        if board[row][column] == "X":
            print(f"You hit one battleship and it sunk. Congratulations!")
            board[row][column] = "*"
            moves.append(guess)
            turns -= 1
        elif guess not in moves:
            print(f"There is no battleship!")
            board[row][column] = "O"
            moves.append(guess)
            turns -= 1
        else:
            print(f"You already tried this one. Please try again.")     
        if ship_sunk_count(board) == 6:
            print(f"Congratulations! You won.") 
            break    
        print("You can try " + str(turns) + " more times.")
        if turns == 0:
            print("Sorry! Game over! You lost.")
            break
    

# Inspired by https://www.youtube.com/watch?v=tF1WRCrd_HQ
def ship_sunk_count(board):
    count = 0
    for row in board:
        for column in row: 
            if column =="X":
                count += 1
    return count


def main():
    print(WELCOME)
    starting_question()
    user = username()
    board1 = board_creation()
    board2 = board_creation()
    ship_generation(board1)
    ship_generation(board2)
    player = "x"
    print(f"{user}'s board")
    style_board(board1)
    print(f"Opponent's board")
    style_board(board2)
    guess = user_guess(board2, player)
    move_validation(guess, board2)
    move_validation(guess, board1)
    style_board(board2)
    #print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")


main()
