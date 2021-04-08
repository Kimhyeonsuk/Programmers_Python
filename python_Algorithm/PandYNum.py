def solution(s):
    answer = True
    s=''.join(s).lower()
    pNum=0
    yNum=0
    for i in s:
        if i=='p':
            pNum+=1
        if i=='y':
            yNum+=1

    return pNum==yNum