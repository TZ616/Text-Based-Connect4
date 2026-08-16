import random
import sys
from file_in import file_in
from file_out import file_out

ROWS = 6
COLS = 7
TOTAL = ROWS*COLS
EMPTY = "."
PIECES = ["R", "Y"]

def initialize():
    lis = []
    for i in range(ROWS):
        lis.append([])
        for j in range(COLS):
            lis[i].append(EMPTY)
    return lis

def print_board(lis):
    print("\nCurrent Board:")
    for i in range(ROWS):
        for j in range(COLS):
            print(lis[i][j], end="")
        print()
    print()

def player_action():
    while 1:
        try:
            choice = int(input("Enter 0 if you want to continue playing, 1 if you want to export the current game, and 2 if you want to quit: "))
        except ValueError:
            print("Please enter 0, 1, or 2!\n")
        else:
            if (choice == 2):
                print("\nAre you sure? The current state of the game will be lost!")
                s = input("Enter y if you wish to continue this action: ")
                if (s == "y"):
                    sys.exit("Quit Successfully!")
            elif (not (0 <= choice <= 2)):
                print("Please enter 0, 1, or 2!\n")
            else:
                break
    return choice

def check_coords(x, y):
    if (0 <= x < ROWS and 0 <= y < COLS):
        return 1
    return 0

def check_vert(x, y, lis):
    if (ROWS-x < 4):
        return 0
    for i in range(x+1, x+4):
        if (lis[i][y] != lis[x][y]):
            return 0
    return 1

def check_hori(x, y, lis):
    counter = 0
    for i in range(max(y-3, 0), min(y+4, COLS)):
        if (lis[x][i] != lis[x][y]):
            counter = 0
        else:
            counter+=1
            if (counter >= 4):
                return 1
    return 0

def check_diag(x, y, lis):
    counter = 0
    for i in range(max(x-3, 0), min(x+4, ROWS)):
        if (check_coords(i, i+(y-x)) and lis[i][i+(y-x)] == lis[x][y]):
            counter+=1
        else:
            counter = 0
        if (counter >= 4):
            return 1
    counter = 0
    for i in range(max(x-3, 0), min(x+4, ROWS)):
        if (check_coords(i, (x+y)-i) and lis[i][(x+y)-i] == lis[x][y]):
            counter+=1
        else:
            counter = 0
        if (counter >= 4):
            return 1
    return 0

def computer_choice(lis):
    cols = []
    for i in range(COLS):
        cols.append(i)
    while 1:
        temp = random.choice(cols)
        match (move(1, temp, lis)):
            case 0:
                cols.remove(temp)
            case 1:
                print(f"\nComputer has placed a piece in column {temp}")
                break
            case 2:
                print(f"\nComputer has placed a piece in column {temp}")
                print_board(lis)
                sys.exit("Computer has won the game!")

def player_choice(player, lis):
    while 1:
        try:
            col = int(input("Enter the column you want to place your piece: "))
            match (move(player, col, lis)):
                case 0:
                    print("Please enter the number of a column that is not full!\n")
                case 1:
                    print(f"\nPlayer {player+1} has placed a piece in column {col}")
                    break
                case 2:
                    print(f"\nPlayer {player+1} has placed a piece in column {col}")
                    print_board(lis)
                    sys.exit(f"Player {player+1} has won the game!")
        except ValueError:
            print("Please enter the number of a column that is not full!")

def move(player, col, lis):
    if (not check_coords(0, col)):
        return 0
    for i in range(ROWS-1, -1, -1):
        if (lis[i][col] == EMPTY):
            lis[i][col] = PIECES[player]
            if (check_vert(i, col, lis) or check_hori(i, col, lis) or check_diag(i, col, lis)):
                return 2
            return 1
    return 0

def main():
    print("Welcome to Text-based Connect 4!\n")
    while (1):
        try:
            choice1 = int(input("Enter 0 to play against the computer (you will go first), or 1 to play against a friend: "))
        except ValueError:
            print("Please enter either 0 or 1!\n")
        else:
            if (choice1 != 0 and choice1 != 1):
                print("Please enter either 0 or 1!\n")
            else:
                break
    while (1):
        try:
            choice2 = int(input("Enter 0 to start a new game, or 1 to load an existing game: "))
        except ValueError:
            print("Please enter either 0 or 1!\n")
        else:
            if (choice2 != 0 and choice2 != 1):
                print("Please enter either 0 or 1!\n")
            else:
                break
    if (choice2):
        moves, lis = file_in()
    else:
        lis = initialize()
        moves = 0
    if (not choice1):
        if (moves%2):
            print_board(lis)
            computer_choice(lis)
            moves+=1
        while (moves <= TOTAL):
            print_board(lis)
            if (player_action()):
                file_out(moves, lis)
                sys.exit("Exported Successfully!")
            player_choice(0, lis)
            moves+=1
            print_board(lis)
            if (player_action()):
                file_out(moves, lis)
                sys.exit("Exported Successfully!")
            computer_choice(lis)
            moves+=1
    else:
        if (moves%2):
            print_board(lis)
            player_choice(1, lis)
            moves+=1
        while (moves <= TOTAL):
            print_board(lis)
            if (player_action()):
                file_out(moves, lis)
                sys.exit("Exported Successfully!")
            player_choice(0, lis)
            moves+=1
            print_board(lis)
            if (player_action()):
                file_out(moves, lis)
                sys.exit("Exported Successfully!")
            player_choice(1, lis)
            moves+=1
    print_board(lis)
    sys.exit("Game Drawn!")

if __name__ == "__main__":
    main()
