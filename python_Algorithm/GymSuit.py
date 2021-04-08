def solution(n, lost, reserve):
    answer = 0

    list=[0 for i in range(n+1)]
    for idx,num in enumerate(lost):
        list[num]-=1
    for num in reserve:
        list[num]+=1
    i=1
    while i!= len(list):
        if list[i]==0:
            answer+=1
        elif list[i]==1:
            answer+=1
            if list[i-1]==-1:
                list[i-1]=0
                list[i]=0
                answer+=1
            elif i+1!=len(list) and list[i+1]==-1:
                list[i+1]=0
                list[i]=0
        i+=1
    return answer