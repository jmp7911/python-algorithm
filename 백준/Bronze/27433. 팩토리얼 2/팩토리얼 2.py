import sys

N = int(sys.stdin.readline())

def factorial(n):
    if n == 0:
        return 1
    elif n <= 2:
        return n
    
    arr = [0] * (n+1)
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i - 1] * i
    
    return arr[n]

print(factorial(N))