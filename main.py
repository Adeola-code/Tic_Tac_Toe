def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Row winner
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Column winner
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Diagonal winner
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Diagonal winner
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False  # Board is not full
    return True  # Board is full

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
