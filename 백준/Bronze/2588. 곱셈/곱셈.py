import sys
N = int(sys.stdin.readline())
M = sys.stdin.readline()

sum = 0
for i in range(3):
    print(int(M[2-i]) * N)
    sum += int(M[2-i]) * 10**i * N

print(sum)
    