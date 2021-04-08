week=['FRI','SAT','SUN','MON','TUE','WED','THU']
day=[31,29,31,30,31,30,31,31,30,31,30,31]
def find(m,d):
    if(m==1):
        return d
    res=0
    for i in range(0,m-1):
        res+=day[i]
    res+=d
    return res
def solution(a, b):
    answer = ''
    answer=week[(find(a,b)%7)-1]
    return answer