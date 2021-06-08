import sys
def solution(val):
    sum=1
    left=1
    n=val[0]
    m=val[1]
    tmpm=m-n
    while m!=n:
        sum*=m
        m-=1
    while tmpm>1:
        left*=tmpm
        tmpm-=1
    return sum//left
T=int(sys.stdin.readline())
for i in range(T):
    val=tuple(map(int,sys.stdin.readline().split()))
    res=solution(val)
    print(res)
