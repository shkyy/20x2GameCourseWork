def create_board():
    board = [['-' for _ in range(21)] for _ in range(2)]
    board[0][6] = 'O'
    board[0][13] = 'O'
    board[1][6] = 'O'
    board[1][13] = 'O'
    return board

def print_board(board):
    print('+----'*20+'+')
    for row in range(2):
        for col in range(20):
            print('|',board[row][col], ' ', end='')
        print('|')
        print('+----'*20+'+')
