import sys
def solution(n, s, a, b, fares):
    answer = 0
    mx=sys.maxsize
    map=[[mx for i in range(0,n+1)] for i in range(0,n+1)]
    for fare in fares:
        map[fare[0]][fare[1]]=int(fare[2])
        map[fare[1]][fare[0]]=int(fare[2])
    for i in range(1,n+1):
        map[i][i]=0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                map[i][j]=min(map[i][j],map[i][k]+map[k][j])

    answer=mx
    for i in range(1, n+1):
        if map[s][i]==mx or map[i][a]==mx or map[i][b]==mx:
            continue
        answer=min(answer, map[s][i]+map[i][a]+map[i][b])


    return answer