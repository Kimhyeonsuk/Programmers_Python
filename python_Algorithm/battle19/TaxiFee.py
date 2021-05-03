def solution(n, s, a, b, fares):
    answer = 1e9
    board = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]

    for fare in fares:
        board[fare[0]][fare[1]] = fare[2]
        board[fare[1]][fare[0]] = fare[2]
    for i in range(1, n + 1):
        board[i][i] = 0
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if board[i][j]>board[i][k]+board[k][j]:
                    board[i][j]=board[i][k]+board[k][j]
    for k in range(1, n + 1):
        answer = min(answer, board[s][k] + board[k][a] + board[k][b])
    return answer