import sys
def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i]=max(dp[i],dp[j]+1)
    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            if arr[j] < arr[i]:
                dp2[i]=max(dp2[i],dp2[j]+1)
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i] + dp2[i] + 1)
    print(ans)
main()
