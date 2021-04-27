def BFS(x,vector,chk):
    q=[]
    q.append(x)
    chk[x]=True
    while q:
        val=q.pop(0)
        for nextNode in vector[val]:
            if chk[nextNode]==False:
                chk[nextNode]=True
                q.append(nextNode)
def solution(n, computers):
    global answer
    answer=0
    nodeNum=len(computers)
    vector=[[] for i in range(nodeNum)]
    chk=[False for i in range(nodeNum)]
    for idx,computer in enumerate(computers):
        for jdx,val in enumerate(computer):
            if val==1:
                vector[idx].append(jdx)
    for i in range(nodeNum):
        if chk[i]==False:
            BFS(i,vector,chk)
            answer+=1
    return answer