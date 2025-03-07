import sys
A = set()
for _ in range(10):
    n = int(sys.stdin.readline())
    A.add(n%42)
print(len(A))
