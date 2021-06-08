import sys
def main():
    t=int(sys.stdin.readline())
    for i in range(t):
        n=int(sys.stdin.readline())
        arr=[]
        res=1
        for k in range(n):
            numarr=list(map(int,sys.stdin.readline().split()))
            arr.append(numarr)
        arr.sort(key=lambda x:x[0])

        minInterviewScore=arr[0][1]
        for k in range(1,len(arr)):
            iscore=arr[k][1]
            if minInterviewScore>iscore:
                res+=1
                minInterviewScore = iscore
        print(res)
