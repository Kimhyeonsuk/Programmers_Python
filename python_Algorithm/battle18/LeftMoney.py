def solution(n, money):
    global answer
    answer = 0
    dp=[[0 for i in range(n+1)]for i in range(len(money))]
    for i in range(n+1):
        if i%money[0]==0:
            dp[0][i]=1
    for idx in range(1,len(money)):
        moneyval=money[idx]
        for i in range(n+1):
            if i>=money[idx]:
                dp[idx][i]=(dp[idx-1][i]+dp[idx][i-moneyval])%1000000007
            else:
                dp[idx][i]=dp[idx-1][i]
    return dp[-1][-1]