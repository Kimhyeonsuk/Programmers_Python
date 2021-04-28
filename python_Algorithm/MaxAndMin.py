def solution(s):
    answer = ''
    sp=''.join(s).split(' ')
    maxNum=-1e9
    minNum=1e9
    for num in sp:
        intnum=int(num)
        maxNum=max(maxNum,intnum)
        minNum=min(minNum,intnum)
    return str(minNum)+' '+str(maxNum)