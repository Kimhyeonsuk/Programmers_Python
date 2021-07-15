import sys
def find(u):
    global parent
    if u==parent[u]:
        return u
    parent[u]=find(parent[u])
    return parent[u]

def isCycle(u,v):
    u=find(u)
    v=find(v)
    if u==v:
        return True
    global parent
    parent[u]=v
    return False
def main():
    global parent
    n=int(sys.stdin.readline())
    m=int(sys.stdin.readline())
    parent=[i for i in range(n+1)]
    edge=[]
    for _ in range(m):
        a,b,c=map(int,sys.stdin.readline().split())
        edge.append((a,b,c))
    edge.sort(key=lambda x:x[2])
    answer=0
    for info in edge:
        if not isCycle(info[0],info[1]):
            answer+=info[2]
    print(answer)