def solution(strs):
    stack=[]
    tmpstack=[]
    for c in strs:
        if c=='<':
            if stack:
                tmpstack.append(stack.pop())
        elif c=='>':
            if tmpstack:
                stack.append(tmpstack.pop())
        elif c=='-':
            if stack:
                stack.pop()
        else:
            stack.append(c)
    while tmpstack:
        stack.append(tmpstack.pop())
    return ''.join(stack)

def main():
    T=int(input())
    for i in range(T):
        strs=input()
        val=solution(strs)
        print(val)
