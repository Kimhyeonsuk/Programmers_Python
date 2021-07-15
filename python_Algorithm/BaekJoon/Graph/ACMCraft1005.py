import sys
def main():
    t=int(sys.stdin.readline())
    while t!=0:
        n,k=map(int,sys.stdin.readline().split())
        buildingInfo=[[]for _ in range(n)]
        inp=[0 for _ in range(n)]
        buildingTime=list(map(int,sys.stdin.readline().split()))
        for _ in range(k):
            a,b=map(int,sys.stdin.readline().split())
            buildingInfo[a-1].append(b-1)
            inp[b-1]+=1

        w=int(sys.stdin.readline())-1
        q=[]
        maxval=[0 for _ in range(n)]
        fnd=False
        for i in range(n):
            if inp[i]==0:
                q.append(i)
                maxval[i]=buildingTime[i]
                if i==w:
                    fnd=True
        if fnd:
            print(buildingTime[w])
            t-=1
            continue
        while q:
            here=q.pop(0)
            fnd=False
            for nextNum in buildingInfo[here]:
                maxval[nextNum]=max(maxval[nextNum], buildingTime[nextNum] + maxval[here])
                inp[nextNum]-=1
                if inp[nextNum]==0:
                    q.append(nextNum)
                    if nextNum==w:
                        print(maxval[nextNum])
                        fnd=True
                        break
            if fnd:
                break
        t-=1