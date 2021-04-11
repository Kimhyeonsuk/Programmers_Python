def solution(n):
    answer = [[0 for x in range(i+1)] for i in range(n)]
    x,y=(-1,0)
    cnt=0
    num=1
    while n!=0:
        for i in range(n):
            if cnt == 0:
                x += 1
            elif cnt == 1:
                y += 1
            elif cnt == 2:
                x -= 1
                y -= 1

            answer[x][y] = num
            num += 1
        cnt = (cnt + 1) % 3
        n-=1
    res=[]
    for numllist in answer:
        for num in numllist:
            res.append(num)
    return res