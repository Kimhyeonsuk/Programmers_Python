from collections import deque
def solution(operations):
    answer = []
    queue=deque()
    for str in operations:
        newStr=''+str
        sp=newStr.split(' ')
        if(sp[0]=='I'):
            answer.append(int(sp[1]))
        elif sp[1]=='1'and answer:
            answer.remove(max(answer))
        elif(sp[1]=='-1') and answer:
            answer.remove(min(answer))

    if not answer:
        answer=[0,0]
    else:
        answer=[max(answer),min(answer)]
    return answer