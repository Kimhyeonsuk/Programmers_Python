def solution(dartResult):
    answer = 0
    list=[]
    num=0
    idx=0
    while idx!=len(dartResult):
        if ord(dartResult[idx]) >= ord('0') and ord(dartResult[idx]) <= ord('9'):
            if ord(dartResult[idx + 1]) == ord('0'):
                num=10
                idx+=1
            else:
                num=int(dartResult[idx])
            list.append(num)
        elif dartResult[idx]=='#':
            list[-1]=list[-1]*-1
        elif dartResult[idx]=='*':
            if len(list)==3:
                list[1]=list[1]*2
                list[2]=list[2]*2
            else:
                for i in range(len(list)):
                    list[i] = list[i] * 2
        elif dartResult[idx]=='S':
            list[-1]=num
        elif dartResult[idx]=='D':
            list[-1]=num*num
        elif dartResult[idx]=='T':
            list[-1]=num*num*num

        idx += 1

    return sum(list)