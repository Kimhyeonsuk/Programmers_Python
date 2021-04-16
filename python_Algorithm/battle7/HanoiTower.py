answer=[]
def hanoi(n,fr,to,mid):
    if n==1:
        global answer
        answer.append([fr,to])
        return
    hanoi(n - 1, fr, mid, to)
    hanoi(1, fr, to, mid)
    hanoi(n - 1, mid, to, fr)
    return
def solution(n):
    global answer
    hanoi(n,1,3,2)
    return answer