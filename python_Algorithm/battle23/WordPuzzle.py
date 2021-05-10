def solution(strs, t):
    answer = 0
    dic=set(strs)
    dp=[1e9]*(len(t)+1)
    dp[0]=0
    for i in range(1,len(t)):
        for j in range(1,6):
            if i-j<0:
                if t[0:i] in dic:
                    dp[i]=min(dp[i],dp[0]+1)
            else:
                if t[i-j:i] in dic:
                    dp[i]=min(dp[i],dp[i-j]+1)
    if dp[-1]==1e9:
        dp[-1]=-1
    return dp[-1]