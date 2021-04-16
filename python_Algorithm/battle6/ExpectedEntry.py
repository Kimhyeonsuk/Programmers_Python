def solution(n,a,b):
    answer = 0
    a=a-1
    b=b-1
    cnt=0
    number=n
    while number!=1:
        number=int(number/2)
        cnt+=1
    n=int(n/2)
    while int(a/n)==int(b/n):
        cnt-=1
        n=int(n/2)
    return cnt