def great():
    print("Good moring")
    print("Welcome to the Tic-Tac-Toe game!")
    print("Player X goes first. To make a move, enter the row and column numbers (1-3) separated by a space.")
    print("Entering '1 2' will place your mark in the first row and second column.")

def display_board(board):
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row))
        print("---------")


def get_move(player, board):
    while True:
        move = input(f"Player {player}, enter your move as row and column (1-3, separated by a space): ")
        parts = move.strip().split()
        if len(parts) != 2:
            print("Please enter two numbers separated by a space.")
            continue

        if not all(part.isdigit() for part in parts):
            print("Please enter valid numbers.")
            continue

        row, col = map(int, parts)
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Row and column must be between 1 and 3.")
            continue

        if board[row - 1][col - 1] != " ":
            print("That cell is already taken. Choose another one.")
            continue

        return row - 1, col - 1


def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[row][i] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def board_full(board):
    return all(cell != " " for row in board for cell in row)


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")

    while True:
        display_board(board)
        row, col = get_move(current_player, board)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if board_full(board):
            display_board(board)
            print("The game is a draw.")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing Tic-Tac-Toe!")
            break


if __name__ == "__main__":
    main()
