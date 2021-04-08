import collections
def solution(priorities, location):
    answer = 0
    printer=collections.deque([[prior,idx] for idx,prior in enumerate(priorities)])
    cnt=1
    while(True):
        if (max(printer,key=lambda x:x[0]))[0]>printer[0][0]:
            printer.append(printer.popleft())
        else:
            if (printer.popleft())[1]==location:
                answer=cnt
                break;
            cnt+=1
    return answer