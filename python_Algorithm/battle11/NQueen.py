ans=0
def chk(cnt,j,queenList):
    for queen in queenList:
        x=queen[0]
        y=queen[1]
        if j==y:
            return False
        if abs(cnt-x)==abs(j-y):
            return False
    return True

def dfs(chess, cnt,n,queenList):
    if cnt==n:
        global ans
        ans+=1
        return
    for j in range(n):
        if chk(cnt,j,queenList):
            queenList.append((cnt,j))
            dfs(chess,cnt+1,n,queenList)
            queenList.pop()
def solution(n):
    chess=[[0 for i in range(n)]for j in range(n)]
    queenList=[]
    dfs(chess,0,n,queenList)
    global ans
    return ans