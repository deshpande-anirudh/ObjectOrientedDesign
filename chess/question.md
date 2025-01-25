---

### **Chess Game Implementation**

#### **Objective**:  
Develop an object-oriented program for a simple chess game. The implementation should focus on the following key aspects: board setup, pieces, and rules for basic moves.

---

### **Requirements**:

1. **Classes and Objects**:
   - Create a `ChessBoard` class to represent the board.
   - Create a `Piece` base class with common attributes and methods for all chess pieces.
   - Create derived classes for each chess piece: `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, and `King`.
   - Create a `Player` class to manage player details and their pieces.

2. **Chess Board**:
   - Represent the board as an 8x8 grid.
   - Each square should either hold a chess piece or be empty.

3. **Game Rules**:
   - Implement the rules for basic movements of pieces:
     - **Pawn**: Moves forward one square (two squares on its first move), captures diagonally.
     - **Rook**: Moves horizontally or vertically.
     - **Knight**: Moves in an "L" shape (two squares in one direction, one square perpendicular).
     - **Bishop**: Moves diagonally.
     - **Queen**: Moves any number of squares horizontally, vertically, or diagonally.
     - **King**: Moves one square in any direction.
   - Handle board boundaries and invalid moves.

4. **Game Logic**:
   - Initialize the board with pieces in their standard starting positions.
   - Alternate turns between two players.
   - Allow a player to make a move by selecting a piece and its destination.
   - Validate each move based on the piece's movement rules and board state.
   - Detect basic check (King under attack) and checkmate conditions.

5. **Optional Features** (for extended practice):
   - Add functionality for castling, en passant, and pawn promotion.
   - Implement a user interface (text-based or graphical).
   - Record move history and display it.
   - Add AI for single-player mode.

6. **Constraints**:
   - Use appropriate encapsulation and inheritance to organize the classes.
   - Write clean and modular code with clear methods for different functionalities.