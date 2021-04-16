def solution(s):
    answer = []
    s=s[2:-2]
    s=''.join(s).split('},{')
    s.sort(key=len)
    for i in s:
        ii=i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer