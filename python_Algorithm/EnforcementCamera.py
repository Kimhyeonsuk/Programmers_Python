def solution(routes):
    answer=[]
    routes.sort(key=lambda sec:sec[1] )

    loc=routes[0][1]
    cnt=1
    for i in range(1,len(routes)):
        if(routes[i][0]>=loc):
            cnt+=1
            loc=routes[i][1]
    answer=cnt
    return answer