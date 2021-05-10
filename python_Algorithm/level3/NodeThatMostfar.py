def BFS(board,chk):
    global answer
    answer=0
    q=[]
    q.append((1,0))
    chk[1]=True
    longestDistance=0
    while q:
        val=q.pop(0)
        here=val[0]
        cnt=val[1]
        for num in board[here]:
            if chk[num]:continue
            chk[num]=True
            if cnt+1>longestDistance:
                answer=1
                longestDistance=cnt+1
            elif cnt+1==longestDistance:
                answer+=1
            q.append((num,cnt+1))
def solution(n, edge):
    global answer
    board=[[]for _ in range(n+1)]
    chk=[False for _ in range(n+1)]
    for edgeinfo in edge:
        board[edgeinfo[0]].append(edgeinfo[1])
        board[edgeinfo[1]].append(edgeinfo[0])
    BFS(board,chk)
    return answer