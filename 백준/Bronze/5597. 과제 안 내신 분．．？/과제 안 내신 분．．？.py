import sys
A = [i[0] for i in enumerate(range(30), 1)]
for _ in range(28):
    n = int(sys.stdin.readline())
    A.remove(n)

A.sort()
print(A[0])
print(A[1])