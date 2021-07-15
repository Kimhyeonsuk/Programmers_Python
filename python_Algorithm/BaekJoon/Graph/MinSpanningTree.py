import sys
def find(u,parent):
    if u==parent[u]:
        return u
    parent[u]=find(parent[u],parent)
    return parent[u]
def isCycle(a,b,parent):
    a=find(a,parent)
    b=find(b,parent)

    if a==b:
        return True
    parent[a]=b
    return False

def main():
    v,e=map(int,sys.stdin.readline().split())
    edge=[]
    for i in range(e):
        a,b,c=map(int,sys.stdin.readline().split())
        edge.append([a,b,c])
    parent=[i for i in range(v+1)]

    edge.sort(key=lambda x:x[2])
    res=0
    for edgeinfo in edge:
        if not isCycle(edgeinfo[0],edgeinfo[1],parent):
            res+=edgeinfo[2]
    print(res)