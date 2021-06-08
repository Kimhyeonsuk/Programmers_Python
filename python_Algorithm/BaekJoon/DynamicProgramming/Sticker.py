import sys
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    sticker=[]
    dp=[[0 for _ in range(n)] for _ in range(2)]
    for j in range(2):
        nums=list(map(int,sys.stdin.readline().split()))
        sticker.append(nums)
    dp[0][0]=sticker[0][0]
    dp[1][0]=sticker[1][0]
    for k in range(1,n):
        if k==1:
            dp[0][1]=sticker[0][1]+dp[1][0]
            dp[1][1]=sticker[1][1]+dp[0][0]
        else:
            dp[0][k]=sticker[0][k]+max(dp[1][k-1],max(dp[0][k-2],dp[1][k-2]))
            dp[1][k]=sticker[1][k]+max(dp[0][k-1],max(dp[1][k-2],dp[0][k-2]))
    print(max(dp[0][n-1],dp[1][n-1]))