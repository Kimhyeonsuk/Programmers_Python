from collections import defaultdict
def solution(a):
    answer = -1
    if len(a)==1:
        answer=0
    dic=defaultdict(int)
    for num in a:
        dic[num]+=1
    dic=dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
    for key,value in dic.items():
        if value*2>len(a):
            continue
        if value*2<answer:
            break
        idx=0
        res=0
        while idx<len(a)-1:
            if a[idx]!=key and a[idx+1]==key:
                idx+=2
                res+=2
            elif a[idx]==key and a[idx+1]!=key:
                idx+=2
                res+=2
            else:
                idx+=1
        answer=max(answer,res)
    return answer
