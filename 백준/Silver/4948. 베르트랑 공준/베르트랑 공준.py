import sys, math
input = sys.stdin.readline
while True:
    x = int(input())
    if x == 0:
        break
    prime = [True] * ((2*x) + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int(math.sqrt(2*x)) + 1):
        if prime[i]:
            for j in range(i * i, 2*x + 1, i):
                prime[j] = False
    print(len([i for i in range(x+1, 2*x+1) if prime[i]]))