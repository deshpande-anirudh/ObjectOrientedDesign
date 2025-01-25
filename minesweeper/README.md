### **Problem Statement**
Design a simplified version of the classic Minesweeper game. Minesweeper is a grid-based game where cells either contain a mine or are empty. The objective is to uncover all cells that do not contain mines without triggering any mines. If a cell containing a mine is clicked, the game ends. If an empty cell is clicked, it reveals the number of adjacent mines. If the cell has no adjacent mines, it recursively uncovers neighboring cells.

---

### **Requirements**
1. **Game Setup:**
   - The game should have a grid-based board (e.g., 2D grid of `n x m` cells).
   - Some cells on the board contain mines. The number of mines is predefined.
   - The player does not know which cells contain mines.
   - The board can vary in size and difficulty (e.g., easy, medium, hard).

2. **Gameplay Rules:**
   - Clicking on a cell reveals:
     - The number of mines in adjacent cells (if the cell does not contain a mine).
     - All neighboring cells recursively, if the cell and its neighbors have no adjacent mines.
     - A mine if the clicked cell contains one (game over).
   - The player wins if all non-mine cells are revealed.
   - The player loses if they click on a mine.

3. **Features:**
   - Flagging: Players can mark cells they suspect contain mines.
   - Restart: The game can be restarted with a new board.
   - Input handling: Allow the player to click cells or flag/unflag them.

4. **Scalability:**
   - Design the game to accommodate varying board sizes and mine counts.

5. **Constraints:**
   - Ensure efficient algorithms for revealing adjacent cells.
   - Support a reasonable maximum board size (e.g., 100x100).

---

### **Expected Outputs**
- **Initialization:**
  - Board with cells hidden, randomly distributed mines.
- **Click Action:**
  - Reveal the clicked cell.
  - If a mine is clicked, display a "Game Over" message.
  - If a non-mine cell is clicked, reveal numbers or recursively uncover neighbors.
- **Flagging:**
  - Mark cells to indicate possible mines.
- **Endgame:**
  - Win: All non-mine cells are revealed.
  - Lose: A mine is clicked.

---

### **Evaluation Points**
1. **Object-Oriented Design:**
   - Identify the key objects and their relationships (e.g., `Board`, `Cell`, `Game`, `Player`).
   - Use appropriate design principles (e.g., Single Responsibility, Open/Closed).

2. **Class Design:**
   - Define attributes and methods for each class.
   - Encapsulation of logic within the right classes.

3. **Algorithm Design:**
   - Efficiently handle recursive uncovering of neighboring cells.
   - Properly manage the distribution of mines.

4. **Extensibility:**
   - Add features like time tracking, scorekeeping, or different game modes.

5. **Edge Cases:**
   - Clicking on a flagged cell.
   - Clicking on an already revealed cell.
   - Ensuring the first click is never a mine.

---

### **Hints (if needed during the interview)**
- Suggest breaking the problem into smaller pieces, like modeling the `Cell` class first.
- Emphasize focusing on the core functionality before adding features like flagging.
- Guide them toward efficient use of data structures (e.g., using a queue for recursive uncovering).
