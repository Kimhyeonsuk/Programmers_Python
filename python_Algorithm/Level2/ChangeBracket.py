def isRight(u):#올바른 문자열인지 확인
    stack=[]
    for idx,c in enumerate(u):
        if c == '(':
            stack.append(c)
            continue
        if c == ')' and stack and stack[-1]=='(':
            stack.pop()
        else:
            return False
    if stack:
        return False
    else:
        return True
def solve(p):
    if p=='':
        return ''
    oNum = 0
    cNum = 0
    u = ''
    v = ''
    for idx, c in enumerate(p):
        if c == '(':
            oNum += 1
        if c == ')':
            cNum += 1
        if oNum == cNum:
            u = p[:idx + 1]
            v = p[idx + 1:]
            break

    if isRight(u):
        return u+solve(v)
    else:
        tmp='('+solve(v)+')'
        u=u[1:len(u)-1]
        u=list(u)
        for idx,c in enumerate(u):
            if c==')':
                u[idx]='('
            else:
                u[idx]=')'
        return tmp+''.join(u)
def solution(p):
    answer = ''
    answer=''.join(solve(p))
    return answer