import random

class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.adjacent_mines = 0

    def reveal(self):
        self.is_revealed = True

    def __repr__(self):
        if self.is_revealed:
            return "M" if self.is_mine else str(self.adjacent_mines) if self.adjacent_mines > 0 else " "
        return "."

class Board:
    def __init__(self, rows, cols, num_mines):
        self.rows, self.cols, self.num_mines = rows, cols, num_mines
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.place_mines()  # Place mines at initialization
        self._calculate_adjacent_mines()

    def place_mines(self):
        cells = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        for r, c in random.sample(cells, self.num_mines):
            self.grid[r][c].is_mine = True

    def _calculate_adjacent_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.grid[r][c].is_mine:
                    self.grid[r][c].adjacent_mines = sum(
                        self.grid[nr][nc].is_mine
                        for nr, nc in self._get_neighbors(r, c)
                    )

    def _get_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return [(row + dr, col + dc) for dr, dc in directions if 0 <= row + dr < self.rows and 0 <= col + dc < self.cols]

    def reveal_cell(self, row, col):
        cell = self.grid[row][col]
        if cell.is_revealed:
            return False
        if cell.is_mine:
            cell.reveal()  # Reveal the mine cell
            return True
        if cell.adjacent_mines == 0:
            for nr, nc in self._get_neighbors(row, col):
                self.reveal_cell(nr, nc)
        else:
            cell.reveal()  # Reveal non-mine cells
        return False

    def is_game_won(self):
        return all(cell.is_revealed or cell.is_mine for row in self.grid for cell in row)

    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print()


class Game:
    def __init__(self, rows=9, cols=9, num_mines=10):
        self.board = Board(rows, cols, num_mines)
        self.game_over = False

    def play(self):
        print("Welcome to Minesweeper!")
        print("Commands: 'reveal row col' (e.g., reveal 0 1).")

        while not self.game_over:
            self.board.display()
            action = input("Your move: ").strip().split()

            if len(action) != 3:
                print("Invalid input. Use format: reveal row col")
                continue

            action_type, row, col = action[0].lower(), int(action[1]), int(action[2])

            if action_type == "reveal":
                if self.board.reveal_cell(row, col):  # Hit a mine
                    print("BOOM! You hit a mine. Game Over.")
                    self.game_over = True
                elif self.board.is_game_won():  # All safe cells revealed
                    print("Congratulations! You've cleared the board. You win!")
                    self.game_over = True
            else:
                print("Invalid command. Use 'reveal'.")

        self.board.display()  # Show final board


if __name__ == "__main__":
    game = Game(rows=9, cols=9, num_mines=10)
    game.play()
