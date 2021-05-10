# def solution(s):
#     answer = 0
#     strlen=len(s)
#     for end in range(strlen-1,-1,-1):
#         if answer>end+1:
#             break
#         anslen=0
#         cnt=0
#         start=0
#         while(True):
#             if start<end-cnt and s[start]==s[end-cnt]:
#                 anslen+=2
#                 cnt+=1
#             elif start==end-cnt and s[start]==s[end-cnt]:
#                 anslen+=1
#                 break
#             elif start>end-cnt:
#                 break
#             else:
#                 anslen=0
#                 start -= cnt
#                 cnt=0
#             start+=1
#
#         answer=max(answer,anslen)
#     return answer

def solution(s):
    answer = 1

    for i in range(len(s)):
        index = 1
        oddvalue = 1
        evenvalue = 0
        if s[i] == s[i + 1]:
            evenvalue += 2
            while index <= i <= len(s) - 2 - index:
                if s[i - index] == s[i + 1 + index]:
                    index += 1
                    evenvalue += 2
                else:
                    break

        while index <= i <= len(s) - 1 - index:
            if s[i - index] == s[i + index]:
                index += 1
                oddvalue += 2
            else:
                break

        value = max(oddvalue, evenvalue)
        answer = max(value, answer)

    return answer