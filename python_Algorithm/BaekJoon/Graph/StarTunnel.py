import sys
def find(a):
    global parent
    if a==parent[a]:
        return a
    parent[a]=find(parent[a])
    return parent[a]
def isCycle(a,b):
    global parent
    a=find(a)
    b=find(b)

    if a==b:
        return True
    parent[a]=b
    return False
def main():
    n=int(sys.stdin.readline())
    star=[]
    for i in range(n):
        x,y,z=map(int,sys.stdin.readline().split())
        star.append((x,y,z,i))
    edge=[]
    for i in range(3):
        star.sort(key=lambda x:x[i])
        for j in range(1,n):
            edge.append((abs(star[j-1][i]-star[j][i]),star[j-1][3],star[j][3]))
    edge.sort()
    global parent
    parent=[i for i in range(n)]
    res=0
    for edgeinfo in edge:
        if not isCycle(edgeinfo[1],edgeinfo[2]):
            res+=edgeinfo[0]
    print(res)