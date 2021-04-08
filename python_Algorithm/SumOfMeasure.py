def solution(n):
    answer = 0
    list=[]
    for i in range(1,int(n/2)+1):
        if n%i==0:
            list.append(i)
            list.append(n/i)
    if n==1:
        list.append(1)
    numset=set(list)

    return sum(numset)