def solution(clothes):
    answer = 1
    closet=dict([])
    for cloth in clothes:
        if cloth[1] in closet:
            closet[cloth[1]]+=1
        else:
            closet[cloth[1]]=1
    for a in closet.keys():
        answer*=(closet[a]+1)
    return answer-1