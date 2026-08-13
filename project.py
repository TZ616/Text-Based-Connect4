import random
from file_in import file_in
from file_out import file_out

ROWS = 6
COLS = 7
EMPTY = "."
PIECES = ["R", "Y"]

def initialize():
    lis = []
    for i in range(ROWS):
        lis.append([])
        for j in range(COLS):
            lis[i].append(EMPTY)
    return lis

def computer_choice(lis):
    cols = [0, 1, 2, 3, 4, 5, 6]
    while 1:
        temp = random.choice(cols)
        if (move(1, temp, lis)):
            break
        else:
            cols.remove(temp)

def move(player, col, lis):
    for i in range(COLS-1, -1, -1):
        if (i[col] == EMPTY):
            lis[i][col] = PIECES[player]
            return 1
    return 0

def check_vert():
    temp = 1

def check_hori():
    temp = 1

def check_diag():
    temp = 1

def main():
    print("Welcome to Text-based Connect 4!\n")
    while (1):
        try:
            choice1 = int(input("Enter 0 to play against the computer, or 1 to play against a friend: "))
        except ValueError:
            print("Please enter either 0 or 1!")
        else:
            if (choice1 != 0 and choice1 != 1):
                print("Please enter either 0 or 1!")
            else:
                break
    while (1):
        try:
            choice2 = int(input("Enter 0 to start a new game, or 1 to load an existing game: "))
        except ValueError:
            print("Please enter either 0 or 1!")
        else:
            if (choice2 != 0 and choice2 != 1):
                print("Please enter either 0 or 1!")
            else:
                break
    if (choice2):
        moves, lis = file_in()
    else:
        lis = initialize()
        moves = 0
    file_out(moves, lis)
if __name__ == "__main__":
    main()
