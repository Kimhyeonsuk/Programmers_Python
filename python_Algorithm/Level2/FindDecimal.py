from itertools import permutations
import math
numberSet=set()
def chkDecimal(n):
    num=int(math.sqrt(n))
    if n<=1:
        return False
    for i in range(2,num+1):
        if n%i==0:
            return False
    return True
def permutation(needLen,str,chk,numbers):
    if needLen==len(str):
        num=int(str)
        if chkDecimal(num):
            global numberSet
            numberSet.add(num)

    else:
        for i in range(len(numbers)):
            if chk[i]==False:
                chk[i]=True
                permutation(needLen,str+numbers[i],chk,numbers)
                chk[i]=False


def solution(numbers):
    answer = 0
    numbers=list(numbers)

    global numberSet
    numberSet=set()
    for i in range(1,len(numbers)+1):
        chk = [False for j in range(len(numbers))]
        permutation(i,'',chk,numbers)
    return len(numberSet)