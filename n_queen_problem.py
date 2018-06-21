import pprint

def consolidate_board(board):
    l = len(board)
    pretty_board = []
    for r in range(l):
        pretty_board.append(''.join(board[r][c] for c in range(l)))

    return pretty_board

def valid_board(board, row, column):
    l = len(board)
    #check there are no queens in that row
    for c in range(0, column):
        if board[row][c] == 'q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 'q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, l, 1), range(column, -1, -1)):
        if board[i][j] == 'q':
            return False

    return True

def place_n_queen(board, column, results):
    l = len(board)
    if column == l:
        results.append(consolidate_board(board))
        return True
    for r in range(l):
        if valid_board(board, r, column):
            board[r][column]='q'
            place_n_queen(board, column+1, results)
            board[r][column]='-'

    return False

def solveNQueen(n):
    board = [['-' for x in range(n)] for y in range(n)]
    results = []
    place_n_queen(board, 0, results)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(results)

solveNQueen(4)
