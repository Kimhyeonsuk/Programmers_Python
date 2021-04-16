def solution(s):
    answer = True
    stack=[]
    for c in s:
        if c=='(':
            stack.append(c)
        elif c==')':
            if len(stack)==0:
                answer=False
                break
            else:
                stack.pop()
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    if len(stack)!=0:
        answer=False
    return True