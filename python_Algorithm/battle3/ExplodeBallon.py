import heapq
def solution(a):
    answer = len(a)
    res=[False for i in range(len(a))]
    minleft=1e9
    minright=1e9
    for i in range(len(a)):
        if minleft>a[i]:
            minleft=a[i]
            res[i]=True
        if minright>a[-1-i]:
            minright=a[-1-i]
            res[i]=True
    return sum(res)