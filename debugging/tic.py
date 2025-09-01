def get_valid_input(prompt, valid_range):
    """Get valid integer input within specified range with error handling."""
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Invalid input! Please enter a number between {min(valid_range)} and {max(valid_range)}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def check_board_full(board):
    """Check if the board is full (tie game)."""
    for row in board:
        if " " in row:
            return False
    return True

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board) and not check_board_full(board):
        print_board(board)
        print(f"\nPlayer {player}'s turn")
        
        # Get valid row input
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {player}: ", [0, 1, 2])
        
        # Get valid column input
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {player}: ", [0, 1, 2])
        
        # Check if the spot is available
        if board[row][col] == " ":
            board[row][col] = player
            # Switch players
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    # Display final board
    print_board(board)
    
    # Determine and announce the result
    if check_winner(board):
        # Switch back to get the winner (since we switched after the winning move)
        winner = "O" if player == "X" else "X"
        print(f"Player {winner} wins!")
    elif check_board_full(board):
        print("It's a tie! The board is full.")
    else:
        print("Game ended unexpectedly.")

tic_tac_toe()

