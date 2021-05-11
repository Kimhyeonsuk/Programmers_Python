def BFS(start,computer,chk):
    q=[]
    q.append(start)
    chk[start]=True
    while q:
        here=q.pop(0)
        for adjidx,num in enumerate(computer[here]):
            if adjidx==here:continue
            if chk[adjidx]:continue
            if num==0:continue
            chk[adjidx]=True
            q.append(adjidx)

def solution(n, computers):
    answer = 0
    chk=[False for _ in range(n)]
    for i in range(n):
        if not chk[i]:
            BFS(i,computers,chk)
            answer+=1
    return answer