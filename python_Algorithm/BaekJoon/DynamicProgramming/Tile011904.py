import sys
def main():
    n = int(sys.stdin.readline())
    dp = [1, 1, 2]
    for i in range(3, n + 1):
        dp.append((dp[-1] + dp[-2]) % 15746)
    print(dp[n])