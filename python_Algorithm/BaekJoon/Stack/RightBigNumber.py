def solution(numbers):
    stack=[]
    global answer
    for idx,num in enumerate(numbers):
        if not stack:
            stack.append((num,idx))
        else:
            while stack and stack[-1][0]<num:
                val=stack.pop()
                answer[val[1]]=num
            stack.append((num,idx))


def func():
    N=int(input())
    arr=[]
    global answer
    answer=[-1 for _ in range(N)]
    arr=list(map(int,input().split(' ')))
    solution(arr)
    for num in answer:
        print(num,end=' ')