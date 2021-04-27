def solution(s):
    answer=True
    arr=[]
    for c in s:
        if c=='(':
            arr.append(c)
        else:
            if len(arr)==0:
                answer=False
                break;
            arr.pop()
    if len(arr)!=0:
        answer=False
    return answer