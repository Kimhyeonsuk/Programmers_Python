def solution(n):
    answer = ''
    arr=[1,2,4]
    while n!=0:
        left=(n-1)%3
        answer=str(arr[left])+answer
        n=(n-1)/3
    return answer