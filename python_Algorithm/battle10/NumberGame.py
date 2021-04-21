import heapq
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    while A:
        valA=A[-1]
        valB=B[-1]
        if valA<valB:
            A.pop()
            B.pop()
            answer+=1
        else:
            A.pop()
            B.pop(0)
    return answer