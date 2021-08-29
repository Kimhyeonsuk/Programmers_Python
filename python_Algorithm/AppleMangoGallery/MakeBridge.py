import sys
def bfs(x,y):
    global chk
    global board
    global edgeInfo
    global dx
    global dy
    n=len(board)
    q=[]
    q.append((x,y))
    edges=[]
    while q:
        val=q.pop(0)
        edgeFlg = False
        for i in range(4):
            nx=val[0]+dx[i]
            ny=val[1]+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:continue
            if chk[nx][ny]==True:continue
            if board[nx][ny]==0:
                edgeFlg=True
                continue
            chk[nx][ny]=True
            q.append((nx,ny))
        if edgeFlg==True:
            edges.append((val[0],val[1]))
    edgeInfo.append(edges)
def makeBridge():
    global edgeInfo
    global res
    islandNum=len(edgeInfo)
    for i in range(islandNum):
        for j in range(i+1,islandNum):
            for val in edgeInfo[i]:
                for nval in edgeInfo[j]:
                    differ=abs(val[0]-nval[0])+abs(val[1]-nval[1])-1
                    res=min(res,differ)
def main():
    n=int(sys.stdin.readline())
    global board
    global chk
    global edgeInfo
    global dx
    global dy
    global res
    board=[]
    chk=[[False for _ in range(n)]for _ in range(n)]
    edgeInfo=[]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for _ in range(n):
        info=map(int,sys.stdin.readline().split())
        board.append(list(info))
    for i in range(n):
        for j in range(n):
            if chk[i][j]==False and board[i][j]==1:
                bfs(i,j)
    res=1e9
    makeBridge()
    print(res)
    return 0