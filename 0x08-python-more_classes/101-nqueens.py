#!/usr/bin/python3
""" this module attempts to solve a chess problem """
import sys


def init_chessboard(n):
    """ init n X n chessboard size """
    chess_board = []
    [chess_board.append([]) for i in range(n)]
    [row.append(" ") for i in range(n) for row in chess_board]
    return chess_board

def copy_chess_board(chess_board):
    """ copying chess_board """
    if isinstance(board, list):
        return list(map(copy_chess_board, chess_board))
    return (chess_board)

def chess_soln(chess_board):
    """ list representatio of sloved chessboard """
    soln = []
    for x in range(len(chess_board)):
        for y in range(len(chess_board)):
            if chess_board[x][y] == "Q":
                soln.append([x, y])
                break
    return soln

def xout(chess_board, row, col):
    """
    chessboard design(spots)

    parameters:
        chessboard
        row
        column
    """
    #forward
    for c in range(col + 1, len(chess_board)):
        chess_board[row][c] = "x"
    #backward
    for c in range(col - 1, -1, -1):
        chess_board[row][c] = "x"
    #below
    for r in range(row + 1, len(chess_board)):
        chess_board[r][col] = "x"
    #above
    for r in range(row -1, -1, -1):
        chess_board[r][col] = "x"
    #rigght & down
    c = col + 1
    for r in range(row +1, len(chess_board)):
        if c >= len(chess_board):
            break
        chess_board[r][c] = "x"
        c += 1
    #all spots
    c = col - 1
    for r in range(row -1, -1, -1):
        if c < 0:
            break
        chess_board[r][c] = "x"
        c -= 1
    #diagonal and left
    c = col -1
    for r in range(row + 1, len(chess_board)):
        if c < 0:
            break
        chess_board[r][c] = "x"

    def solve(chess_board, rew, queens, solns):
        """
        solving n queens problem

        parameters:
            chessboard
            row
            queens
            solns
        """
        if queens == len(chess_board):
            solns.append(chess_soln(chess_board))
            return solns

        for c in range(len(chess_board)):
            if chess_board[row][c] == " ":
                tmp_board = copy_chess_board(chess_board)
                tmp_board[row][c] = "Q"
                xout(tmp_board, row, c)
                solns = solve(tmp_board, row + 1, queens + 1, solns)
        return solns

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        if sys.argv[1].isdigit() is False:
            print("N must be a number")
            sys.exit(1)
        if int(sys.argv[1]) < 4:
            print("N must be at least 4")
            sys.exit(1)

        chess_board = init_chessboard(int(sys.argv[1]))
        solns = solve(chess_board, 0, 0, [])
        for sol in solns:
            print(sol)
