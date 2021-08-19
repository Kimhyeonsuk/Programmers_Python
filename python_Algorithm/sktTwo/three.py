import sys
def solution(N,A,B):
    A=list(A)
    B=list(B)
    board=dict()
    chk=[False for _ in range(N+1)]
    listLen=len(A)
    for a,b in zip(A,B):
        if a in board.keys():
            board[a].add(b)
        else:
            board[a]={b}
        if b in board.keys():
            board[b].add(a)
        else:
            board[b]={a}
    board=list(board.items())
    board.sort(key=lambda x:len(x[1]),reverse=True)
    verticeValue=[0 for _ in range(N+1)]
    for item in board:
        key=item[0]
        child=item[1]
        if chk[key]==False:
            chk[key]=True
            verticeValue[key]=N
            N-=1
        for childItem in child:
            if chk[childItem] == False:
                chk[childItem]=True
                verticeValue[childItem] = N
                N -= 1
                chk[childItem] = True

    res=0
    for a,b in zip(A,B):
        res+=verticeValue[a]+verticeValue[b]
    return res
def main():
    solution(5,[2,2,1,2],[1,3,4,4])
    #solution(4,[1,3],[2,4])
