import random

class Cell:
    def __init__(self):
        self.is_revealed = False
        self.is_mine = False
        self.neighbor_mines = 0

    def reveal(self):
        self.is_revealed = True

    def __repr__(self):
        if self.is_revealed:
            return "M " if self.is_mine else (str(self.neighbor_mines) + " " if self.neighbor_mines > 0 else "  ")
        return ". "

class Board:
    def __init__(self, num_rows, num_cols, num_mines):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_mines = num_mines

        self.board = [[Cell() for _ in range(num_cols)] for _ in range(num_rows)]
        self.initialize_board()

    def initialize_board(self):
        available = [(r, c) for r in range(self.num_rows) for c in range(self.num_cols)]
        mines = random.sample(available, self.num_mines)

        for r, c in mines:
            self.board[r][c].is_mine = True

        self.initialize_mine_counts()

    def get_neighbor_cells(self):
        return [
            (1, -1), (1, 0), (1, 1),
            (0, -1), (0, 1),
            (-1, -1), (-1, 0), (-1, 1),
        ]

    def count_neighboring_mines(self, row, col):
        count = 0

        for row_offset, col_offset in self.get_neighbor_cells():
            r = row + row_offset
            c = col + col_offset

            if (0 <= r < self.num_rows) and (0 <= c < self.num_cols):
                if self.board[r][c].is_mine:
                    count += 1

        return count

    def initialize_mine_counts(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if not self.board[r][c].is_mine:
                    self.board[r][c].neighbor_mines = self.count_neighboring_mines(r, c)

    def display(self):
        for row in self.board:
            print(''.join(str(cell) for cell in row))
        print()

    def reveal(self, row, col, visited=None):
        if visited is None:
            visited = set()

        if (row, col) in visited:
            return

        visited.add((row, col))

        self.board[row][col].reveal()
        if self.board[row][col].is_mine:
            return

        if self.board[row][col].neighbor_mines > 0:
            return

        for row_offset, col_offset in self.get_neighbor_cells():
            r = row + row_offset
            c = col + col_offset

            if (0 <= r < self.num_rows) and (0 <= c < self.num_cols):
                if not self.board[r][c].is_mine:
                    self.reveal(r, c, visited)

class MineSweeperGame:
    def __init__(self, num_rows, num_cols, num_mines):
        self.board = Board(num_rows, num_cols, num_mines)

    def validate(self, row, col):
        _board = self.board
        if 0 <= int(row) < _board.num_rows and 0 <= int(col) < _board.num_cols:
            return True
        return False

    def is_game_won(self):
        _board = self.board
        for r in range(_board.num_rows):
            for c in range(_board.num_cols):
                if not _board.board[r][c].is_mine and not _board.board[r][c].is_revealed:
                    return False

        return True

    def play(self):
        print("Welcome to minesweeper")
        print("Instructions: Enter (row, col) like the example 2 2")
        self.board.display()

        while True:
            _input = input("Please enter the row, col: ").split()

            row, col = int(_input[0].strip()), int(_input[1].strip())

            if len(_input) != 2 and not self.validate(row, col):
                print("Invalid input! please try again")
                continue

            row, col = int(row), int(col)

            self.board.reveal(row, col)
            self.board.display()

            if self.board.board[row][col].is_mine:
                print("BOOM! you hit a mine!!")
                break

            if self.is_game_won():
                print("Congratulations!! You have won!")
                break


game = MineSweeperGame(10, 10, 10)
game.play()
