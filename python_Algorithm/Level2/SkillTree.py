from re import sub
def solution(skill, skill_trees):
    answer = 0
    for idx,skilltree in enumerate(skill_trees):
        newStr=''
        for c in skilltree:
            if c in skill:
                newStr+=c
        if ''.join(skill)[0:len(newStr)].find(newStr)!=-1 or newStr=='':
            answer+=1

    return answer