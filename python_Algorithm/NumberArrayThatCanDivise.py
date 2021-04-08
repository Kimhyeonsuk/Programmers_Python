def solution(arr, divisor):
    answer = []
    for num in arr:
        if(num%divisor==0):
            answer.append(num)
    answer.sort()
    a=0
    if not answer:
        a=answer[-1]
    return answer