from collections import defaultdict
from collections import deque
answer=deque([])
def dfs(dic,here):
    global answer
    while len(dic[here])!=0:
        val=dic[here].pop()
        dfs(dic,val)
    answer.appendleft(here)

def solution(tickets):
    global answer
    dic=defaultdict(list)
    for ticket in tickets:
        s=ticket[0]
        d=ticket[1]
        dic[s].append(d)
    dfs(dic,'ICN')
    return list(answer)
