import sys
def main():
    s1 = sys.stdin.readline().replace('\n','')
    s2 = sys.stdin.readline().replace('\n','')
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        c = s1[i - 1]
        for j in range(1, m + 1):
            if s2[j - 1] == c:
                dp[i][j] = dp[i - 1][j - 1]+1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[n][m])


