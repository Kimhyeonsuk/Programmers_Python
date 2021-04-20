def compare(x, y):
    first = ''.join(x[0])
    second = ''.join(y[0])
    if (first<second):
        return -1
    elif first>second:
        return 1
    else:
        fNum=int(''.join(x[1]))
        sNum=int(''.join(y[1]))
        if fNum<sNum:
            return -1
        elif fNum>sNum:
            return 1
        else:
            return -1
def solution(files):
    answer = []
    newlist=[]
    for file in files:
        split=[]
        ifNum=False
        numPart=[-1,-1]
        for idx,c in enumerate(file):
            if ord('0')<=ord(c)<=ord('9'):
                if ifNum==False:
                    ifNum=True
                    numPart[0]=idx
            else:
                if ifNum==True:
                    numPart[1]=idx
                    break
        if numPart[1]==-1:
            split.append(''.join(file[0:numPart[0]]))
            split.append(''.join(file[numPart[0]:]))
            split.append('')
        else:
            if (numPart[1]-numPart[0])>5:
                split.append(''.join(file[0:numPart[0]]))
                split.append(''.join(file[numPart[0]:numPart[0]+5]))
                split.append(''.join(file[numPart[0]+5:]))
            else:
                split.append(''.join(file[0:numPart[0]]))
                split.append(''.join(file[numPart[0]:numPart[1]]))
                split.append(''.join(file[numPart[1]:]))
        newlist.append(split)
    tmp=sorted(newlist,key=lambda x:((''.join(x[0]).lower()),int(x[1])))
    for ans in tmp:
        tmpstr=''
        for elem in ans:
            tmpstr+=elem
        answer.append(tmpstr)
    return answer