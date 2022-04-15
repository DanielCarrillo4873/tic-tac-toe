#
#   Main file, application entry point
#

import Tic_tac_toe as toe

if __name__ == "__main__":
    game = toe.TicTacToe()

    print("Game initiated!!!")
    while not game.game_finished:
        print(game)

