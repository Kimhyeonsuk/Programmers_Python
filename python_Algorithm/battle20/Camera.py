def solution(routes):
    answer = 0
    routes.sort(key=lambda out:out[1])
    here=routes[0][1]
    answer=1
    for route in routes:
        if here>=route[0]:continue
        answer+=1
        here=route[1]
    return answer