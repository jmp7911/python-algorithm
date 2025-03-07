import sys
remain = list(map(int,sys.stdin.readline().split()))
standard = [1,1,2,2,2,8]
for i in range(len(remain)):
    standard[i] -= remain[i]
print(*standard)