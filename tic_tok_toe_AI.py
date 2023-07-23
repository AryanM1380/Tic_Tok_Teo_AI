def initialize_board():
           return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-----')

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def evaluate(board):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif depth == 0:
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth - 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth - 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def ai_move(board):
    best_move = None
    best_eval = float('-inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_eval = minimax(board, 0, False)
                board[i][j] = ' '
                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = 'X'

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

def main():
    board = initialize_board()

    while True:
        print_board(board)

        if check_winner(board, 'X'):
            print("AI wins!")
            break
        elif check_winner(board, 'O'):
            print("Player wins!")
            break
        elif all([cell != ' ' for row in board for cell in row]):
            print("It's a tie!")
            break

        player_move(board)

        if all([cell != ' ' for row in board for cell in row]):
            print("It's a tie!")
            break

        ai_move(board)

if __name__ == "__main__":
    main()
