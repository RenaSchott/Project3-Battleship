import pyfiglet
import sys
from random import randint


# Inspired by:
# https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
WELCOME = pyfiglet.figlet_format("Welcome to Battleship!")


convert_guess_to_numbers = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}


# Inspired by:
# https://www.freecodecamp.org/news/
# python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/
def display_homepage():
    """
    Question asked whether the user want to play the game.

    Args:
        none

    Returns:
        start = Answer to the question
    """
    start = input(f"Do you want to start the game (y/n)?\n")
    if start == "y":
        print(f"Have fun!")
    elif start == "n":
        print(f"Sadly, you won't play the game")
        sys.exit(0)
    else:
        while start != "y" or start != "n":
            print("Invalid input. Please redo.")
            start = input(f"Do you want to start the game (y/n)?\n")
            if start == "y":
                print(f"Have fun!")
                break
            elif start == "n":
                print(f"Sadly, you won't play the game")
                sys.exit(0)
                break
    return start


def get_username():
    """
    User is asked for their name.

    Args:
        none

    Returns:
        username = Answer to the question
    """
    username = input("A name is needed for playing the game. "
                     "What is your name?\n")
    if username.isspace():
        print(f"The input contains only whitespace characters.\
              Please restart the game.")
        sys.exit(0)
    elif username == "":
        print(f"A username is needed for playing the game.\
              Please restart the game.")
        sys.exit(0)
    return username


# Inspired by https://www.freecodecamp.org/news/print-newline-in-python/
def explain_rules():
    """
    User is asked whether a rule explanation is needed,

    Args:
        none

    Returns:
        rules = Game rules
    """
    rules = input(f"Do you need the game rules (y/n)?\n")
    if rules == "y":
        text = "This is a simplified version of the normal battleship game.\
                Therefore 6 ships \n are randomly distributed on the game\
                board and your task is to find them by \n guessing a row\
                and a column. When you hit all 6 ships you win. But\
                therefore \n you only have 15 valid tries. Otherwise you\
                loose the game."
        lines = text.split('\n')
        print('\n'.join(lines))
    elif rules == "n":
        print(f"Have fun!")
    else:
        while rules != "y" or rules != "n":
            print("Invalid input. Please redo.")
            rules = input(f"Do you need the game rules (y/n)?\n")
            if rules == "y":
                text = "This is a simplified version of the normal battleship\
                        game. Therefore 6 ships \n are randomly distributed on\
                        the game board and your task is to find them by \n\
                        guessing a row and a column. When you hit all 6 ships\
                        you win. But therefore \n you only have 15 valid\
                        tries. Otherwise you loose the game."
                lines = text.split('\n')
                print('\n'.join(lines))
                break
            elif rules == "n":
                print(f"Have fun!")
                break
    return rules


# Inspired by https://www.youtube.com/watch?v=RqCZBbfd9Fw
def create_board():
    """
    Creates the board for the battleship game

    Args:
        none

    Returns:
        board = battleship game board
    """
    board = [
        [" ", 1, 2, 3, 4, 5, 6],
        ["a", " ", " ", " ", " ", " ", " ", ],
        ["b", " ", " ", " ", " ", " ", " ", ],
        ["c", " ", " ", " ", " ", " ", " ", ],
        ["d", " ", " ", " ", " ", " ", " ", ],
        ["e", " ", " ", " ", " ", " ", " ", ],
        ["f", " ", " ", " ", " ", " ", " ", ],
        ]
    return board


# Inspired by https://www.youtube.com/watch?v=RqCZBbfd9Fw
def print_board(board):
    """
    Printing the game board with the proper styling.

    Args:
        board = list from create_board()

    Returns:
        only print statements
    """
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} |\
          {board[0][4]} | {board[0][5]} | {board[0][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} |\
          {board[1][4]} | {board[1][5]} | {board[1][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} |\
          {board[2][4]} | {board[2][5]} | {board[2][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} |\
          {board[3][4]} | {board[3][5]} | {board[3][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} |\
          {board[4][4]} | {board[4][5]} | {board[4][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[5][0]} | {board[5][1]} | {board[5][2]} | {board[5][3]} |\
          {board[5][4]} | {board[5][5]} | {board[5][6]} ")
    print(f"---|---|---|---|---|---|---")
    print(f" {board[6][0]} | {board[6][1]} | {board[6][2]} | {board[6][3]} |\
          {board[6][4]} | {board[6][5]} | {board[6][6]} ")


# Inspired by https://www.youtube.com/watch?v=tF1WRCrd_HQ
def generate_ships(board):
    """
    Creating 6 ships and placing them randomly on the board

    Args:
        board = list from create_board()

    Returns:
        board = including ships
    """
    for ship in range(6):
        ship_row, ship_column = randint(1, 6), randint(1, 6)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(1, 6), randint(1, 6)
        board[ship_row][ship_column] = "X"
    return board


# Inspired by https://www.youtube.com/watch?v=tF1WRCrd_HQ
def guess_by_user():
    """
    Player input for their guesses for the battleship locations

    Args:
        none

    Returns:
        convert_guess_to_numbers[row], int(column) = integers for row and
        column
    """
    while True: 
        row = input("Make a guess for the row (a-f): \n").lower()
        if row not in "abcdef":
            print("Invalid input. Please redo.")
        elif row.isspace():
            print("Invalid input. Please redo.")
        elif row == "":
            print("Invalid input. Please redo.")
        else:
            break

    while True: 
        column = input("Make a guess for the column (1-6): \n").lower()
        if column not in "123456":
            print("Invalid input. Please redo.")
        elif column.isspace():
            print("Invalid input. Please redo.")
        elif column == "":
            print("Invalid input. Please redo.")
        else:
            break
    return convert_guess_to_numbers[row], int(column)


# Inspired by https://www.youtube.com/watch?v=tF1WRCrd_HQ
def run_game():
    """
    Main game engine including the evaluation of the user input

    Args:
        none

    Returns:
        Print statements on the user guess and turn count

    """
    moves = []
    turns = 15
    sunken1 = 0
    while turns > 0:
        print_board(board1)
        row, column = guess_by_user()
        guess = str(row) + str(column)
        if board2[row][column] == "X":
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
        print("You can try " + str(turns) + " more times.")
        if sunken1 == 6:
            print(f"Congratulations! You won.")
            sys.exit(0)
        if turns == 0:
            print("Sorry! Game over! You lost.")
            sys.exit(0)


def main():
    print(WELCOME)
    display_homepage()
    user = get_username()
    explain_rules()
    global board1
    board1 = create_board()
    global board2
    board2 = create_board()
    board2 = generate_ships(board2)
    print(f"{user}'s board")
    run_game()


main()
