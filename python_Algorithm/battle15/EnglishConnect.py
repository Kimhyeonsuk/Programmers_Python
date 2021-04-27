def solution(n, words):
    answer = [0,0]
    presentList=set()
    tmp=''
    for idx,word in enumerate(words):
        if tmp!='' and tmp[-1]!=word[0]:
            answer[0]=((idx%n) + 1)
            answer[1]=((idx//n) + 1)
            break
        elif word not in presentList:
            presentList.add(word)
            tmp=word
        else:
            answer[0] = ((idx % n) + 1)
            answer[1] = ((idx // n) + 1)
            break
    return answer