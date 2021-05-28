import re
global stack
global opstack
def cal(isClose):
    global stack
    global opstack
    while opstack and opstack[-1] != '(':
        val1 = stack.pop()
        val2 = stack.pop()
        op = opstack.pop()
        if op == '+' :
            stack.append(val2 + val1 + '+')
        elif op == '-' :
            stack.append(val2 + val1 + '-')
        elif op == '*' :
            stack.append(val2 + val1 + '*')
        elif op == '/' :
            stack.append(val2 + val1 + '/')
    if isClose:
        opstack.pop()
def cal2():
    global stack
    global opstack
    while opstack and  opstack[-1] != '(':
        if opstack[-1]=='*' or opstack[-1]=='/':
            val1 = stack.pop()
            val2 = stack.pop()
            op = opstack.pop()
            if op == '*':
                stack.append(val2 + val1 + '*')
            elif op == '/':
                stack.append(val2 + val1 + '/')
        else:
            break
def solution(strs):
    global stack
    global opstack
    stack = []
    opstack = []
    for c in strs:
        if c==')':
            cal(True)
        elif c=='(':
            opstack.append(c)
        elif c=='+' or c=='-':
            cal(False)
            opstack.append(c)
        elif c=='*' or c=='/':
            cal2()
            opstack.append(c)
        else:
            stack.append(c)
    cal(False)
    return stack[0]
# strs=input().replace('\n','')
# val=solution(strs)
# print(val)
# def main():
#     print(1)


# import re
# def solution(strs):
#     stack = []
#     opstack = []
#     for c in strs:
#         if c == ')':
#             if not opstack:
#                 val = stack.pop()
#                 stack.pop()
#                 stack.append(val)
#             else:
#                 val1 = stack.pop()
#                 val2 = stack.pop()
#                 if val2=='(':
#                     stack.append(val1)
#                     continue
#                 stack.pop()
#                 op = opstack.pop()
#                 stack.append(val2 + val1 + op)
#         elif c == '+' or c == '-':
#             while opstack:
#                 if stack[-2]=='(':
#                     break
#                 val1=stack.pop()
#                 val2=stack.pop()
#                 op=opstack.pop()
#                 stack.append(val2+val1+op)
#             opstack.append(c)
#         elif c == '*' or c == '/':
#             while opstack:
#                 if stack[-2]=='(':
#                     break
#                 if opstack[-1]=='-' or opstack[-1]=='+':
#                     break
#                 val1=stack.pop()
#                 val2=stack.pop()
#                 op=opstack.pop()
#                 stack.append(val2+val1+op)
#             opstack.append(c)
#         else:
#             stack.append(c)
#     while opstack:
#         val1 = stack.pop()
#         val2 = stack.pop()
#         op = opstack.pop()
#         stack.append(val2 + val1 + op)
#     return ''.join(stack)
# strs=input()
# print(solution(strs))
