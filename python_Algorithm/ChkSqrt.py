import math
def solution(n):
    answer = -1
    x=int(math.sqrt(n))
    if x*x==n:
        answer=(x+1)*(x+1)
    return answer