def solution(triangle):
    answer = 0
    n=len(triangle)
    answer=triangle[0][0]
    for i in range(1,n):
        for j in range(i+1):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==i:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j],triangle[i-1][j-1])
            answer=max(answer,triangle[i][j])


    return answer