def solution(n):
    answer = ''
    list=['수','박']
    for i in range(n):
        answer=answer+list[i%2]
    return answer