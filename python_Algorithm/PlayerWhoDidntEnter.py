def solution(participant, completion):
    answer = ''
    list={}
    a=1
    for p in participant:
        if p in list:
            list[p]+=1
        else:
            list[p]=1

    for c in completion:
        list[c]-=1

    for a in list:
        if list[a]==1:
            answer=a
            break
    return answer