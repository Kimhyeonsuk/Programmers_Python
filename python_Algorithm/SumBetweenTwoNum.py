def solution(a, b):
    answer = 0
    sum=0
    if a>b:a,b=b,a
    return sum(range(a,b+1))