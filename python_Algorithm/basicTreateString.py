def solution(s):
    answer = True
    for c in s:
        if not (ord(c)>=ord('0') and ord(c)<=ord('9')):
            answer=False
            break
    if len(s)!=4 and len(s)!=6:
        answer=False
    return answer