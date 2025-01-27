class Player:
    def __init__(self, name):
        self.name = name


class Board:
    def __init__(self):
        self.board = [[" " for _ in range(4)] for _ in range(4)]

    def display(self):
        for row in self.board:
            print("| " + " | ".join(row) + " |")
        print("-" * 30)
        print("| " + ' | '.join(chr(i) for i in range(ord('A'), ord('H'))) + " |")
        print()

    def drop(self, col, player):
        for row in range(len(self.board)-1, -1, -1):
            if self.board[row][col] == " ":
                self.board[row][col] = player.name
                return row, col
        return None, None

    """
    
    R R [R] R 
    
    """
    def check_won(self, row, col, player):
        return (
            self._check_direction(row, col, player.name, 1, 0) >= 3 or
            self._check_direction(row, col, player.name, 0, 1) + self._check_direction(row, col, player.name, 0, -1) >= 3 or
            self._check_direction(row, col, player.name, 1, -1) + self._check_direction(row, col, player.name, -1, 1) >= 3 or
            self._check_direction(row, col, player.name, 1, 1) + self._check_direction(row, col, player.name, -1, -1) >= 3
        )

    def _check_direction(self, row, col, color, d_row, d_col):
        count = 0
        r, c = row + d_row, col + d_col
        while 0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and self.board[r][c] == color:
            count += 1
            r += d_row
            c += d_col
        return count


class ConnectFourGame:
    def __init__(self):
        self.board = Board()
        self.players = [Player('R'), Player('Y')]
        self.cur_player = self.players[0]

    def switch_player(self):
        if self.cur_player.name == self.players[0].name:
            self.cur_player = self.players[1]
        else:
            self.cur_player = self.players[0]

    def get_column(self, input_col):
        return ord(input_col) - ord('A')

    def validate(self, input_col):
        if len(input_col) != 1:
            return False

        if 0 <= ord(input_col) - ord('A') < len(self.board.board[0]):
            return True

        return False

    def play(self):
        print("Welcome to connect 4")

        while True:
            self.board.display()
            input_col = input(f"Player ({self.cur_player.name}), enter the column to drop the ball (E.g. A): ")
            if not self.validate(input_col):
                print("Invalid input, please try again!")
                continue

            row, col = self.board.drop(self.get_column(input_col), self.cur_player)

            if row is None and col is None:
                break

            if self.board.check_won(row, col, self.cur_player):
                self.board.display()
                print(f"\n\nYay!! Player {self.cur_player.name} - you are the winner!!")
                break

            self.switch_player()


game = ConnectFourGame()
game.play()

