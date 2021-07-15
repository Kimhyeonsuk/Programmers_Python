import sys
sys.setrecursionlimit(10**6)
def DFS(here,board,m,n):
    global dp
    x = here[0]
    y = here[1]
    if x==m-1 and y==n-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]

    dp[x][y]=0
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=m or ny>=n:continue
        if board[nx][ny]<board[x][y]:
            dp[x][y]+=DFS([nx,ny],board,m,n)
    return dp[x][y]
def main():
    m,n=map(int,sys.stdin.readline().split())
    board=[]
    global dp
    dp=[[-1 for _ in range(n)] for _ in range(m) ]
    for _ in range(m):
        row=list(map(int,sys.stdin.readline().split()))
        board.append(row)
    print(DFS([0,0],board,m,n))