import re
def solution(record):
    answer = []
    idMap={}
    for str in record:
        sp=''+str
        sp=sp.split(' ')
        if sp[0]=='Enter' or sp[0]=='Change':
            id = sp[1]
            idMap[id] = sp[2]
    for str in record:
        sp = '' + str
        sp = sp.split(' ')
        if sp[0]=='Enter':
            answer.append(idMap[sp[1]]+'님이 들어왔습니다.')
        elif sp[0]=='Leave':
            answer.append(idMap[sp[1]]+'님이 나갔습니다.')
    return answer