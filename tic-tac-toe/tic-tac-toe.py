import re
import random
import time

class TicTacToeBoard:
    def __init__(self):
        self.board = [[" "] * 3 for _ in range(3)]

    def display(self):
        print("    1   2   3 ")
        print('-' * 15)

        for i, row in enumerate(self.board):
            print(f"{i+1} | {' | '.join(row)} |")
            print('-' * 15)


class TicTacToeGame:
    def __init__(self):
        self.tic_tac_toe_board = TicTacToeBoard()
        self.cur_player = 'X'

    def switch_player(self):
        self.cur_player = 'O' if self.cur_player == 'X' else 'X'

    def is_valid_move(self, move):
        if len(move) != 2:
            return False
        move = [int(x) for x in move]
        if not (1 <= move[0] <= 3 and 1 <= move[1] <= 3):
            return False
        return True

    def parse_move(self, move):
        return [int(x) for x in move]

    def is_game_won(self):
        board = self.tic_tac_toe_board.board
        required = self.cur_player * 3

        # Rows contain cur_player symbol
        if ((''.join(board[0]) == required) or
            (''.join(board[1]) == required) or
            (''.join(board[2]) == required)):
            return True

        # Cols contain cur_player symbol
        if ((''.join([board[0][0], board[1][0], board[2][0]]) == required) or
            (''.join([board[0][1], board[1][1], board[2][1]]) == required) or
            (''.join([board[0][2], board[1][2], board[2][2]]) == required)):
            return True

        # Fwd/Rev diagonal contain cur_player symbol
        if ((''.join([board[0][0], board[1][1], board[2][2]]) == required) or
            (''.join([board[2][0], board[1][1], board[0][2]]) == required)):
            return True

        return False

    def is_game_over(self):
        # if all cells are occupied
        board = self.tic_tac_toe_board.board

        re.sub('\s', '', ''.join(board[2]))

        return (len(re.sub('\s', '', ''.join(board[0]))) == 3 and
                len(re.sub('\s', '', ''.join(board[1]))) == 3 and
                len(re.sub('\s', '', ''.join(board[2]))) == 3)


    def play(self):
        print("Welcome to Tic Tac Toe")
        self.tic_tac_toe_board.display()
        while True:
            if self.cur_player == 'O':
                row, col = random.randint(0,2), random.randint(0,2)
                while self.tic_tac_toe_board.board[row][col] != " ":
                    row, col = random.randint(0,2), random.randint(0,2)
                move = str(row+1) + str(col+1)
                time.sleep(1)
                print("Computer chose: "+ move)
            else:
                move = input(f"\nPlayer {self.cur_player} Enter the (row, column) to place your move (E.g. 22): ")
            if not self.is_valid_move(move):
                print("Not a valid selection! Please select again!")
                continue
            row, col = self.parse_move(move)
            if self.tic_tac_toe_board.board[row-1][col-1] != " ":
                print("The cell is already occupied! Please select again!")
                continue

            self.tic_tac_toe_board.board[row - 1][col - 1] = self.cur_player

            self.tic_tac_toe_board.display()
            if self.is_game_won():
                print(f"\nYayy! Player {self.cur_player} is the winner!!!")
                break

            if self.is_game_over():
                print(f"\nThe game resulted in a tie! ")
                break

            self.switch_player()


game = TicTacToeGame()
game.play()



