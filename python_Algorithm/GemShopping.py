def solution(gems):
    answer = []
    size=len(set(gems))
    dic={gems[0]:1}
    start,end=0,0

    tmp=[0,1e9]
    while start<len(gems):
        if len(dic)==size:
            gem=gems[start]
            if dic[gem]-1==0:
                if end-start<tmp[1]-tmp[0]:
                    tmp=[start+1,end+1]
                del dic[gem]
                start+=1
            else:
                dic[gem]-=1
                start+=1
        else:
            end+=1
            if end==len(gems):
                break
            if gems[end] in dic:
                dic[gems[end]]+=1
            else:

                dic[gems[end]]=1
    return tmp