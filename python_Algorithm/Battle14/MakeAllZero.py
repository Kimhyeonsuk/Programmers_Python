valueList=[]
def dfs(nodeMap,chk,nodeNum):
    global valueList

    for nextNum in nodeNum:
        if chk[nextNum]:continue
        chk[nextNum]=True
        valueList[nodeNum]+=valueList[nextNum]
        dfs(nodeMap,chk,nextNum)
        chk[nextNum]=False
def solution(a, edges):
    answer = -2
    N=len(a)
    global valueList
    valueList=list(a)
    nodeMap=[[]for i in range(N)]
    input=[0]*N
    chk=[False]*N
    for edge in edges:
        s=edge[0]
        d=edge[1]
        nodeMap[s].append(d)
        nodeMap[d].append(s)
    chk[0]=True
    dfs(nodeMap,chk,0)
    return answer