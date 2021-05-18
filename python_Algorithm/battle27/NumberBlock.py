def isPrime(num):
    sqrt=int(num**(1/2))
    for i in range(2,sqrt+1):
        if num%i==0:
            return False
    return True
def biggestDiv(num):
    standard=int(num**(1/2))
    for i in range(2,standard+1):
        if num%i==0:
            if num//i<=10000000:
                return num//i
            else:
                maxval=max(maxval,i)
    return maxval

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        if i==1:answer.append(0)
        elif isPrime(i):
            answer.append(1)
        else:
            val=biggestDiv(i)
            answer.append(biggestDiv(i))
    return answer