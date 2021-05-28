def solution(N,li):
    stack=[]
    answer=[0 for _ in range(N)]
    for idx,num in enumerate(li):
        while stack and stack[-1][0] < num:
            stack.pop()
        if stack:
            answer[idx] = stack[-1][1]
        stack.append((num, idx + 1))
    return answer
#
# N = int(input())
# li = list(map(int, input().split()))
# ans = solution(N, li)
# print(" ".join(map(str,ans)))
