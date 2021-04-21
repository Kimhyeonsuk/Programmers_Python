from collections import defaultdict
def solution(genres, plays):
    answer = []
    musicDict=defaultdict(list)
    for i in range(len(genres)):
        musicDict[genres[i]].append((i,plays[i]))

    #musicDict.items().sort(key=lambda x: len(musicDict[x]))
    tmplist=[(1,200),(2,300),(4,100)]
    a=sum(pair[1] for pair in tmplist)
    newDict=dict(sorted(musicDict.items(),key=lambda x:sum(pair[1] for pair in x[1]),reverse=True))
    for key in newDict.keys():
        newDict[key].sort(key=lambda x:x[1],reverse=True)
        answer.append(newDict[key][0][0])
        if len(newDict[key])!=1:
            answer.append(newDict[key][1][0])
    return answer