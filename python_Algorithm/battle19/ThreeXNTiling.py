def solution(n):
    answer = 0
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=0
    dp[2]=3

    for i in range(4,n+1,2):
        dp[i]+=dp[i-2]*3
        for j in range(i-4,-1,-2):
            dp[i]+=dp[j]*2
        dp[i]=dp[i]%1000000007
    return dp[n]