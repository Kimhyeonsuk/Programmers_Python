import re
def solution(expression):
    answer = 0
    dic={'+':0,'-':0,'*':0}

    for i in range(3):
        for j in range(3):
            if i==j:continue
            for k in range(3):
                if i==k or j==k:continue
                dic['+']=i
                dic['-']=j
                dic['*']=k

                numstack=[]
                opstack=[]

                numStr=re.sub('[^0-9]',' ',expression)
                opStr=re.sub('[0-9]','',expression)
                sp=''.join(numStr).split(' ')
                oplen=len(opStr)
                for p in range(oplen):
                    numstack.append(int(sp[p]))

                    if not opstack:
                        opstack.append(opStr[p])
                    elif dic[opstack[-1]]<dic[opStr[p]]:
                        opstack.append(opStr[p])
                    else:
                        c=opStr[p]
                        while opstack and dic[opstack[-1]]>=dic[c]:
                            val2=numstack.pop()
                            val1=numstack.pop()
                            op=opstack.pop()
                            if op=='+':
                                numstack.append(val1+val2)
                            elif op=='*':
                                numstack.append(val1*val2)
                            else:
                                numstack.append(val1-val2)
                        opstack.append(c)
                numstack.append(int(sp[-1]))

                while opstack:
                    val2 = numstack.pop()
                    val1 = numstack.pop()
                    op = opstack.pop()
                    if op == '+':
                        numstack.append(val1 + val2)
                    elif op == '*':
                        numstack.append(val1 * val2)
                    else:
                        numstack.append(val1 - val2)
            answer=max(answer,abs(numstack[-1]))

    return answer