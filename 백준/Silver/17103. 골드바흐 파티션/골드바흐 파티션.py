import sys, math
N=1000000
prime = [True for i in range(N+1)]
prime[0] = False
prime[1] = False
for i in range(2, int(math.sqrt(N)) + 1):
    if prime[i]:
        for j in range(i + i, N+1, i):
            prime[j] = False
p = dict()
for i in range(N+1):
    if prime[i]:
        p[i] = True
    
T=int(input())
for _ in range(T):
    n=int(input())
    count = 0
    for x in p.keys():
        if x > n//2:
            break
        if p.get(n-x, False):
            count += 1
    print(count)