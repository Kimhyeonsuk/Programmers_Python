from collections import defaultdict
import re
global cursobi
def permutation(n,pnum,dic,makedList,limit):
    if n== len(makedList):
        global answer
        global cursobi
        time=0
        space=0
        for datainfo in makedList:
            time+=int(datainfo[3])
            space+=int(datainfo[4])
        if (time<=limit[0] and space<=limit[1]) or (limit[0]==0 and space<=limit[1]) or (time<=limit[0] and limit[1]==0) or (limit[0]==0 and limit[1]==0 ):
            if time+space<cursobi:
                cursobi=time+space
                tmplist=[]
                for datainfo in makedList:
                    strs=datainfo[0]+str(datainfo[1])
                    tmplist.append(strs)
                answer=tmplist
        return
    if pnum in dic:
        for datainfo in dic[pnum]:
            makedList.append(datainfo)
            permutation(n, pnum + 1, dic, makedList, limit)
            makedList.pop()

def solution(n, data, limit):
    global answer
    global cursobi
    cursobi=1e9
    answer = []
    #n 몇개의 문제를 풀어야하는지
    #data 알고리즘 정보 [알고리즘이름, 해결문제번호, 필요한 시간, 필요한 공간]
    #총 시간과 저장 공간의 정보
    #판단기준: 알고리즘이 조합이 소모한 시간, 저장 공간의 합계 작을수록 좋음
    #조합 -> 제한된 공간,시간 확인 ->  최소값 확인
    dic=dict()
    customData=[]
    for datastr in data:
        datainfo=''.join(datastr).split(' ')
        name=re.sub('[0-9]','',''.join(datainfo[0]))
        number=int(re.sub('[^0-9]','',''.join(datainfo[0])))
        pnum=int(datainfo[1])
        time=int(datainfo[2])
        space=int(datainfo[3])
        customData.append([name,number,pnum,time,space])
    for datainfo in customData:
        if datainfo[2] in dic:
            dic[datainfo[2]].append(datainfo)
        else:
            dic[datainfo[2]]=[datainfo]
    for num in range(1,n+1):
        if num in dic:
            dic[num].sort(key=lambda x:(-x[1],x[0]))
    makedList=[]
    limit=list(map(int,limit.split(' ')))
    permutation(n,1,dic,makedList,limit)
    return answer