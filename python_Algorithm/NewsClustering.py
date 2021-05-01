import re
from collections import defaultdict
def solution(str1, str2):
    answer = 0
    list1=defaultdict(int)
    list2=defaultdict(int)
    for i in range(len(str1)-1):
        word=re.sub('[^a-z]','',''.join(str1[i:i+2]).lower())
        if len(word)==2:
            list1[word]+=1
    for i in range(len(str2)-1):
        word=re.sub('[^a-z]','',''.join(str2[i:i+2]).lower())
        if len(word)==2:
            list2[word]+=1

    inter=0
    prod=0

    for k,v in list1.items():
        if k in list2:
            if list1[k]<list2[k]:
                inter+=list1[k]
                prod+=list2[k]
            else:
                inter+=list2[k]
                prod+=list1[k]
        if k not in list2:
            prod+=list1[k]
    for k,v in list2.items():
        if k not in list1:
            prod+=v
    if prod==0:
        answer=65536
    else:
        answer=(inter*65536)//prod
    return answer