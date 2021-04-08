def solution(n):
    answer = 0

    ansStr=''
    while n>=3:
        left=n%3
        ansStr=str(left)+ansStr
        n=int(n/3)
    ansStr=str(n)+ansStr

    numlist= [x for x in str(int(''.join(reversed(ansStr)))) ]

    for idx,num in enumerate(numlist):
        answer+= int(num)* pow(3,len(numlist)-idx-1)
    return answer