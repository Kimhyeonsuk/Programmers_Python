def gcd(a,b):
   while b!=0:
       t=a%b
       a=b
       b=t
   return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
def solution(arr):
    answer = 0
    arr.sort(reverse=True)

    while len(arr)!=1:
        val1= arr.pop()
        val2=arr.pop()
        arr.append(lcm(val2,val1))

    return arr[0]