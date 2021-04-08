def solution(seoul):
    answer = ''
    for idx, name in enumerate(seoul):
        if name=='Kim':
            answer = '김서방은 ' + str(idx) + '에 있다'
    return answer