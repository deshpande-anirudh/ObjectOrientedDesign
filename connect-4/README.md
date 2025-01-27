### **Functional Requirements**
These define what the game should do.

#### **1. Core Game Logic**
1.1. The game is played on a **6-row x 7-column grid**.
1.2. Players take turns to drop discs into one of the **7 columns**.
1.3. A disc will occupy the **lowest empty slot** in the selected column (gravity-based movement).
1.4. The game ends when:
   - A player achieves **four consecutive discs** in a line (horizontally, vertically, or diagonally).
   - The board is full, resulting in a **draw**.

#### **2. Player Management**
2.1. The game should support **two players**.
2.2. Each player is assigned a color (e.g., "Red" and "Yellow").
2.3. Players should alternate turns.

#### **3. Win Condition**
3.1. A player wins if they align **four discs consecutively**:
   - Horizontally (e.g., `R R R R`).
   - Vertically (e.g., a column with `R` stacked in four slots).
   - Diagonally (e.g., from bottom-left to top-right or bottom-right to top-left).

#### **4. Input Validation**
4.1. Ensure the player selects a **valid column** (1-7).
4.2. Prevent a player from dropping a disc into a **full column**.
4.3. Handle invalid inputs gracefully (e.g., non-numeric inputs or out-of-range values).

#### **5. Board Display**
5.1. Display the board after each turn, showing the current state of the grid.
5.2. Mark empty slots with placeholders (e.g., `" "` or `"."`).

#### **6. Game End**
6.1. Declare the **winner** if one player aligns four discs.
6.2. Declare a **draw** if the board is full without a winner.
6.3. Allow an option to **restart** or exit the game after a match concludes.

### **Optional Features**
These are additional enhancements you can consider after implementing the core game.

1. **Single-Player Mode**:
   - Add an AI opponent with varying difficulty levels.
   
2. **Custom Game Rules**:
   - Allow players to configure the board size (e.g., 8x8).
   - Allow changing the "connect" goal (e.g., Connect 5).

3. **Undo/Redo**:
   - Provide players with the option to undo their last move.

4. **Visual Enhancements**:
   - Use colors for discs (e.g., `R` for red and `Y` for yellow in the terminal).
   - Create a graphical user interface (GUI) for a more immersive experience.

5. **Multiplayer Online**:
   - Enable online play where two players can compete over a network.

