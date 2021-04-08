def solution(n, t, m, p):
    answer = ''
    allNum='0'
    for i in range(1, t * m):
        ans = ''
        num = i
        while num > 1:
            left = num % n
            if left >= 10:
                ans = ans + (chr(ord('A')+(left-10)))
            else:
                ans=ans+str(left)
            num=int(num/n)

        if num==1:
            ans=str(num)+ans
        allNum=allNum+ans
    for i in range(0, t):
        answer+=allNum[i*m+p-1]
    return answer