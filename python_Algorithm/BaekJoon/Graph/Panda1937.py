import sys
sys.setrecursionlimit(10**6)
def DFS(x,y,board):
    global zoo
    global answer
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    n=len(board)
    if zoo[x][y]!=-1:
        return zoo[x][y]

    val=0
    zoo[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<n:
            if board[nx][ny]>board[x][y]:
                val=max(val,DFS(nx,ny,board))
    zoo[x][y]+=val
    answer=max(answer,zoo[x][y])
    return zoo[x][y]
def main():
    n=int(sys.stdin.readline())
    board=[]
    for i in range(n):
        row=list(map(int,sys.stdin.readline().split()))
        board.append(row)
    global zoo
    zoo=[[-1 for _ in range(n)]for _ in range(n)]
    global answer
    answer = 0
    for i in range(n):
        for j in range(n):
            DFS(i,j,board)
    print(answer)