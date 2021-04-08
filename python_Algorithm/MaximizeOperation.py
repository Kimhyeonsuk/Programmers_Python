from collections import deque
ops=['*','+','-']
res=0;
def permutation(idx,cnt,list,expression):
    if(len(list)==cnt):
        dic={ops[i]:list[i] for i in len(list)}
        numtmp=""+expression
        numtmp.replace('[^0-9]'," ")
        numsplit=deque([int(n) for n in numtmp.split(" ")])
        optmp=""+expression
        oplist=deque([k for k in optmp.replace('[0-9]','')])
        numst=[]
        opst=[]
        while oplist:
            op=oplist.popleft()
            if(opst):
                opst.append(op)
                numst.append(numsplit.popleft())
                numst.append(numsplit.popleft())
            else:
                while not opst.isEmpty() and dic[opst[-1]]<=dic[op]:
                    newop=opst.pop()
                    if(newop=='*'):

                    elif(newop=='+'):
                    elif(newop=='-'):
    else:
        for i in range(idx,3):
            list.append(i)
            permutation(i+1,cnt,list)
            list.pop(i)


def solution(expression):
    answer = 0
    list=[]
    permutation(0,list,expression)
    return answer
