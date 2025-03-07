import sys
A=[int(sys.stdin.readline()) for _ in range(9)]
maximum = max(A)
print(maximum)
print(A.index(maximum)+1)