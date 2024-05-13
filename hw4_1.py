import random

def create_board():
    board_size = 9
    num_mines = 10
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    mines_placed = 0

    while mines_placed < num_mines:
        x = random.randint(0, board_size - 1)
        y = random.randint(0, board_size - 1)
        if board[x][y] != -1:
            board[x][y] = -1
            mines_placed += 1
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < board_size and 0 <= j < board_size and board[i][j] != -1:
                        board[i][j] += 1

    return board

def print_board(board, revealed, flags):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                print(board[i][j], end=" ")
            elif flags and flags[i][j]:
                print("F", end=" ")
            else:
                print("-", end=" ")
        print()



def make_move(board, revealed, x, y, flag=False):
    if flag:
        # Flagging a spot
        if not revealed[x][y]:
            revealed[x][y] = True
            print("Flag placed at position ({}, {}).".format(x, y))
        else:
            print("Flag already placed at position ({}, {}).".format(x, y))
    else:
        if revealed[x][y]:
            print("This spot has already been revealed.")
            return
        revealed[x][y] = True
        if board[x][y] == -1:
            print("Game Over! You hit a mine.")
            print_board(board, revealed, [])
            return True
        elif board[x][y] == 0:
            reveal(board, revealed, x, y)
    return False


def reveal(board, revealed, x, y):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < len(board) and 0 <= j < len(board) and not revealed[i][j]:
                revealed[i][j] = True
                if board[i][j] == 0:
                    reveal(board, revealed, i, j)

def play_game():
    board = create_board()
    revealed = [[False for _ in range(9)] for _ in range(9)]
    flags = [[False for _ in range(9)] for _ in range(9)]

    while True:
        print_board(board, revealed, flags)
        action = input("Enter 'r' to reveal, 'f' to flag: ")
        if action == 'R':
            y = int(input("Enter row (x): "))
            x = int(input("Enter column (y): "))
            if not (0 <= x < 9 and 0 <= y < 9):
                print("Invalid position. Try again.")
                continue
            if make_move(board, revealed, x, y):
                break
        elif action == 'F':
            y = int(input("Enter row (x) to place flag: "))
            x = int(input("Enter column (y) to place flag: "))
            if not (0 <= x < 9 and 0 <= y < 9):
                print("Invalid position. Try again.")
                continue
            flags[x][y] = True  # Place flag
        else:
            print("Invalid action. Try again.")

    if all(revealed[i][j] or board[i][j] == -1 for i in range(9) for j in range(9)):
        print("Congratulations! You win!")
    else:
        print("Game over!")



play_game()
