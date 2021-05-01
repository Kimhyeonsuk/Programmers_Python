def solution(s):
    answer = ''
    s=''.join(s).lower()
    blank=True
    s=list(s)
    for idx,c in enumerate(s):
        if ord('a')<=ord(c)<=ord('z') and blank==True:
            s[idx]=c.upper()
            blank=False
        elif c==' ':
            blank=True
        else:
            blank=False
    return ''.join(s)