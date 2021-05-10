from collections import defaultdict
def solution(N, number):
    answer = 0
    strs=''
    dic=defaultdict(set)
    for i in range(8):
        strs+='1'
        dic[i+1].add(int(strs)*N)

    if number==N:
        return 1
    for i in range(2,9):
        for k in range(i-1,0,-1):
            for key in dic[k]:
                for key2 in dic[i-k]:
                    dic[i].add(key+key2)
                    dic[i].add(key-key2)
                    dic[i].add(key*key2)
                    if key2!=0:
                        dic[i].add(key//key2)
                    if number in dic[i]:
                        return i
    return -1