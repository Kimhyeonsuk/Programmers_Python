def solution(n, s):
    ans=[]
    if n>s:
        ans.append(-1)
    else:
        while n!=0:
            a = int(s / n)
            ans.append(a)
            n-=1
            s=s-a
    return ans