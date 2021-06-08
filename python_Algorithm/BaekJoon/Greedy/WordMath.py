def solution(n,list):
    dic = dict()
    for strs in list:
        strlen=len(strs)
        for idx,c in enumerate(strs):
            if c in dic:
                dic[c]+=pow(10,strlen-idx-1)
            else:
                dic[c]=pow(10,strlen-idx-1)
    sortedDict=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    sum=0
    for strs in list:
        strlen=len(strs)
        for idx,c in enumerate(strs):
            for num, val in enumerate(sortedDict):
                if val[0]==c:
                    sum+=(9-num)*pow(10,strlen-idx-1)
                    break
    return sum
N=int(input())
list=[]
for i in range(N):
    s=input()
    list.append(s)
res=solution(N,list)
print(res)