"""
CODSOFT AI Internship - Task 2
Tic-Tac-Toe AI using the Minimax algorithm.

Run:
    python tic_tac_toe.py
"""

import math


def print_board(board):
    print("\n")
    for row in range(3):
        print(" " + " | ".join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print("---+---+---")
    print()


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == " "]


def check_winner(board):
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(board, maximizing):
    """
    Minimax evaluates every possible future game state.
    X is the AI and O is the human player.
    """
    result = check_winner(board)

    if result == "X":
        return 1
    if result == "O":
        return -1
    if result == "Draw":
        return 0

    if maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = "X"
            score = minimax(board, False)
            board[move] = " "
            best_score = max(best_score, score)
        return best_score

    best_score = math.inf
    for move in available_moves(board):
        board[move] = "O"
        score = minimax(board, True)
        board[move] = " "
        best_score = min(best_score, score)
    return best_score


def best_move(board):
    """Return the optimal move for the AI."""
    best_score = -math.inf
    move_choice = None

    for move in available_moves(board):
        board[move] = "X"
        score = minimax(board, False)
        board[move] = " "

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice


def human_move(board):
    """Read and validate the human player's move."""
    while True:
        choice = input("Enter your move (1-9): ").strip()

        if not choice.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice) - 1

        if position not in range(9):
            print("Please enter a number from 1 to 9.")
        elif board[position] != " ":
            print("That position is already occupied.")
        else:
            return position


def main():
    board = [" "] * 9

    print("=" * 45)
    print("           TIC-TAC-TOE AI")
    print("=" * 45)
    print("You are O. The AI is X.")
    print("Choose positions using the following layout:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:
        print_board(board)

        # Human turn
        move = human_move(board)
        board[move] = "O"

        result = check_winner(board)
        if result:
            print_board(board)
            break

        # AI turn
        print("AI is thinking...")
        ai_move = best_move(board)
        board[ai_move] = "X"

        result = check_winner(board)
        if result:
            print_board(board)
            break

    if result == "X":
        print("AI wins! Minimax found the best move.")
    elif result == "O":
        print("Congratulations! You beat the AI.")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
