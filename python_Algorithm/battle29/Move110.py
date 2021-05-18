import re
def solution(s):
    answer = []
    for strs in s:
        strs=re.sub('110','',strs)
        idx=strs.find('11')
        if idx==-1:
            if len(strs)==1 and strs=='1':
                strs='110'+strs
            else:
                strs+='110'
        else:
            li=list(strs)
            li.insert(idx,'1')
            li.insert((idx+1),'1')
            li.insert(idx+2,'0')
            strs=''.join(li)
        answer.append(strs)
    return answer