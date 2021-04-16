def chkOneCnt(number):
    oNum=0
    while number!=0:
        left=number%2
        if left==1:
            oNum+=1
        number=int(number/2)
    return oNum
def solution(n):
    answer = 0
    oNum=0
    number=n
    while number!=0:
        left=number%2
        if left==1:
            oNum+=1
        number=int(number/2)
    nextNum=n+1
    while True:
        if chkOneCnt(nextNum)==oNum:
            answer=nextNum
            break
        nextNum+=1
    return answer