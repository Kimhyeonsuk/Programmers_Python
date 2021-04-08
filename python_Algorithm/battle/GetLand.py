def solution(land):
    answer = 0
    for i in range(1,len(land)):
        for j in range(0,4):
            val=land[i][j]
            for k in range(0,4):
                if j!=k:
                    land[i][j]=max(land[i][j],val+land[i-1][k])
            answer=max(answer,land[i][j])

    return answer