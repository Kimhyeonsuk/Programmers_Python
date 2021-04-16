from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def BFS(board):
    boardlen=len(board)
    chk = [[1e9 for j in range(boardlen)] for i in range(boardlen)]
    chk[0][0] = 0
    q=deque()
    q.append((0,0,0,-1))
    while q:
        val=q.popleft()
        tx=val[0]
        ty=val[1]
        sum=val[2]
        dir=val[3]
        for i in range(4):
            nx=tx+dx[i]
            ny=ty+dy[i]
            nextcost=0
            if dir == -1 or dir == i:
                nextcost=100
            else:
                nextcost=600

            if nx < 0 or ny < 0 or nx >= boardlen or ny >= boardlen: continue
            if board[nx][ny] == 1: continue
            if chk[nx][ny]<sum+nextcost:continue
            chk[nx][ny]=sum+nextcost
            q.append((nx,ny,sum+nextcost,i))
    return chk[boardlen-1][boardlen-1]
def solution(board):
    return  BFS(board)


# def dfs(x,y,board,dir,sum):
#     global dx
#     global dy
#     global res
#     if x==len(board)-1 and y==len(board)-1:
#         res=min(res,sum)
#         return
#
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if nx<0 or ny<0 or nx>=len(board) or ny>=len(board):continue
#         if board[nx][ny]==1:continue
#         if chk[nx][ny]:continue
#         chk[nx][ny]=True
#         if dir==i or dir==-1:
#             dfs(nx,ny,board,i,sum+100)
#         else:
#             dfs(nx,ny,board,i,sum+600)
#         chk[nx][ny]=False