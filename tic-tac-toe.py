def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    y = 0
    idx = 0
    idx2 = 0
    while y < 13:
        i = 0
        while i < 25:
            if (i == 4 or i == 12 or i == 20) and\
            (y == 2 or y == 6 or y == 10):
                if idx < 3:
                    print(board[idx][idx2], end="")
                    idx2 += 1
                    if idx2 == 3:
                        idx += 1
                        idx2 = 0
                    i += 1
            elif (i == 0 or i == 8 or i == 16 or i == 24) and\
            (y == 0 or y == 4 or y == 8 or y == 12):
                print("+", end="")
                i += 1
            elif (y == 0 or y == 4 or y == 8 or y == 12):
                print("-",end="")
                i += 1
            elif (i == 0 or i == 8 or i == 16 or i == 24):
                print("|", end="")
                i += 1
            else:
                print(" ", end="")
                i += 1
        print("")
        y += 1

def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    moves = make_list_of_free_fields(board)
    flag = 0
    while True:
        i = input("Enter Your Move: ")
        if i.lstrip("-+").isdigit() == False:
            print("Please enter a number!")
            continue
        else:
            i = int(i)
        if i < 1 or i > 9:
            print("Please enter a valid number!")
            continue
        for a in moves:
            if i in a:
                j = 0
                for x in board:
                    k = 0
                    for y in x:
                        if y == i:
                            board[j][k] = "O"
                            display_board(board)
                            victory_for(board, "O")
                            flag = 1
                        k += 1
                    j += 1
        if flag == 1:
            break
        print("Please enter a valid square number!")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = ()
    for i in board:
        lst = []
        for y in i:
            if y != "X" and y != "O":
                lst.append(y)
        if len(lst)!= 0:
            free_fields += tuple(lst),
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    global victory
    victory = 0
    if sign == "O":
        if board[0][0] == board[0][1] == board[0][2] == "O":
            print("You Won!")
            victory = 1
        elif board[1][1] == board[0][1] == board[2][1] == "O":
            print("You Won!")
            victory = 1
        elif board[0][0] == board[1][0] == board[2][0] == "O":
            print("You Won!")
            victory = 1
        elif board[0][2] == board[1][2] == board[2][2] == "O":
            print("You Won!")
            victory = 1
        elif board[2][0] == board[2][1] == board[2][2] == "O":
            print("You Won!")
            victory = 1
        elif board[0][0] == board[1][1] == board[2][2] == "O":
            print("You Win!")
            victory = 1
        elif board[0][2] == board[1][1] == board[2][0] == "O":
            print("You Win!")
            victory = 1
        elif board[1][0] == board[1][1] == board[1][2] == "O":
            print("You Win!")
            victory = 1
        elif not make_list_of_free_fields(board):
            print("Draw!")
            victory = 1
    elif sign == "X":
        if board[0][0] == board[0][1] == board[0][2] == "X":
            print("You Lost!")
            victory = 1
        elif board[1][0] == board[1][1] == board[1][2] == "X":
            print("You Lost!")
            victory = 1
        elif board[2][0] == board[2][1] == board[2][2] == "X":
            print("You Lost!")
            victory = 1
        elif board[0][0] == board[1][0] == board[2][0] == "X":
            print("You Lost!")
            victory = 1
        elif board[1][1] == board[0][1] == board[2][1] == "X":
            print("You Lost!")
            victory = 1
        elif board[0][2] == board[1][2] == board[2][2] == "X":
            print("You Lost!")
            victory = 1
        elif board[0][0] == board[1][1] == board[2][2] == "X":
            print("You Lost!")
            victory = 1
        elif board[0][2] == board[1][1] == board[2][0] == "X":
            print("You Lost!")
            victory = 1
        elif not make_list_of_free_fields(board):
            print("Draw!")
            victory = 1


def draw_move(board):
    # The function draws the computer's move and updates the board.
    moves = make_list_of_free_fields(board)
    flag = 0
    while True:
        i = rnd.randint(1,9)
        for a in moves:
            if i in a:
                j = 0
                for x in board:
                    k = 0
                    for y in x:
                        if y == i:
                            board[j][k] = "X"
                            print("Computer makes move to:", i)
                            display_board(board)
                            victory_for(board, "X")
                            flag = 1
                        k += 1
                    j += 1
        if flag == 1:
            break

import random as rnd
import time
print("Welcome to Tic-Tac-Toe game.")
while True:
    board = [[1,2,3],[4,5,6],[7,8,9]]
    display_board(board)
    print("Flipping a coin!")
    time.sleep(2)
    x = rnd.randint(1,2)
    if x == 1:
        print("You First")
        enter_move(board)
        draw_move(board)
    else:
        print("Computer First")
        draw_move(board)
    while True:
        victory = 0
        enter_move(board)
        if victory == 1:
            i = input("Press Q/q for quit the game or to restart press any key.")
            if i == "Q" or i == "q":
                quit()
            else:
                break
        draw_move(board)
        if victory == 1:
            i = input("Press Q/q for quit the game or to restart press any key.")
            if i == "Q" or i == "q":
                quit()
            else:
                break
