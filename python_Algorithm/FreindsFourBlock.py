def chkBoard(m,n,board,chklist):
    for i in range(m-1):
        for j in range(n-1):
            val=board[i][j]
            if val!=' 'and board[i+1][j]==val and board[i][j+1]==val and board[i+1][j+1]==val:
                chklist.append((i,j))
def deleteBoard(board,chklist):
    global answer
    while chklist:
        val= chklist.pop()
        x=val[0]
        y=val[1]
        if board[x][y]!=' ':
            answer+=1
        if board[x+1][y]!=' ':
            answer+=1
        if board[x][y+1]!=' ':
            answer+=1
        if board[x+1][y+1]!=' ':
            answer+=1
        board[x][y]=' '
        board[x+1][y]=' '
        board[x][y+1]=' '
        board[x+1][y+1]=' '
def moveBoard(m,n,board):
    for i in range(m-1,-1,-1):
        for j in range(n):
            val=board[i][j]
            if val!=' ':
                x=i
                y=j
                while True:
                    nx=x+1
                    if nx>=m or board[nx][y]!=' ':
                        break
                    else:
                        x=nx
                board[i][j]=' '
                board[x][y]=val
def solution(m, n, board):
    global answer
    m=6
    n=6
    board=["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
    for i in range(m):
        board[i]=list(board[i])
    answer = 0
    chklist=[]

    while(True):
        chkBoard(m,n,board,chklist)
        if len(chklist)==0:
            break
        deleteBoard(board,chklist)
        moveBoard(m,n,board)
    return answer