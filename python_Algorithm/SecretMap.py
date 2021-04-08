def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        binStr=''.join(str(bin(a|b)[2:]))
        if len(binStr)<n:
            binStr=' '*(n-len(binStr))+binStr

        binStr=binStr.replace('0',' ')
        binStr=binStr.replace('1','#')
        answer.append(binStr)
    return answer