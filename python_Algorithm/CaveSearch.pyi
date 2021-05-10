def BFS(chk,board,dic,dic2):
    cnt=1
    q=[]
    chk[0]=1
    q.append(0)
    while q:
        val=q.pop(0)
        for next in board[val]:
            if chk[next]==0:
                if next in dic and chk[dic[next]]==0:
                    chk[next]=2
                else:
                    cnt+=1
                    chk[next]=1
                    q.append(next)
                    if next in dic2 and chk[dic2[next]]==2:
                        chk[dic2[next]]=1
                        cnt+=1
                        q.append(dic2[next])
    return cnt

def solution(n, path, order):
    answer = True
    dic=dict()
    dic2=dict()
    board=[[]for _ in range(n+1)]
    for pathinfo in path:
        s=pathinfo[0]
        d=pathinfo[1]
        board[s].append(d)
        board[d].append(s)
    for orderinfo in order:
        if orderinfo[0]==0:
            continue
        if orderinfo[1]==0:
            return False
        dic[orderinfo[1]]=orderinfo[0]
        dic2[orderinfo[0]]=orderinfo[1]
    chk=[0 for _ in range(n+1)]
    if BFS(chk,board,dic,dic2)==n:
        answer=True
    else:
        answer=False
    return answer