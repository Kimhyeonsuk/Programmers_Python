def permutation(cnt,map,strList,resStr):
    if cnt==4:
        score = int(strList[4])
        map[resStr]=score
    else:
        permutation(cnt+1,map,strList,resStr+'-')
        permutation(cnt+1,map,strList,resStr+strList[cnt])
def solution(info, query):
    answer = [0 for i in range(len(query))]
    updateQueryList=[]
    for queryStr in query:
        sp=''.join(queryStr).split(' ')
        resStr=''
        cnt=0
        score=0
        for s in sp:
            if(s!='and'):
                cnt+=1
                if cnt==5:
                    score=int(s)
                else:
                    resStr += s
        updateQueryList.append([resStr,score])


    for infoStr in info:
        map = {}
        infoStr=''.join(infoStr)
        sp=infoStr.split(' ')
        permutation(0,map,sp,'')
        for idx, queryStr in enumerate(updateQueryList):
            if queryStr[0] in map:
                if map[queryStr[0]]>=queryStr[1]:
                    answer[idx]+=1
    return answer