from collections import defaultdict
def solution(N, number):
    answer = -1
    numberList=defaultdict(set)
    for i in range(1,9):
        nstring=int((str(N))*i)
        numberList[i].add(nstring)

    for cnt in range(1,9):
        for i in range(1,cnt):
            for num1 in numberList[i]:
                for num2 in numberList[cnt-i]:
                    numberList[cnt].add(num1+num2)
                    numberList[cnt].add(num1*num2)
                    if(num2!=0):
                        numberList[cnt].add(num1//num2)
                    numberList[cnt].add(num1-num2)
        if number in numberList[cnt]:
            answer=cnt
            break
    return answer