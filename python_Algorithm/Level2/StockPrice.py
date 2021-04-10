def solution(prices):
    answer = [0]*len(prices)
    stack=[]
    for i,price in enumerate(prices):
        while stack and price<prices[stack[-1]]:
            j=stack.pop()
            answer[j]=i-j
        stack.append(i)

    l=len(prices)
    while stack:
        j=stack.pop()
        answer[j]=l-1-j
    return answer