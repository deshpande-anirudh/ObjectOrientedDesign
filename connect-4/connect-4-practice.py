class ConnectFourBoard:
    def __init__(self, rows=6, cols=7):
        self.board = [[" " for _ in range(cols)] for _ in range(rows)]

    def display(self):
        for row in self.board:
            print("| " + ' | '.join(row) + " |")
        print("| " + ' | '.join([ str(i+1) for i in range(len(self.board[0]))]) + " |")
        print()

    def drop(self, col, symbol):
        for row in range(len(self.board) - 1, -1, -1):
            if self.board[row][col] == " ":
                self.board[row][col] = symbol
                return row, col
        return None, None

    def is_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != " ":
                    return False
        return True

    def _check_condition(self, row, col, d_row, d_col, symbol):
        count = 0
        cur_row = row + d_row
        cur_col = col + d_col

        while 0 <= cur_row < len(self.board) and 0 <= cur_col < len(self.board[0]):
            if self.board[cur_row][cur_col] != symbol:
                break
            count += 1
            cur_row += d_row
            cur_col += d_col
        return count

    def is_game_won(self, row, col, symbol):
        return (
            # Column condition
            self._check_condition(row, col, 1, 0, symbol) >= 3 or

            # Row condition
            (self._check_condition(row, col, 0, -1, symbol)
                + self._check_condition(row, col, 0, 1, symbol) >= 3) or

            # Forward diagonal condition
            (self._check_condition(row, col, 1, 1, symbol)
                + self._check_condition(row, col, -1, -1, symbol) >= 3) or

            # Reverse diagonal condition
            (self._check_condition(row, col, -1, 1, symbol)
             + self._check_condition(row, col, 1, -1, symbol) >= 3)
        )

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return f"({self.symbol})"

class ConnectFourGame:
    def __init__(self):
        self.connect_four_board = ConnectFourBoard()
        self.players = [Player('R'), Player('Y')]
        self.cur_player = self.players[0]

    def switch_player(self):
        if self.cur_player == self.players[0]:
            self.cur_player = self.players[1]
        else:
            self.cur_player = self.players[0]

    def validate(self, col):
        if len(col) != 1 or not col.isdigit():
            return False

        if 0 <= int(col) < len(self.connect_four_board.board):
            return True

        return False

    def sanitize(self, col):
        return int(col) - 1

    def play(self):
        print("Welcome to Connect 4")
        board = self.connect_four_board
        board.display()

        while True:
            column = input(f"Player {self.cur_player}, enter the column to drop the ball: ").strip()
            if not self.validate(column):
                print("Invalid input, please try again!")
                continue

            row, col = self.connect_four_board.drop(self.sanitize(column), self.cur_player.symbol)

            if row is None and col is None:
                print(f"The column {column} is full, please try a different column")
                continue

            board.display()

            if self.connect_four_board.is_game_won(row, col, self.cur_player.symbol):
                print(f"Yayy! player {self.cur_player} is the winner")
                break

            if self.connect_four_board.is_full():
                print(f"Oh! Its a draw!")
                break

            self.switch_player()


game = ConnectFourGame()
game.play()
