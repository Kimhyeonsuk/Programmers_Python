parent=[]
chk=False
def find(u):
    global parent
    if u==parent[u]:
        return u
    parent[u]=find(parent[u])
    return parent[u]
def union(u,v):
    global chk
    chk=False
    u=find(u)
    v=find(v)

    if u==v:
        return
    parent[u]=v
    chk=True
def solution(n, costs):
    answer = 0
    global parent
    global chk
    maplist=[]
    parent=[i for i in range(n)]
    for cost in costs:
        maplist.append(tuple(cost))
    maplist.sort(key=lambda x:x[2])
    for data in maplist:
        union(data[0],data[1])
        if chk:
            answer+=data[2]
    return answer