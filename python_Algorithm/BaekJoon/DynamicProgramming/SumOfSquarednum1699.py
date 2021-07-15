import sys
def main():
    n=int(sys.stdin.readline())
    dp=[0 for _ in range(n+1)]
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=i
        val=int(pow(i,0.5))
        for j in range(1, val + 1):
            dp[i] = min(dp[i], dp[i - j *j] + 1)
    print(dp[n])
