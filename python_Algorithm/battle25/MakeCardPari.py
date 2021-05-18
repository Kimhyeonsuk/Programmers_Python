# from collections import defaultdict
# def BFS(cx,cy,gx,gy,tmpboard):
#     if cx==gx and cy==gy:
#         return 1
#     goal=tmpboard[gx][gy] # 찾아야할 값
#     q=[]
#     q.append((cx,cy,0))
#     dx=[0,0,-1,1]
#     dy=[-1,1,0,0]
#     chk=[[False for _ in range(4)]for _ in range(4)]
#     while q:
#         val=q.pop(0)
#         x=val[0]
#         y=val[1]
#         cnt=val[2]
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if nx<0 or ny<0 or nx>=4 or ny>=4:continue
#             if chk[nx][ny]:continue
#             if tmpboard[nx][ny]==goal:
#                 return cnt+2
#             q.append((nx,ny,cnt+1))
#             if tmpboard[nx][ny]==0:
#                 while (nx>=0 and ny>=0 and nx<4 and ny<4) and  tmpboard[nx][ny]==0 :
#                     nx=nx+dx[i]
#                     ny=ny+dy[i]
#                 if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
#                     nx-=dx[i]
#                     ny-=dy[i]
#                 if chk[nx][ny]:continue
#                 if tmpboard[nx][ny]==goal:
#                     return cnt+2
#                 q.append((nx,ny,cnt+1))
# def permu(dic,n,r,c,chk,visitSeq,board):
#     if len(visitSeq)==n*2:
#         global answer
#         x=r
#         y=c
#         sum=0
#         for val in visitSeq:
#             nx=val[0]
#             ny=val[1]
#             sum+=BFS(x,y,nx,ny,board)
#             board[nx][ny]=0
#             x=nx
#             y=ny
#         for key,valuelist in dic.items():
#             for value in valuelist:
#                 i=value[0]
#                 j=value[1]
#                 board[i][j]=key
#         answer=min(answer,sum)
#
#     for i in range(1,n+1):
#         if chk[i]:continue
#         chk[i]=True
#         visitSeq.append((dic[i][0]))
#         visitSeq.append((dic[i][1]))
#         permu(dic,n,r,c,chk,visitSeq,board)
#
#         visitSeq.pop()
#         visitSeq.pop()
#         visitSeq.append((dic[i][1]))
#         visitSeq.append((dic[i][0]))
#         permu(dic,n,r,c,chk,visitSeq,board)
#
#         visitSeq.pop()
#         visitSeq.pop()
#         chk[i]=False
#
# def solution(board, r, c):
#     global answer
#     answer = 1e9
#     dic=defaultdict(list)
#     for idx,boardinfo in enumerate(board):
#         for jdx,num in enumerate(boardinfo):
#             if num!=0:
#                 dic[num].append((idx,jdx))
#     chk=[False for _ in range(len(dic)+1)]
#     visitSeq=[]
#     permu(dic,len(dic),r,c,chk,visitSeq,board)
#     return answer

from collections import defaultdict
def BFS(cx,cy,gx,gy,tmpboard):
    if cx==gx and cy==gy:
        return 1
    goal=tmpboard[gx][gy] # 찾아야할 값
    q=[]
    q.append((cx,cy,0))
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    chk=[[False for _ in range(4)]for _ in range(4)]
    while q:
        val=q.pop(0)
        x=val[0]
        y=val[1]
        cnt=val[2]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=4 or ny>=4:continue
            if chk[nx][ny]:continue
            if tmpboard[nx][ny]==goal:
                return cnt+2
            q.append((nx,ny,cnt+1))
            if tmpboard[nx][ny]==0:
                while (nx>=0 and ny>=0 and nx<4 and ny<4) and  tmpboard[nx][ny]==0 :
                    nx=nx+dx[i]
                    ny=ny+dy[i]
                if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                    nx-=dx[i]
                    ny-=dy[i]
                if chk[nx][ny]:continue
                if tmpboard[nx][ny]==goal:
                    return cnt+2
                q.append((nx,ny,cnt+1))
def permu(dic,n,r,c,chk,visitSeq,board):
    if len(visitSeq)==n*2:
        global answer
        x=r
        y=c
        sum=0
        for val in visitSeq:
            nx=val[0]
            ny=val[1]
            sum+=BFS(x,y,nx,ny,board)
            board[nx][ny]=0
            x=nx
            y=ny
        for key,valuelist in dic.items():
            for value in valuelist:
                i=value[0]
                j=value[1]
                board[i][j]=key
        answer=min(answer,sum)

    for i in range(1,n+1):
        if chk[i]:continue
        chk[i]=True
        visitSeq.append((dic[i][0]))
        visitSeq.append((dic[i][1]))
        permu(dic,n,r,c,chk,visitSeq,board)

        visitSeq.pop()
        visitSeq.pop()
        visitSeq.append((dic[i][1]))
        visitSeq.append((dic[i][0]))
        permu(dic,n,r,c,chk,visitSeq,board)

        visitSeq.pop()
        visitSeq.pop()
        chk[i]=False

def solution(board, r, c):
    global answer
    answer = 1e9
    dic=defaultdict(list)
    for idx,boardinfo in enumerate(board):
        for jdx,num in enumerate(boardinfo):
            if num!=0:
                dic[num].append((idx,jdx))
    chk=[False for _ in range(len(dic)+1)]
    visitSeq=[]
    permu(dic,len(dic),r,c,chk,visitSeq,board)
    return answer