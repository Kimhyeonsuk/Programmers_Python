def solution(cookie):
    answer = 0
    for idx in range(len(cookie)-1):
        i,s1=idx ,cookie[idx]
        r,s2=idx+1,cookie[idx+1]
        while True:
            if s1==s2:
                answer=max(answer,s1)
                if i==0:break
                i-=1
                s1+=cookie[i]
            elif s1<s2:
                if i==0:break
                i-=1
                s1+=cookie[i]
            elif s1>s2:
                if r==len(cookie)-1:break
                r+=1
                s2+=cookie[r]


    return answer