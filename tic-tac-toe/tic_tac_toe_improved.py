import random
import time


class TicTacToeBoard:
    def __init__(self):
        self.board = [[" "] * 3 for _ in range(3)]

    def display(self):
        print("    1   2   3 ")
        print("  " + "-" * 13)
        for i, row in enumerate(self.board):
            print(f"{i + 1} | {' | '.join(row)} |")
            print("  " + "-" * 13)

    def is_full(self):
        # Check if all cells are occupied
        return all(cell != " " for row in self.board for cell in row)


class TicTacToeGame:
    def __init__(self):
        self.board = TicTacToeBoard()
        self.cur_player = "X"

    def switch_player(self):
        self.cur_player = "O" if self.cur_player == "X" else "X"

    def is_valid_move(self, move):
        if len(move) != 2 or not move.isdigit():
            return False
        row, col = map(int, move)
        return 1 <= row <= 3 and 1 <= col <= 3 and self.board.board[row - 1][col - 1] == " "

    def is_game_won(self):
        b = self.board.board
        player = self.cur_player

        # Check rows, columns, and diagonals for a win
        return any(
            all(b[r][c] == player for c in range(3)) for r in range(3)  # Rows
        ) or any(
            all(b[r][c] == player for r in range(3)) for c in range(3)  # Columns
        ) or all(
            b[i][i] == player for i in range(3)  # Main diagonal
        ) or all(
            b[i][2 - i] == player for i in range(3)  # Anti-diagonal
        )

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.board.display()

        while True:
            if self.cur_player == "O":
                print("\nComputer is making its move...")
                time.sleep(1)
                row, col = random.randint(0, 2), random.randint(0, 2)
                while self.board.board[row][col] != " ":
                    row, col = random.randint(0, 2), random.randint(0, 2)
                print(f"Computer chose: {row + 1}{col + 1}")
            else:
                move = input(f"\nPlayer {self.cur_player}, enter your move (row and column, e.g., 22): ")
                if not self.is_valid_move(move):
                    print("Invalid move! Please try again.")
                    continue
                row, col = map(int, move)
                row, col = row - 1, col - 1

            # Place the move and update the board
            self.board.board[row][col] = self.cur_player
            self.board.display()

            if self.is_game_won():
                print(f"\nYay! Player {self.cur_player} wins!")
                break

            if self.board.is_full():
                print("\nIt's a tie!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()
