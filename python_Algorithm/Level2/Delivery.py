def solution(N, road, K):
    answer = 0

    downtown=[[1e9 for j in range(N+1)] for i in range(N+1)]

    for i in range(1,N+1):
        downtown[i][i]=0
    for roadinfo in road:
        s=roadinfo[0]
        d=roadinfo[1]
        val=roadinfo[2]
        downtown[s][d]=min(downtown[s][d],val)
        downtown[d][s]=min(downtown[s][d],val)
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                downtown[i][j]=min(downtown[i][j],downtown[i][k]+downtown[k][j])

    for i in range(1,N+1):
        if downtown[1][i]<=K:
            answer+=1
    return answer