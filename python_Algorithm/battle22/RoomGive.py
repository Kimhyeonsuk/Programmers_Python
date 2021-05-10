import sys
sys.setrecursionlimit(10**6)
def findRoom(num,dic):
    if num in dic:
        val=findRoom(dic[num],dic)
        dic[num]=val+1
        return val
    else:
        dic[num]=num+1
        return num
def solution(k, room_number):
    answer = []
    dic=dict()
    s=set(room_number)
    for num in room_number:
        val=findRoom(num,dic)
        answer.append(val)
    return answer