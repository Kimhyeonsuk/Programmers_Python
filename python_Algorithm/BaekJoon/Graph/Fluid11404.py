import sys
def main():
    n=int(sys.stdin.readline())
    m=int(sys.stdin.readline())
    fluid=[[1e9 for _ in range(n+1)]for _ in range(n+1)]
    for _ in range(m):
        a,b,c=map(int,sys.stdin.readline().split())
        fluid[a][b]=min(fluid[a][b],c)

    for i in range(1,n+1):
        fluid[i][i]=0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if fluid[i][j]>fluid[i][k]+fluid[k][j]:
                    fluid[i][j]=fluid[i][k]+fluid[k][j]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if fluid[i][j]==1e9:
                print(0,end=' ')
            else:
                print(fluid[i][j],end=' ')
        print('')