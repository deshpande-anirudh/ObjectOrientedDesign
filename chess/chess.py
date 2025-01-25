from enum import Enum, auto
from abc import ABC, abstractmethod

class Color(Enum):
    BLACK = auto()
    WHITE = auto()

class Piece(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def is_valid_move(self, start, end, board):
        pass

# PAWN, ROOK, KNIGHT, BISHOP, QUEEN, KING
class Pawn(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self.has_moved = False
        self.name = 'P'

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        direction = -1 if self.color == Color.WHITE else 1

        # Move forward by 1
        if start_col == end_col and start_row + direction == end_row:
            if board[end_row][end_col] is None:
                return True

        # Move forward by 2, only at the beginning
        if start_col == end_col and start_row + 2 * direction == end_row:
            mid_row = start_row + direction
            starting_row = 6 if self.color == Color.WHITE else 1
            if start_row == starting_row and board[mid_row][end_col] is None and board[end_row][end_col] is None:
                return True

        # Move diagonally by 1,if piece of similar color exists at the diagonal
        if abs(start_col - end_col) == 1 and start_row + direction == end_row:
            if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
                return True

        return False


class Rook(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self.name = 'R'

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        if start_row != end_row and start_col != end_col:
            return False

        row_step = 0 if start_row == end_row else(1 if end_row > start_row else -1)
        col_step = 0 if start_col == end_col else (1 if end_col > start_col else -1)

        start_r, start_c = start_row + row_step, start_col + col_step
        while start_r != end_row and start_c != end_col:
            if board[start_r][start_c] is not None:
                return False # Path is blocked
            start_r += row_step
            start_c += col_step

        if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
            return True

        return False


class Knight(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self.name = 'N'

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        if ((abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or
                (abs(start_col - end_col) == 2 and abs(start_row - end_row) == 1)):
            if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
                return True

        return False



class Bishop(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self.name = 'B'

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        if abs(end_row - start_row) != abs(end_col - start_col):
            return False

        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1

        cur_row, cur_col = start_row + row_step, start_col + col_step

        while cur_row != end_row and cur_col != end_col:
            if board[cur_row][cur_col] is not None:
                return False
            cur_row += row_step
            cur_col += col_step

        if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
            return True

        return False


class Queen(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self.name = 'Q'

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        is_diagonal = abs(start_row - end_row) == abs(start_col - end_col)
        is_straight = start_row == end_row or start_col == end_col

        if not is_diagonal and not is_straight:
            return False

        if is_diagonal:
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
        else:
            row_step = 0 if end_row == start_row else (1 if end_row > start_row else -1)
            col_step = 0 if end_col == start_col else (1 if end_col > start_col else -1)

        cur_row, cur_col = start_row + row_step, start_col + col_step

        while cur_row != end_row and cur_col != end_col:
            if board[cur_row][cur_col] is not None:
                return False

            cur_row += row_step
            cur_col += col_step

        if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
            return True
        return False

class King(Piece):
    def __init__(self, color: Color):
        super().__init__(color)
        self.name = 'K'

    def is_valid_move(self, start, end, board):
        start_row, start_col = start
        end_row, end_col = end

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        if row_diff <= 1 and col_diff <= 1:
            if board[end_row][end_col] is None or board[end_row][end_col].color != self.color:
                return True

        return False


class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_pieces()

    def initialize_pieces(self):
        # Place Pawns
        for col in range(len(self.board[0])):
            self.board[1][col] = Pawn(Color.BLACK)
            self.board[6][col] = Pawn(Color.WHITE)

        # Place Rooks
        self.board[0][0] = Rook(Color.BLACK)
        self.board[0][7] = Rook(Color.BLACK)
        self.board[7][0] = Rook(Color.WHITE)
        self.board[7][7] = Rook(Color.WHITE)

        # Place Knights
        self.board[0][1] = Knight(Color.BLACK)
        self.board[0][6] = Knight(Color.BLACK)
        self.board[7][1] = Knight(Color.WHITE)
        self.board[7][6] = Knight(Color.WHITE)

        # Place Bishops
        self.board[0][2] = Bishop(Color.BLACK)
        self.board[0][5] = Bishop(Color.BLACK)
        self.board[7][2] = Bishop(Color.WHITE)
        self.board[7][5] = Bishop(Color.WHITE)

        # Place King
        self.board[0][3] = Queen(Color.BLACK)
        self.board[7][3] = Queen(Color.WHITE)

        # Place Queen
        self.board[0][4] = King(Color.BLACK)
        self.board[7][4] = King(Color.WHITE)

    def display(self):
        print("     a  b  c  d  e  f  g  h")
        print("---------------------------")
        for i in range(len(self.board)):
            cur_row = []
            for j in range(len(self.board[0])):
                if self.board[i][j] is None:
                    cur_row.append(f' . ')
                else:
                    cur_row.append(f' {self.board[i][j].name} ')
            print(f"{i} | {''.join(cur_row)}")


class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.cur_turn = Color.WHITE

    def switch_turn(self):
        self.cur_turn = Color.WHITE if self.cur_turn == Color.BLACK else Color.BLACK

    def is_valid_input(self, move):
        parts = move.split()
        if len(parts) != 2:
            return False
        for part in parts:
            if len(part) != 2 or part[0] not in "abcdefgh" or not part[1].isdigit():
                return False
        return True

    def parse_input(self, move):
        # Convert chess notation (e.g., "e2 e4") to board indices
        start, end = move.split()
        start_col = ord(start[0]) - ord("a")
        start_row = int(start[1])
        end_col = ord(end[0]) - ord("a")
        end_row = int(end[1])
        return (start_row, start_col), (end_row, end_col)

    def play(self):
        print("Welcome to Chess!")
        self.board.display()
        while True:
            print(f"\n{self.cur_turn}'s turn. Enter your move (E.g. e2 e4): ")
            move = input().strip()

            if not self.is_valid_input(move):
                print("Invalid input! Please use the format 'e2 e4'.")
                continue

            start, end = self.parse_input(move)
            piece = self.board.board[start[0]][start[1]]

            # Validate that the piece belongs to the current player
            # print(piece.name, piece.color)
            if piece is None or piece.color != self.cur_turn:
                print("Invalid move! You must move your own piece.")
                continue

            # Validate the piece's move
            if not piece.is_valid_move(start, end, self.board.board):
                print("Invalid move for this piece. Try again.")
                continue

            # Execute the move
            self.board.board[end[0]][end[1]] = piece
            self.board.board[start[0]][start[1]] = None

            # Display the updated board
            self.board.display()

            # Check for endgame (simplified: not checking checkmate here)
            if self.is_game_over():
                print(f"Game over! {self.current_turn.name} wins!")
                break

            self.switch_turn()

    def is_game_over(self):
        white_king = False
        black_king = False

        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]
                if isinstance(piece, King):
                    if piece.color == Color.WHITE:
                        white_king = True
                    elif piece.color == Color.BLACK:
                        black_king = True

        if not white_king:
            print("Game over! Black wins!")
            return True
        if not black_king:
            print("Game over! White wins!")
            return True

        return False


game = ChessGame()
game.play()






