def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for row in board:
        if all(spot == player for spot in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def board_full(board):
    return all(spot != ' ' for row in board for spot in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current = 'X'
    while True:
        print_board(board)
        print(f"Player {current}'s turn.")
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] != ' ':
                print("Spot taken, try again.")
                continue
            board[row][col] = current
            if check_winner(board, current):
                print_board(board)
                print(f"Player {current} wins!")
                break
            if board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current = 'O' if current == 'X' else 'X'
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers 1-3.")

tic_tac_toe()
               
