board = []

answer = 0

for i in range(8):
    board.append(input())

fdiag = [0] * 20
bdiag = [0] * 20
columns = [0] * 20

def find(cboard, row, placed):
    global answer
    if placed == 8:
        answer += 1
        return

    for c in range(8):
        if board[row][c] == "." and fdiag[row + c] == 0 and bdiag[row + 7 - c] == 0 and columns[c] == 0:
            fdiag[row + c] = 1
            bdiag[row + 7 - c] = 1
            columns[c] = 1
            find(cboard,row + 1, placed + 1)
            fdiag[row + c] = 0
            bdiag[row + 7 - c] = 0
            columns[c] = 0

find(board, 0,0)
print(answer)
