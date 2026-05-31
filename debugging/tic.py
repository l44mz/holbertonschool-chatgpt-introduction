#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and \
           board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[0][0] != " " and \
       board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] != " " and \
       board[0][2] == board[1][1] == board[2][0]:
        return True

    return False


def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def get_valid_move(player):
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Coordinates must be between 0 and 2.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter numbers only.")


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    try:
        while True:
            print_board(board)

            row, col = get_valid_move(player)

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            board[row][col] = player

            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            if board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            player = "O" if player == "X" else "X"

    except KeyboardInterrupt:
        print("\nGame interrupted.")


tic_tac_toe()
