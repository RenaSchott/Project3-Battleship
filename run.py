# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pyfiglet

WELCOME = pyfiglet.figlet_format("Welcome to Battleship!")
#RULES = You can find the rules for Battleship 

#START = input("Do you want to start the game (y/n)?")
 

def board_creation():
    """Create a board for the game battleship"""
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

board1 = board_creation()


board2 = board_creation()


#def start_game():
    #try:
        #if input == y:

       # else:
    #except:
        

def main():
    print(WELCOME)
    #print(START)
    #print(RULES)
    print(board1)
    print(board2)
    #print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")


main()
