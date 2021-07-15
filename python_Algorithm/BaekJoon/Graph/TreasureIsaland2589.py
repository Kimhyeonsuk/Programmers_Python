import sys
import re
from collections import deque
def BFS(i,j):
    global n, m, maxWidth,board
    global dx, dy

    q=deque()
    q.append((i,j,0))
    chk={(i,j)}
    while q:
        val=q.popleft()
        x=val[0]
        y=val[1]
        dist=val[2]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m and (nx,ny) not in chk and board[nx][ny]=='L':
                chk.add((nx,ny))
                q.append((nx,ny,dist+1))
                if maxWidth<dist+1:
                    maxWidth=dist+1
def main():
    global n,m,maxWidth,board
    global dx,dy
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    n,m=map(int,sys.stdin.readline().split())
    board=[]
    for _ in range(n):
        s=sys.stdin.readline()
        s=re.sub('\n','',s)
        board.append(list(s))
    maxWidth=0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='L':
                BFS(i,j)

    print(maxWidth)


