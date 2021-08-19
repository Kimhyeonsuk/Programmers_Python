import sys
# def main():
#     n=int(sys.stdin.readline())
#     m=int(sys.stdin.readline())
#     board=[[] for _ in range(n+1)]
#     for j in range(n):
#         arr=list(map(int,sys.stdin.readline().split()))
#         for idx,num in enumerate(arr):
#             if num==1:
#                 board[j+1].append(idx+1)
#     cities=list(map(int,sys.stdin.readline().split()))
#
#     s=cities[0]
#     q=[s]
#     chk=[False for _ in range(n+1)]
#     chk[s]=True
#     while q:
#         here=q.pop(0)
#         for next in board[here]:
#             if chk[next]==False:
#                 chk[next]=True
#                 q.append(next)
#     for city in cities:
#         if chk[city]==False:
#             print('NO')
#             return
#     print('YES')
#     return
def main():
    arr=[[0]*10]*10
    arr2=[[0 for _ in range(10)]for i in range(10)]
    for i in range(len(arr)):
        arr[i][0]=1
        arr2[i][0]=1
        arr[i][i]=1