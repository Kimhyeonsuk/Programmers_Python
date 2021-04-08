def solution(s):
    answer = ''
    list=[]
    sp=''.join(s).split(' ')
    for word in sp:
        wordlist=[]
        for idx,c in enumerate(word):
            if idx%2==0:
                wordlist.append(''.join(c).upper())
            else:
                wordlist.append(''.join(c).lower())
        list.append(''.join(wordlist))
        list.append(' ')
    list= list[0:len(list)-1]
    return ''.join(list)