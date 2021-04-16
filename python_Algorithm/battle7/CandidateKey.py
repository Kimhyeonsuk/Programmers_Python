# def permutation(cnt,comb,relation):#조합 구하기
#     if cnt==len(relation[0]):
#         if len(comb)==0:
#             return
#         ans=True
#         chkSet=set()
#         for relationInfo in relation:
#             chkStr=''
#             for i in comb:
#                 chkStr+=relationInfo[i]
#             if chkStr in chkSet:
#                 ans=False
#                 break;
#             chkSet.add(chkStr)
#         return
#     permutation(cnt+1,comb,relation)#현재 칼럼을 선택하지 않음
#     comb.append(cnt)
#     permutation(cnt+1,comb,relation)#현재 칼럼을 선택
#     comb.pop()
ansSet=[]
def permutation(idx,cnt,comb,relation):
    if len(comb)==cnt:
        for ansEntry in ansSet:
            setList=set(ansEntry)-set(comb)
            if len(setList)==0:
                return

        ans = True
        chkSet=set()
        for relationInfo in relation:
            chkStr=''
            for i in comb:
                chkStr+=relationInfo[i]
            if chkStr in chkSet:
                ans=False
                break;
            chkSet.add(chkStr)

        if ans:
            tmplist=[num for num in comb]
            ansSet.append(tmplist)
        return
    for i in range(idx,len(relation[0])):
        comb.append(i)
        permutation(i+1,cnt,comb,relation)
        comb.pop()
def solution(relation):
    answer = 0
    colNum=len(relation[0])#column의 개수

    comb=[]
    for i in range(1,colNum+1):
        comb=[]
        permutation(0,i,comb,relation)
    #permutation(0,comb,relation)
    global ansSet
    return len(ansSet)