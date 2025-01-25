### **Initial class structure**:
```python
class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize()    
    
    def initialize(self):
        pass

    def display(self):
        pass

class Piece(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def is_valid_move(self, start, end, board):
        """
        Determine if the move from 'start' to 'end' is valid for this piece.
        This method must be implemented by all subclasses.
        """
        pass


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        pass
        

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        pass

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        pass

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        pass

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        pass

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        pass

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class ChessGame:
    def __init__(self):
        pass

    def play(self):
        pass

    def switch_turn(self):
        pass

    def is_input_valid(self):
        pass
    
    def parse_input(self):
        pass
```

### 