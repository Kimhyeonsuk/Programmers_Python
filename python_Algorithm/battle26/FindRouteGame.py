preorder=[]
postorder=[]
def find(nodes,levels,curlevel):
    val= nodes.pop(0)
    preorder.append(val[0])
    x=val[1][0]
    y=val[1][1]
    for idx,next in enumerate(nodes):
        if next[1][1]==levels[curlevel+1]:
            find(nodes.l)

def solution(nodeinfo):
    answer = [[]]
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)
    l=list(zip(range(1,len(nodeinfo)),nodeinfo))
    l.sort(key=lambda x:(-x[1][1],x[1][0]))

    return answer