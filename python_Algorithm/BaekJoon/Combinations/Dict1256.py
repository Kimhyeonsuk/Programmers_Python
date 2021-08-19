import sys
def main():
    n,m,k=map(int,sys.stdin.read().split(' '))
    dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j]=1
    dp[0][0]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j]=dp[i-1][j]+dp[i][j-1];
            if(dp[i][j]>1000000000):
                dp[i][j]=1000000000
    acnt=n
    zcnt=m
    if(dp[n][m]<k):
        print(-1)
        return
    for i in range(n+m):
        prea=dp[acnt-1][zcnt]#a로 시작하는 개수
        if acnt==0:
            zcnt-=1
            print('z',end='')
            continue
        elif zcnt==0:
            acnt-=1
            print('a',end='')
            continue
        if(k<=prea):
            acnt-=1
            print('a',end='')
        else:
            k=k-prea
            zcnt-=1
            print('z',end='')
    print('')
    return