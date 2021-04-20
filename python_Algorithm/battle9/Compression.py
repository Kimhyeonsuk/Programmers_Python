from collections import defaultdict
def solution(msg):
    answer = []
    dictionary=defaultdict(int)
    for i in range(26):
        char=chr(ord('A')+i)
        dictionary[char]=i+1
    idx=0
    maxNum=26
    while idx!=len(msg):
        str=msg[idx]
        isNew=False
        while dictionary[str]!=0:
            if idx==len(msg)-1:
                answer.append(dictionary[str])
                idx+=1
                break
            idx+=1
            str+=msg[idx]
            if dictionary[str]==0:
                isNew=True
                answer.append(dictionary[''.join(str[0:-1])])
                break
        if isNew:
            maxNum += 1
            dictionary[str] = maxNum

    return answer