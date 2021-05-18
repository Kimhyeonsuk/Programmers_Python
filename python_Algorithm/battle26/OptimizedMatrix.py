import sys
def solution(matrix_sizes):
    global answer
    answer = sys.maxsize
    n=len(matrix_sizes)
    board=[[sys.maxsize for _ in range(n)]for _ in range(n)]

    for i in range(n):
        board[i][i]=0
    for gap in range(1,n):
        for start in range(n):

            if start+gap==n:break
            end=start+gap
            for st in range(start,end):
                board[start][end]=min(board[start][end],board[start][st]+board[st+1][end]+matrix_sizes[start][0]*matrix_sizes[st][1]*matrix_sizes[end][1])
    return board[0][n-1]
