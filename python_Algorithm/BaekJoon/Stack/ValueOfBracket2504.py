def solution(strs):
    stack=[]
    answer=0
    fnd=True
    for c in strs:
        if c==')':
            sum=0
            while stack:
                if stack[-1]=='(':
                    stack.pop()
                    if sum==0:
                        stack.append(2)
                    else:
                        stack.append(2*sum)
                    break
                elif stack[-1]=='[':
                    return 0
                else:
                    sum+=stack.pop()
        elif c==']':

            sum=0
            while stack:
                if stack[-1]=='(':
                    return 0
                elif stack[-1]=='[':
                    stack.pop()
                    if sum == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * sum)
                    break
                else:
                    sum+=stack.pop()
        else:
            stack.append(c)
    for i in stack:
        if i=='(' or i=='[':
            return 0
        answer+=i
    return answer
# strs=input()
# print(solution(strs))

