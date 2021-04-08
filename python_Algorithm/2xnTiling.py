def solution(n):
    answer = 0
    a,b=1
    for i in range(2,n+1):
        answer=a+b
        a=b
        b=answer
    return answer