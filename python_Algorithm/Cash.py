def solution(cacheSize, cities):
    answer = 0
    dic=dict()
    for idx in range(len(cities)):
        str1=cities[idx].lower()
        cities[idx]=str1
    for idx,city in enumerate(cities):
        if city not in dic:
            answer += 5
            if len(dic)<cacheSize:
                dic[city]=idx
            else:
                newlist=list(dic.items())
                newlist.sort(key=lambda x:x[1])
                if len(newlist)!=0:
                    newlist.pop(0)
                    dic=dict(newlist)
                    dic[city]=idx
        else:
            dic[city]=idx
            answer+=1
    return answer