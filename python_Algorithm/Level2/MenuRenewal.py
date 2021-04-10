from itertools import combinations
def solution(orders, course):
    answer = []

    for orderNum in course:
        courseMap={}
        for order in orders:
            if orderNum>len(order):
                continue
            orderlistComb=list(combinations(sorted(order),orderNum))
            for comb in orderlistComb:
                combStr=''.join(comb)
                if combStr in courseMap:
                    courseMap[combStr]+=1
                else:
                    courseMap[combStr]=1


        if len(courseMap)==0:
            continue

        res=dict(sorted(courseMap.items(),key=lambda x:x[1],reverse=True))
        maxCnt=max(res.values())
        for key in res.keys():
            if res[key]==maxCnt and maxCnt!=1:
                answer.append(key)
    return sorted(answer)