# Title: Connect 4 Game with AI
This is game coded in python programming language named **Connect 4**. This project is implemented with AI using the Minimax algorithm.

### Project Description:
This project implements a Connect 4 game with two game modes:
- Player vs. Player: Two players can compete against each other by taking turns dropping discs into the board.
- Player vs. AI: You can play against an AI opponent that uses the Minimax algorithm with alpha-beta pruning to make its moves.

### Features:
- Classic Connect 4 gameplay with a 6x7 grid.
- Clean and well-structured code using functions for different functionalities.
- User-friendly interface with clear instructions and prompts.
- AI opponent that makes strategic moves based on the Minimax algorithm.

### Dependencies:
This project uses the following libraries:
- ```tabulate```: Used for displaying the game board in a clear format.
- ```random```: Used for the AI to select an initial move (can be replaced with a more advanced selection strategy).
- ```math```: Used for the Minimax algorithm's calculations.

### Running the Game:
1. Clone or download the project repository.
2. Ensure you have python installed in pc and then install the required libraries (```pip install tabulate```) or by running this command:
```sh
pip install -r requirements.txt
```
3. Run the game by using:
```sh
python connect4.py
```
4. Choose your game mode (1 for Player vs. Player, 2 for Player vs. AI).
5. Follow the on-screen instructions to play the game.

### Gameplay:
- Players take turns dropping discs into the board by choosing a column (1-7).
- Discs fall down to the lowest available slot in the chosen column.
- The first player to connect four discs horizontally, vertically, or diagonally wins the game.
- If the board fills up and there is no winner, the game ends in a tie.

### AI Implementation:
- The AI uses the Minimax algorithm with alpha-beta pruning to evaluate potential moves and choose the one with the highest chance of winning.
- The AI considers the opponent's potential moves as well and tries to block them from achieving a winning combination.

### Note:
- The current implementation of the AI uses a simple scoring function (```score_position```). This function can be improved to take into account various factors such as the number of potential winning moves for the AI and the opponent.

### Further Development:
- Enhance the AI's decision-making by implementing a more sophisticated scoring function.
- Add difficulty levels for the AI.
- Implement a graphical user interface (GUI) for a more visually appealing experience.
- Allow customization of the game board size.

We hope you enjoy playing this Connect 4 game with AI!






