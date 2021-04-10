def solution(triangle):
    answer = triangle[0][0]
    for idx in range(1,len(triangle)):
        for jdx in range(0,len(triangle[idx])):
            if jdx==0:
                triangle[idx][jdx]+=triangle[idx-1][jdx]
            elif jdx==len(triangle[idx-1]):
                triangle[idx][jdx]+=triangle[idx-1][jdx-1]
            else:
                triangle[idx][jdx]+=max(triangle[idx-1][jdx-1],triangle[idx-1][jdx])

            answer=max(answer,triangle[idx][jdx])
    return answer