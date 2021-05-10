def spin(key):
    m=len(key)
    key2=[[0 for _ in range(m)]for _ in range(m)]
    for i in range(m):
        for j in range(m):
            key2[j][m-i-1]=key[i][j]
    return key2
def chk(x,y,board,key,n,m,boardlen):
    tmp=[[0 for _ in range(boardlen)]for _ in range(boardlen)]
    for i in range(boardlen):
        for j in range(boardlen):
            tmp[i][j]=board[i][j]
    for i in range(x, x+m):
        for j in range(y, y+m):
            tmp[i][j]+=key[i-x][j-y]
    for i in range(m-1,m-1+n):
        for j in range(m-1,m-1+n):
            if tmp[i][j]!=1:
                return False
    return True
def solution(key, lock):
    answer = False
    key2=spin(key)
    key3=spin(key2)
    key4=spin(key3)
    n=len(lock)
    m=len(key)
    boardlen=n+(m-1)*2
    board=[[0 for _ in range(boardlen)]for _ in range(boardlen)]
    for i in range(m-1,m-1+n):
        for j in range(m-1,m-1+n):
            board[i][j]=lock[i-(m-1)][j-(m-1)]
    for i in range(n+m-1):
        for j in range(n+m-1):
            if chk(i,j,board,key,n,m,boardlen):
                answer=True
                break
            elif chk(i,j,board,key2,n,m,boardlen):
                answer=True
                break
            elif chk(i,j,board,key3,n,m,boardlen):
                answer=True
                break
            elif chk(i,j,board,key4,n,m,boardlen):
                answer=True
                break
        if answer:
            break
    return answer