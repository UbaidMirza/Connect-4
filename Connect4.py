# Title: Connect 4 Game
from tabulate import tabulate
import random
import math

#Initializing Global Variables
ROWS = 6
COLS = 7
player = "X"
AI_PIECE = "O"
PLAYER_PIECE = "X"

#Main Function
def main():
    #Creation of board and prompting the user to choose the mode
    board = create_board()
    game_over = False
    while True:
        try:
            mode = input("Enter '1' to play with a friend or '2' to play with AI: ")
            if mode not in ('1', '2'):
                raise ValueError
            break
        except ValueError:
            print("Invalid input!")
    show_board(board)

    #Game Engine Loop
    while not game_over:
        if mode == "1":
            col = int(input(f"Player {player}, choose a column (1-7): ")) - 1
            if col < 0 or col >= COLS:
                print("Invalid column! Choose a column between 1 and 7.")
                continue
            if board[1][col] != "":
                print("Column is full! Choose another column.")
                continue
            game_over = insert_disc(board, col, player)
            if not game_over:
                game_over = check_tie(board)
            switch_player()
        elif mode == "2":
            if player == PLAYER_PIECE:
                col = int(input(f"Player {player}, choose a column (1-7): ")) - 1
                if col < 0 or col >= COLS:
                    print("Invalid column! Choose a column between 1 and 7.")
                    continue
                if board[1][col] != "":
                    print("Column is full! Choose another column.")
                    continue
                game_over = insert_disc(board, col, player)
                if not game_over:
                    game_over = check_tie(board)
            else:
                col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)
                game_over = insert_disc(board, col, AI_PIECE)
                if not game_over:
                    game_over = check_tie(board)
            switch_player()
        if mode == "2" and not game_over and player == PLAYER_PIECE:
            show_board(board)
        elif mode == "1" and not game_over:
            show_board(board)

# Create board with the first row as column labels
def create_board():
    board = [list(range(1, COLS + 1))]
    for _ in range(ROWS):
        board.append([""] * COLS)  # Initialize all cells to empty strings
    return board

# Display the board using tabulate
def show_board(board):
    print(tabulate(board, headers="firstrow", tablefmt="grid"))

# Switch player after each turn
def switch_player():
    global player
    player = "O" if player == "X" else "X"

# Check if the current player has won
def check_winner(board, piece):
    # Check horizontal locations for win
    for c in range(COLS-3):
        for r in range(1, (ROWS+1)):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLS):
        for r in range(ROWS-2):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLS-3):
        for r in range(ROWS-2):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLS-3):
        for r in range(3, ROWS+1):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

# Check if the game is a tie
def check_tie(board):
    for col in range(COLS):
        if board[1][col] == "":
            return False
    show_board(board)
    print("It's a tie!")
    return True

# Get all valid locations where a piece can be inserted
def get_valid_locations(board):
    valid_locations = []
    for col in range(COLS):
        if board[1][col] == "":
            valid_locations.append(col)
    return valid_locations

# Check if the current node is a terminal node
def is_terminal_node(board):
    return check_winner(board, PLAYER_PIECE) or check_winner(board, AI_PIECE) or len(get_valid_locations(board)) == 0

# This is a placeholder implementation (can be improved later)
def score_position(board, piece):
    # Implement a scoring function for the board
    return random.randint(0, 100)

# Get the next open row in the column
def get_next_open_row(board, col):
    for r in range(ROWS, 0, -1):
        if board[r][col] == "":
            return r

# Drop a piece in the board (directly modifies the board)
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# AI Engine (Minimax algorithm with alpha-beta pruning)
def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_winner(board, AI_PIECE):
                return (None, 100000000000000)
            elif check_winner(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else: # Game is over, no more valid moves
                return (None, 0)
        else: # Depth is zero
            return (None, score_position(board, AI_PIECE))
    if maximizingPlayer: # Maximizing player
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [row[:] for row in board]
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else: # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = [row[:] for row in board]
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

# Insert a disc in the board using drop_piece and check if the player has won by calling check_winner
def insert_disc(board, col, piece):
    row = get_next_open_row(board, col)
    drop_piece(board, row, col, piece)
    if check_winner(board, piece):
        show_board(board)
        print(f"Player {piece} wins!")
        return True
    return False

if __name__ == "__main__":
    main()