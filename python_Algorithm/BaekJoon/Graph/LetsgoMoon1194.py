import sys
import re
# 빈곳 : 언제나 이동 가능 .
# 벽 : 이동 불가 #
# 열쇠 : 이동가능, 열쇠를 집음 a~f
# 문 :  대응하는 열쇠가 있을때만 이동 A~F
# 민식이 위치 : 0
# 출구 1
# 한번의 움직임은 현재 위치에서 수평이나 수직으로 한칸 이동
# 탈출하는데 걸리는 이동 횟수의 최솟값
#위치, 열쇠 내용(set) ,이동횟수
def BFS():
    global n
    global m
    global board
    global chlsu
    chk=[[[0]*64 for _ in range(m)]for _ in range(n)]
    q=[]
    q.append([chlsu[0],chlsu[1],0,0])
    chk[chlsu[0]][chlsu[1]][0]=1
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    while q:
        node=q.pop(0)
        x=node[0]
        y=node[1]
        z=node[2]
        cnt=node[3]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m:
                if board[nx][ny]=='1':
                   return cnt+1
                elif board[nx][ny]=='.'and chk[nx][ny][z]==0:
                    chk[nx][ny][z]=1
                    q.append([nx,ny,z,cnt+1])
                elif ord('a')<=ord(board[nx][ny])<=ord('z') and chk[nx][ny][z]==0:
                    chk[nx][ny][z]=1
                    nz=z|1<<ord(board[nx][ny])-ord('a')
                    q.append([nx,ny,nz,cnt+1])
                elif ord('A')<=ord(board[nx][ny])<=ord('z') and chk[nx][ny][z]==0:
                    alp=1<<ord(''.join(board[nx][ny]).lower())-ord('a')
                    if z & alp!=0:
                        chk[nx][ny][z]=1
                        q.append([nx,ny,z,cnt+1])
    return -1
def main():
    global n
    global m
    global board
    global chlsu
    n,m=tuple(map(int,sys.stdin.readline().split()))
    board=[]
    chlsu=[]
    for i in range(n):
        s=sys.stdin.readline()
        val=s.find('0')
        if val!=-1:
            chlsu.append(i)
            chlsu.append(val)
        s=re.sub('0','.',s)
        s=re.sub('\n','',s)
        board.append(list(s))
    ans=BFS()
    print(ans)