def solution(name):
    answer = 0
    for c in name:
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
    
    return answer