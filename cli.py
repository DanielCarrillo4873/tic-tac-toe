"""
    Cli
    - Creates cli interface
"""
import re

import Tic_tac_toe


def init():
    finished = False
    while not finished:
        print("Select a option")
        print("1) Start game")
        print("0) Quit")

        try:
            option = int(input())
        except ValueError:
            print("Enter an integer")
            continue

        if option == 1:
            again = "y"
            while again == "y":
                start_game()
                again = input("Play again? (y|n): ")
        elif option == 0:
            print("Bye!!!")
            finished = True
        else:
            print("Enter a valid option")


def start_game():
    game = Tic_tac_toe.TicTacToe()

    # Game main loop
    while not game.finished:
        print(game)

        # Enter, validate coordinates and make move
        while True:
            coordinates = input("Enter coordinates (X Y): ")
            if re.search(r"[1-3] [1-3]", coordinates):
                # Convert coordinates to int
                coordinates = coordinates.split(" ")
                coordinates = [int(i) - 1 for i in coordinates]
                try:
                    # Make move
                    game.next_move(coordinates[0], coordinates[1])
                    break
                except Tic_tac_toe.SquareOccupied:
                    print("Square occupied")
            else:
                print("Enter validate coordinates")

    print(game)
    if game.status() == game.EMPTY:
        print("Even, nobody wins")
    elif game.status() == game.X:
        print(f"{game.X_symbol} wins!!!")
    else:
        print(f"{game.O_symbol } Wins!!!")
    print("Game finished")
