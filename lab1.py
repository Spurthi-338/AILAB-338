board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

def print_board():
    for row in board:
        print(row)

def check_winner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def play_game():
    print_board()
    for turn in range(9):
        if turn % 2 == 0:
            player = 'X'
        else:
            player = 'O'

        print(f"Enter position to place {player}: ")
        row = int(input("Row (1-3): ")) - 1
        col = int(input("Column (1-3): ")) - 1

        if board[row][col] == '-':
            board[row][col] = player
        else:
            print("Cell already taken, try again!")
            continue

        print_board()

        if check_winner(player):
            print(f"{player} wins")
            print("Game Over")
            return

    print("It's a Draw!")
    print("Game Over")

play_game()
