def solution(N, stages):
    answer = {}
    stages=list(stages)
    num=len(stages)#사람수

    for stage in range(1,N+1):
        if num!=0:
            count=stages.count(stage)
            answer[stage]=count/num
            num-=count
        else:
            answer[stage]=0
    return sorted(answer,key=lambda x:answer[x],reverse=True)