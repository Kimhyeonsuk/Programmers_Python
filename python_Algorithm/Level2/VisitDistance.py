from collections import defaultdict

def solution(dirs):
    answer = 0
    loc=(0,0)
    dirmap=dict()
    dirmap['U']=0
    dirmap['D']=1
    dirmap['L']=2
    dirmap['R']=3
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    mapdict = defaultdict(set)
    for dir in dirs:
        dirnum=dirmap[dir]
        nx=loc[0]+dx[dirnum]
        ny=loc[1]+dy[dirnum]

        curstr = str(loc[0]) + str(loc[1])
        nextStr=str(nx)+str(ny)
        if nx<-5 or ny<-5 or nx>5 or ny>5:continue
        if nextStr in mapdict[curstr]:
            loc=(nx,ny)
            continue
        mapdict[curstr].add(nextStr)
        mapdict[nextStr].add(curstr)
        answer+=1
        loc=(nx,ny)
    return answer