def solution(A,B):
    answer = 0
    idx=0
    n=len(A)
    A.sort()
    B.sort()
    for i in range(n):
        answer+=A[i]*B[-1-i]

    return answer