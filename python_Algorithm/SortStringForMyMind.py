def solution(strings, n):
    answer = []
    list=[]
    for string in strings:
        list.append([string[n],string])
    list.sort()
    for child in list:
        answer.append(child[1])
    return answer