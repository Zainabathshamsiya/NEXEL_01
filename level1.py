# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (draw)
def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to get available moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# Minimax function for the AI player
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -10 + depth, None
    elif check_winner(board, 'O'):
        return 10 - depth, None
    elif is_draw(board):
        return 0, None
    
    if is_maximizing:
        best_score = float('-inf')
        best_move = None
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            score, _ = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            score, _ = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

# Function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Human's turn
        row, col = map(int, input("Enter your move (row[1-3] column[1-3]): ").split())
        row -= 1
        col -= 1
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        board[row][col] = 'X'
        print_board(board)
        
        if check_winner(board, 'X'):
            print("Congratulations! You won!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break
        
        # AI's turn
        print("AI is making its move...")
        _, best_move = minimax(board, 0, True)
        board[best_move[0]][best_move[1]] = 'O'
        print_board(board)
        
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()