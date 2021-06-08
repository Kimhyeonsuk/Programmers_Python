import sys
def main():
    n = int(sys.stdin.readline())
    arr=[]
    for i in range(n):
        num=int(sys.stdin.readline())
        arr.append(num)
    arr.sort()
    for number in arr:
        print(number)
