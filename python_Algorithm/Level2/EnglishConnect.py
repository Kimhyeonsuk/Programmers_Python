def solution(n, words):
    answer = [0,0]
    calllist=set()
    tmpword=words[0]
    calllist.add(tmpword)
    for idx,word in enumerate(words):
        if idx==0:continue
        if word in calllist or tmpword[-1]!=word[0]:
            answer[1]=int(idx/n)+1
            answer[0]=1+(idx%n)
            break
        tmpword=word
        calllist.add(word)
    return answer