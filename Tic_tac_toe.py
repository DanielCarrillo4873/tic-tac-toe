import copy


class TicTacToe:
    __X = 1
    __O = 2
    __EMPTY = 0

    __X_symbol = "X"
    __O_symbol = "O"
    __EMPTY_SYMBOL = "_"

    def __init__(self):
        self.__board = self.__create_board()
        self.__turn = self.__X
        self.__moves = 0
        self.__game_finished = False

    def __str__(self):
        board = "-------\n"

        for row in self.__board:
            board += "| "
            for i in range(3):
                if row[i] == self.__X:
                    board += self.__X_symbol
                elif row[i] == self.__O:
                    board += self.__O_symbol
                else:
                    board += self.__EMPTY_SYMBOL
            board += " |"
            board += '\n'

        board += "-------\n"
        return board

    @property
    def board(self):
        return copy.deepcopy(self.__board)

    @property
    def turn(self):
        return self.__turn

    @property
    def moves(self):
        return self.__moves

    @property
    def game_finished(self):
        return self.__game_finished

    def next_move(self, x, y):
        if 0 > x or x > 2 or 0 > y or x > 2:
            raise CoordinateOutOfRange(x, y)
        elif self.__game_finished:
            raise GameAlreadyFinished()
        elif self.__board[x][y] != self.__EMPTY:
            raise SquareOccupied(x, y)
        else:
            self.__board[x][y] = self.__turn
            self.__turn = self.__next_turn()
            self.__moves += 1
            if self.__moves == 9 or self.game_status() != 0:
                self.__game_finished = True

    def __next_turn(self):
        if self.__turn == self.__X:
            return self.__O
        else:
            return self.__X

    def __create_board(self):
        return [[self.__EMPTY for _ in range(3)] for _ in range(3)]

    def game_status(self):
        if self.__moves > 4:
            # Checking rows
            for row in self.__board:
                if row[0] == row[1] == row[2]:
                    return row[0]

            # Checking columns
            for i in range(3):
                if self.__board[0][i] == self.__board[1][i] == self.__board[2][i]:
                    return self.__board[0][i]

            # Checking first diagonal
            if self.__board[0][0] == self.__board[1][1] == self.__board[2][2]:
                return self.__board[0][0]

            # Checking second diagonal
            if self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
                return self.__board[0][2]

        return self.__EMPTY


# Exception classes
class CoordinateOutOfRange(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.message = f"Coordinates: ({x}, {y}) are out range"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class GameAlreadyFinished(Exception):
    def __init__(self):
        self.message = "Game already finished"

    def __str__(self):
        return self.message


class SquareOccupied(Exception):
    def __init__(self, x, y):
        self.message = f"Square ({x}, {y}) is already occupied"

    def __str__(self):
        return self.message
