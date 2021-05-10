def solution(money):
    answer = 0
    if len(money)<=3:
        answer=max(money)
        return answer

    dp=[0]*len(money)
    dp[0]=money[0]
    for i in range(2,len(money)-1):
        dp[i]=max(dp[i-1],dp[i-2]+money[i])
    dp[0]=0
    dp[1]=money[1]
    for i in range(2, len(money)):
        dp[i]=max(dp[i-1],dp[i-2]+money[i])
    return dp[len(money)-1]