from collections import defaultdict
def solution(n):
    answer = 0
    dp=defaultdict(set)
    dp[1].add('()')
    dp[2].add('(())')
    dp[2].add('()()')
    for i in range(3,n+1):
        for first in range(1,i):
            for firstval in dp[first]:
                for secondval in dp[i-first]:
                    dp[i].add(firstval+secondval)
                    if first==1:
                        dp[i].add('('+secondval+')')
    return len(dp[n])