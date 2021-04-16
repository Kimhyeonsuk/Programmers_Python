def solution(board):
    answer=0
    for row in board:
        if 1 in row:
            answer=1
            break
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j]==1:
                minNum=min(board[i-1][j-1],min(board[i-1][j],board[i][j-1]))
                board[i][j]=minNum+1
                answer=max(answer,board[i][j])


    return answer*answer