def solution(brown, yellow):
    answer = []
    for i in range(1,int(yellow/2)+1):
        if yellow%i==0:
            a=i
            b=int(yellow/i)
            if brown==(a)*2 + (b+2)*2:
                answer.append(b+2)
                answer.append(a+2)
                break
    if yellow==1:
        answer.append(3)
        answer.append(3)
    return answer