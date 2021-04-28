def solution(rows, columns, queries):
    answer = []
    maplist=[[i*rows+j for j in range(1,columns+1)]for i in range(rows)]
    for querie in queries:
        x1=querie[0]-1
        y1=querie[1]-1
        x2=querie[2]-1
        y2=querie[3]-1
        minNum=1e9
        val1=maplist[x1][y1]
        minNum=min(minNum,val1)
        val2=maplist[x1][y2]
        minNum = min(minNum, val2)
        val3=maplist[x2][y1]
        minNum = min(minNum, val3)
        val4=maplist[x2][y2]
        minNum = min(minNum, val4)
        for i in range(y2,y1,-1):
            maplist[x1][i]=maplist[x1][i-1]
            minNum = min(minNum, maplist[x1][i])
        for i in range(x2,x1,-1):
            maplist[i][y2]=maplist[i-1][y2]
            minNum = min(minNum, maplist[i][y2])
        for i in range(y1,y2):
            maplist[x2][i]=maplist[x2][i+1]
            minNum = min(minNum, maplist[x2][i])
        for i in range(x1,x2):
            maplist[i][y1]=maplist[i+1][y1]
            minNum = min(minNum, maplist[i][y1])
        maplist[x1][y1+1]=val1
        maplist[x1+1][y2]=val2
        maplist[x2-1][y1]=val3
        maplist[x2][y2-1]=val4
        answer.append(minNum)
    return answer