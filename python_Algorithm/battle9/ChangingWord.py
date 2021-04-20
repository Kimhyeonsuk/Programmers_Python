ans=1e9
def chkString(complist,targetlist):
    differ=0
    for c1,c2 in zip(complist,targetlist):
        if c1!=c2:
            differ+=1
    if differ>1:
        return False
    else:
        return True
def permu(beginlist,targetlist,words,removelist):
    fnd=False
    for word in words:
        if word in removelist:continue
        if chkString(beginlist,list(word)):
            fnd=True
            if word==''.join(targetlist):
                global ans
                ans=min(ans,len(removelist)+1)
            removelist.append(word)
            permu(list(word),targetlist,words,removelist)
            removelist.pop()
    if fnd==False:
        return

def solution(begin, target, words):
    answer = 0
    tmp=[12,3,4,123,3]
    tmp.remove(3)
    beginlist=list(begin)
    targetlist=list(target)
    removelist=[]
    permu(beginlist,targetlist,words,removelist)
    global ans
    if ans==1e9:
        ans=0
    return ans