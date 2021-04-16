from collections import defaultdict
answer=1e9
def cal(r,c,one,two):
    sum=0
    if r==one[0] and c==one[1]:
        sum+=1
    elif r==one[0]or c==one[1]:
        sum+=2
    else:
        sum+=3
    r=one[0]
    c=one[1]
    if r==two[0] and c==two[1]:
        sum+=1
    elif r==two[0]or c==two[1]:
        sum+=2
    else:
        sum+=3
    return sum

def calMinMove(cnt,r,c,newlist,charDict,sum):
    if cnt==len(newlist):
        return sum
    else:
        return min(
            calMinMove(cnt+1,charDict[newlist[cnt]][1][0],charDict[newlist[cnt]][1][1],newlist,charDict,sum+cal(r,c,charDict[newlist[cnt]][0],charDict[newlist[cnt]][1]))
            ,calMinMove(cnt+1,charDict[newlist[cnt]][0][0],charDict[newlist[cnt]][0][1],newlist,charDict,sum+cal(r,c,charDict[newlist[cnt]][1],charDict[newlist[cnt]][0]))
        )
def permu(cnt,charlist,newlist,charChk,r,c,charDict):
    if cnt== len(charlist):
        global answer
        ans=calMinMove(0,r,c,newlist,charDict,0)
        answer=min(answer,ans)
        return
    for charNum in charlist:
        if charChk[charNum]:continue
        charChk[charNum]=True
        newlist.append(charNum)
        permu(cnt+1,charlist,newlist,charChk,r,c,charDict)
        charChk[charNum]=False
        newlist.pop()


def solution(board, r, c):
    charDict=defaultdict(list)
    charlist=set()
    for i,row in enumerate(board):
        for j ,col in enumerate(row):
            if col!=0:
                charDict[col].append([i,j])
                charlist.add(col)
    charlist=list(charlist)

    charChk=defaultdict(bool)
    newlist=[]
    permu(0,charlist,newlist,charChk,r,c,charDict)
    global answer
    return answer