from itertools import permutations
from itertools import combinations
def solution(number, k):
    answer = ''
    stack=[]
    for i in range(len(number)):
        while stack and k>0 and stack[-1]<number[i]:
            stack.pop()
            k-=1
        stack.append(number[i])
    answer=''.join(stack[:len(stack)-k])
    return answer