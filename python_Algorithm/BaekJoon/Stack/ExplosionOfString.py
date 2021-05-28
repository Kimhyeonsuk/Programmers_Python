def solution(s,ex):
    stack=[]
    cnt=0
    for c in s:
        if c==ex[cnt]:
            cnt += 1
            stack.append((c,cnt))

            if cnt==len(ex):
                while cnt!=0:
                    cnt-=1
                    stack.pop()
                if stack:
                    cnt=stack[-1][1]
                else:
                    cnt=0
        elif c!=ex[0]:
            cnt=0
            stack.append((c,0))
        elif c==ex[0]:
            cnt=1
            stack.append((c,1))
            if cnt==len(ex):
                while cnt!=0:
                    cnt-=1
                    stack.pop()
                if stack:
                    cnt=stack[-1][1]
                else:
                    cnt=0
    strs=''
    for c in stack:
        strs+=c[0]
    return strs
def func():
    s = input()
    ex = input()
    val = solution(s, ex)
    if val == '':
        val = 'FRULA'
    print(val)
