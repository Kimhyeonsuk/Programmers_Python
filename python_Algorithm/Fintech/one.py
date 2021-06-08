def chk(number,strs):
    strsidx=0
    for c in str(number):
        if strsidx>=len(strs):
            return True
        if c==strs[strsidx]:
            strsidx+=1
    if strsidx>=len(strs):
        return True
    return False
def solution(inputString):
    answer = 0
    inputidx=0
    for i in range(0,1001):
        if 0<=i<=9:
            strs=inputString[inputidx:inputidx+1]
            if chk(i,strs):
                answer=i
                inputidx+=1
        elif 10<=i<=99:
            for k in range(2,0,-1):
                strs=inputString[inputidx:inputidx+k]
                if chk(i,strs):
                    answer=i
                    inputidx+=k
                    break
        elif 100<=i<=999:
            for k in range(3, 0, -1):
                strs = inputString[inputidx:inputidx + k]
                if chk(i, strs):
                    answer = i
                    inputidx += k
                    break
        elif i==1000:
            for k in range(4,0,-1):
                strs=inputString[inputidx:inputidx+k]
                if chk(i, strs):
                    answer = i
                    inputidx += k
                    break
        if inputidx>=len(inputString):
            break
    return answer