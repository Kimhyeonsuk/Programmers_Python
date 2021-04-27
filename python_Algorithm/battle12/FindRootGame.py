from collections import defaultdict
postorderlist=[]
preorderlist=[]
def preorder(idx,x,newinfo,chk):
    global preorderlist
    if(idx==len(newinfo)):
        return
    nodes=list(newinfo.values())[idx]
    size= len(nodes)
    smaller=0
    bigger=0
    for node in nodes:
        if x==-1:
            chk[node[0]]=True
            preorderlist.append(node[0])
            preorder(idx+1,node[1],newinfo,chk)
            continue
        if chk[node[0]]:continue
        if node[1]<x and smaller==0:
            chk[node[0]]=True
            preorderlist.append(node[0])
            preorder(idx+1,node[1],newinfo,chk)
            smaller+=1
        if node[1]>x and bigger==0:
            chk[node[0]]=True
            preorderlist.append(node[0])
            preorder(idx+1,node[1],newinfo,chk)
            bigger+=1
def postorder(idx,x,newinfo,chk):
    global postorderlist
    if (idx == len(newinfo)):
        return
    nodes = list(newinfo.values())[idx]
    size = len(nodes)
    smaller = 0
    bigger = 0
    for node in nodes:
        if x == -1:
            chk[node[0]] = True
            postorder(idx + 1, node[1], newinfo, chk)
            postorderlist.append(node[0])
            continue
        if chk[node[0]]: continue
        if node[1] < x and smaller == 0:
            chk[node[0]] = True
            postorder(idx + 1, node[1], newinfo, chk)
            postorderlist.append(node[0])
            smaller += 1
        if node[1] > x and bigger == 0:
            chk[node[0]] = True
            postorder(idx + 1, node[1], newinfo, chk)
            postorderlist.append(node[0])
            bigger += 1


def solution(nodeinfo):
    answer = []
    newinfo=defaultdict(list)

    for idx,info in enumerate(nodeinfo):
        x=info[0]
        y=info[1]
        num=idx+1
        newinfo[y].append((num,x))
    newinfo=dict(sorted(newinfo.items(),reverse=True))
    for key in newinfo.keys():
        newinfo[key].sort(key=lambda x:x[1])

    chk=[False]*(len(nodeinfo)+1)
    preorder(0,-1,newinfo,chk)
    chk = [False] * (len(nodeinfo) + 1)
    postorder(0,-1,newinfo,chk)

    global preorderlist
    global postorderlist
    answer.append(preorderlist)
    answer.append(postorderlist)
    return answer