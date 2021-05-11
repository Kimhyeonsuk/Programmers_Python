from collections import deque
answer=0

def BFS(maps):
    q=deque()
    q.append((0,0,1))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    chk=[[False for i in range(len(maps[0]))]for j in range(len(maps))]
    chk[0][0]=True
    while q:
        val=q.popleft()
        x=val[0]
        y=val[1]
        cnt=val[2]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]):continue
            if chk[nx][ny]:continue
            if maps[nx][ny]==0:continue

            if nx==len(maps)-1 and ny==len(maps[0])-1:
                return cnt+1

            chk[nx][ny]=True
            q.append((nx,ny,cnt+1))
    return -1
def solution(maps):
    return BFS(maps)