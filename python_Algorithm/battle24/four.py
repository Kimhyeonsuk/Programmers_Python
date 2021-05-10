import heapq
def dfs(here,end,chk,cost,traps,board):
    if here==end:
        global answer
        answer=min(answer,cost)
        return
    else:
        for nextval in board[here]:
            next = nextval[0]
            cost = nextval[1]
            if (chk[here]+chk[next])%2!=nextval[2]:continue
            if next in traps:
                chk[next]+=1
                dfs(next,end,chk,cost,traps,board)
                chk[next]-=1
            else:
                if chk[next]==False:
                    chk[next]=True
                    dfs(next, end, chk, cost, traps, board)
                    chk[next]=False


def solution(n, start, end, roads, traps):
    global answer
    answer = 1e9
    board = [[] for _ in range(n + 1)]
    for road in roads:
        s = road[0]
        d = road[1]
        c = road[2]
        board[s].append((d, c,0))
        board[d].append((s,c,1))
    traps = set(traps)
    chk = [0 for _ in range(n + 1)]
    dfs(start,end,chk,0,traps,board)

    return answer