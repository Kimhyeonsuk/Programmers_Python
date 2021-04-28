def solution(rows, columns, queries):
    maplist = [[j+i*columns for j in range(1,columns+1)]for i in range(rows)]
    answer=[]

    # maplist = [[] for _ in range(rows)]
    # for i in range(1, rows + 1):
    #     for j in range(1, columns + 1):
    #         maplist[i - 1].append((i - 1) * columns + j)
    for querie in queries:
        x1=querie[0]-1
        y1=querie[1]-1
        x2=querie[2]-1
        y2=querie[3]-1
        tmplist=[]
        for i in range(x1,x2):
            tmplist.append(maplist[i][y1])
        for i in range(y1,y2):
            tmplist.append(maplist[x2][i])
        for i in range(x2,x1,-1):
            tmplist.append(maplist[i][y2])
        for i in range(y2,y1,-1):
            tmplist.append(maplist[x1][i])
        val=tmplist.pop(0)
        tmplist.append(val)
        minval=min(tmplist)
        answer.append(minval)
        for i in range(x1,x2):
            maplist[i][y1]=tmplist.pop(0)
        for i in range(y1,y2):
            maplist[x2][i]=tmplist.pop(0)
        for i in range(x2,x1,-1):
            maplist[i][y2]=tmplist.pop(0)
        for i in range(y2,y1,-1):
            maplist[x1][i]=tmplist.pop(0)
    return answer