# Develop a Tic-Tac-Toe game for two players using the Minimax algorithm for intelligent moves.

board = [' '] * 9
def print_board():
    print(
        f"{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}")

def check_win(p):

    for i in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if board[i[0]] == board[i[1]] == board[i[2]] == p:
            return True
    return False

player = 'X'
for _ in range(9):
    print_board()
    move = int(input(f"{player}'s turn (0-8): "))
    if board[move] == ' ':
        board[move] = player
        if check_win(player):
            print_board()
            print(player, "wins!")
            break
        player = 'O' if player == 'X' else 'X'
    else:
        print_board()
        print("Draw!")