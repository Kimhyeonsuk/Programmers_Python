from collections import defaultdict
infomap=defaultdict(list)
def permutation(cnt,sp,str):
    if cnt==4:
        global infomap
        infomap[str].append(int(sp[4]))
        return
    permutation(cnt+1,sp,str+sp[cnt])
    permutation(cnt+1,sp,str+'-')
def solution(info, query):
    answer = []
    global infomap
    for data in info:
        sp=''.join(data).split(' ')
        permutation(0,sp,'')
    for key in infomap.keys():
        infomap[key].sort()
    for data in query:
        sp=''.join(data).split(' ')
        num=int(sp[-1])
        queryStr=''
        for i in range(len(sp)-1):
            if sp[i]!='and':
                queryStr+=sp[i]

        low=0
        high=len(infomap[queryStr])-1
        while(low<=high):
            mid=int((low+high)/2)
            if infomap[queryStr][mid]<num:
                low=mid+1
            else:
                high=mid-1
        answer.append(len(infomap[queryStr])-low)

    return answer