import sys
def chk(board,i,j):
    chklist=[False for _ in range(len(board))]
    q=[i]
    while q:
        here=q.pop(0)
        for adjidx in board[here]:
            if chklist[adjidx]==False:
                if adjidx==j:
                    return True
                chklist[adjidx]=True
                q.append(adjidx)
    return False

def main():
    n=int(sys.stdin.readline())
    board=[[]for _ in range(n)]
    for i in range(n):
        row=list(map(int,sys.stdin.readline().split()))
        for idx,next in enumerate(row):
            if next==1:
                board[i].append(idx)

    for i in range(n):
        for j in range(n):
            if chk(board,i,j):
                print('1',end='')
            else:
                print('0',end='')
            if j==n-1:
                print('')
            else:
                print(' ',end='')