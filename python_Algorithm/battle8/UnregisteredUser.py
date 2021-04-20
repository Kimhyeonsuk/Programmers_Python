from collections import defaultdict
idMap=defaultdict(list)
def permuation(cnt,userId,createdId):
    if cnt==len(userId):
        global idMap
        idMap[createdId].append(userId)
        return
    permuation(cnt+1,userId,createdId+userId[cnt])
    permuation(cnt+1,userId,createdId+'*')
ansSet=[]
def casePermu(cnt,caselist,caseSet):
    if cnt==len(caselist):
        global ansSet
        newSet=set(caseSet)
        chk=True
        for ans in ansSet:
            if len(newSet-set(ans))==0:
                chk=False
                break
        if chk:
            ansSet.append(newSet)
        return
    for case in caselist[cnt]:
        if case in caseSet: continue
        caseSet.append(case)
        casePermu(cnt + 1, caselist, caseSet)
        caseSet.pop()
def solution(user_id, banned_id):
    answer = 1
    global idMap
    for userId in user_id:
        permuation(0,userId,'')
    tmp=1
    caselist=[]
    for bannedId in banned_id:
        caselist.append(idMap[bannedId])
    caseSet=[]
    casePermu(0,caselist,caseSet)
    global ansSet

    return len(ansSet)