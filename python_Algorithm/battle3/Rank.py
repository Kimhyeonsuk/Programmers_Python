from collections import deque
def BFS(win,num,n):
    chk = [False for j in range(n + 1)]
    q=deque([num])
    chk[num]=True
    cnt=0
    while q:
        idx=q.popleft()
        for i in win[idx]:
            if chk[i]==False:
                chk[i]=True
                q.append(i)
                cnt+=1
    return cnt
def solution(n, results):
    answer = 0
    win=[[] for i in range(n+1)]
    defeat=[[]for i in range(n+1)]
    #트리에서 자신보다 위에있느 사람 + 자신보다 아래있는 사람 ==n-1이면 순위를 메ㅔ길수 있다.
    #win, defeat tree 초기화
    for result in results:
        win[result[0]].append(result[1])
        defeat[result[1]].append(result[0])

    for i in range(1,n+1):
        winNum=BFS(win,i,n)
        defeatNum=BFS(defeat,i,n)
        if winNum+defeatNum==n-1:
            answer+=1
    return answer