import sys
import heapq
def timeToFloat(timeStr):
    sp=((str(timeStr).split('T'))[1].split('+'))[0].split(':')
    h=int(sp[0])*3600
    m=int(sp[1])*60
    s=float(sp[2])
    return h+m+s
def solution():
    n=int(input())
    A=dict()
    B=dict()
    for _ in range(n):
        a,b=map(int,input().split(','))
        A[a]=[]
        B[b]=[]
    m=int(input())
    for _ in range(m):
        logs=input().split(',')
        user_no=int(logs[5])
        log_name=logs[3]
        log_time=timeToFloat(logs[0])
        if user_no in A.keys():
            A[user_no].append((log_time,log_name))
        if user_no in B.keys():
            B[user_no].append((log_time,log_name))


