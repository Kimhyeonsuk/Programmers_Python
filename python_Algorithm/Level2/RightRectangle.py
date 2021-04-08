import math
def solution(w,h):
    answer = 1
    if w>h:
        w,h=h,w
    return w*h-(w+h-math.gcd(w,h))