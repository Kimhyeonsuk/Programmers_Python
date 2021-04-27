
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
def solution(n, k):
    answer = []

    arr=[i for i in range(1,n+1)]
    k-=1
    while arr:
        fact=factorial(n)
        unit=fact//n

        val=k//unit
        answer.append(arr[val])
        arr.pop(val)
        n=n-1
        k=k%unit
    return answer