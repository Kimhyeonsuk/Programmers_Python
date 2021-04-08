import math
def findDecimal(n):
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2,n+1):
        if findDecimal(i):
            answer+=1
    return answer