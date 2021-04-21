def solution(m, n, puddles):
    answer = 0
    chkMap=[[False for i in range(m)]for j in range(n)]
    waterMap=[[0 if i!=0 and j!=0 else 1 for i in range(m) ] for j in range(n)]
    for puddle in puddles:
        chkMap[puddle[1]-1][puddle[0]-1]=True
        if puddle[1]-1==0:
            for i in range(puddle[0]-1,m):
                waterMap[0][i]=0
        if puddle[0]-1==0:
            for i in range(puddle[1]-1,n):
                waterMap[i][0]=0

    for i in range(1,n):
        for j in range(1,m):
            if chkMap[i][j]==True:
                waterMap[i][j]=0
            else:
                waterMap[i][j]=(waterMap[i-1][j]+waterMap[i][j-1])%1000000007

    return waterMap[n-1][m-1]