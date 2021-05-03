from collections import defaultdict
def dfs(crewname,money,tree,add):
    if len(tree[crewname])!=0:
        val=money//10
        add[crewname]+=money-val
        dfs(tree[crewname][0],val,tree,add)
def solution(enroll, referral, seller, amount):
    answer = []
    tree=defaultdict(list)
    money=defaultdict(list)
    inp=defaultdict(int)
    add=defaultdict(int)
    for a,b in zip(enroll,referral):
        tree[a].append(b)
        inp[b]+=1
    for a,b in zip(seller,amount):
        money[a].append(b*100)
    q=[]
    for k in enroll:
        if inp[k]==0:
            q.append(k)
    while q:
        crewName=q.pop(0)
        while money[crewName]:
            value=money[crewName].pop()
            dfs(crewName,value,tree,add)
        if len(tree[crewName])!=0:
            inp[tree[crewName][0]] -= 1
            if inp[tree[crewName][0]] == 0:
                q.append(tree[crewName][0])
    for a in enroll:
        answer.append(add[a])
    return answer