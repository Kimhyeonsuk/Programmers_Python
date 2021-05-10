
def BFS(place, x,y):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    q=[]
    chk=[[False for _ in range(5)]for _ in range(5)]
    q.append((x,y,0))
    chk[x][y]=True
    while q:
        val=q.pop(0)
        tx=val[0]
        ty=val[1]
        cnt=val[2]
        for i in range(4):
            nx=tx+dx[i]
            ny=ty+dy[i]
            if nx<0 or nx>=5 or ny<0 or ny>=5:continue
            if place[nx][ny]=='X':continue
            if chk[nx][ny]:continue
            if place[nx][ny]=='P' and cnt+1<=2:
                return False
            q.append((nx,ny,cnt+1))
            chk[nx][ny]=True

    return True

def solution(places):
    answer = []
    for place in places:
        fnd=True
        for idx,row in enumerate(place):
            for jdx,c in enumerate(row):
                if c=='P':
                    if not BFS(place,idx,jdx):
                        fnd=False
                        break
            if not fnd:
                break
        if fnd:
            answer.append(1)
        else:
            answer.append(0)
    return answer
