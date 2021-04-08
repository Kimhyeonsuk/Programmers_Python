def solution(answers):
    answer = []
    score=[0,0,0]
    oneAnswer=[1,2,3,4,5]
    twoAnswer=[2,1,2,3,2,4,2,5]
    threeAnswer=[3,3,1,1,2,2,4,4,5,5]
    for i in range(0,len(answers)):
        if(oneAnswer[i%5]==answers[i]):
            score[0]+=1
        if(twoAnswer[i%8]==answers[i]):
            score[1]+=1
        if(threeAnswer[i%10]==answers[i]):
            score[2]+=1

    for idx,s in enumerate(score):
        if(s==max(score)):
            answer.append(idx+1)

    return answer