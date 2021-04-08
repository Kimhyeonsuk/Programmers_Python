def solution(s, n):
    answer = ''
    s=[c for c in s]
    for idx,c in enumerate(s):
        if ord(c)>=ord('a') and ord(c)<=ord('z'):
            num=ord(c)+n
            if num>ord('z'):
                num=ord(c)+n-26
            s[idx]=chr(num)

        elif ord(c)>=ord('A') and ord(c)<=ord('Z'):
            num=ord(c)+n
            if num>ord('Z'):
                num=ord(c)+n-26
            s[idx]=chr(num)
    answer=''.join(s)
    return answer