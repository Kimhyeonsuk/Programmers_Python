def solution(phone_number):
    return ''.join(['*'for i in range(len(phone_number)-4)])+''.join(phone_number[-4:])