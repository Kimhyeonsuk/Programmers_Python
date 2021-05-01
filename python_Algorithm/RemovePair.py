def solution(s):
    answer = 0
    stack=[s[0]]
    idx=1
    while idx<len(s):
        if not stack:
            stack.append(s[idx])
        elif s[idx]==stack[-1]:
            stack.pop()
        else:
            stack.append(s[idx])
        idx+=1
    if not stack:
        answer=1
    return answer