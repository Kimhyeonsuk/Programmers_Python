def gcd(n, m):
    while n != 0:
        tr = m % n
        m=n
        n = tr
    return m
def lcm(n, m):
    return (n * m) / gcd(n, m)


def solution(n, m):
    answer = []
    if n > m:
        n, m = m, n
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))
    return answer