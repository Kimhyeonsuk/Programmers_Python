def solution(n):
    ans = 0
    while n!=1:
        if n%2==0:
            n=int(n/2)
        else:
            ans+=1
            n=n-1
    return ans+1