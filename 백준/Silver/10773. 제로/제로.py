import sys
input = sys.stdin.readline
N=int(input())
test_case = [int(input()) for _ in range(N)]
length = 0
sum = 0
stack = dict()
for x in test_case:
    if x != 0:
        length += 1
        stack[length] = x
        sum += x
    else:
        sum -= stack[length]
        length -= 1
print(sum)