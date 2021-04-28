def solution(n):
    answer = []
    board=[[0 for _ in range(i)]for i in range(1,n+1)]

    cnt=0
    val=0
    x,y=-1,0
    while n!=0:
        if cnt%3==0:
            for i in range(n):
                x=x+1
                val += 1
                board[x][y]=val
        elif cnt%3==1:
            for i in range(n):
                y=y+1
                val+=1
                board[x][y]=val
        elif cnt%3==2:
            for i in range(n):
                x=x-1
                y=y-1
                val+=1
                board[x][y]=val
        cnt+=1
        n-=1
    for boardlist in board:
        for num in boardlist:
            answer.append(num)
    return answer