import sys
input = sys.stdin.readline
N=int(input())
test_case = list(map(int, input().split()))
stack = []
i = 1
flag = True
for x in test_case:
    if x == i:
        i += 1
    else:
        while len(stack) > 0:
            if stack[-1] == i:
                stack.pop()
                i += 1
            else:
                break
        if len(stack) == 0:
            stack.append(x)
        elif x > stack[-1]:
            break
        elif x < stack[-1]:
            stack.append(x)
if i > N or stack[-1] == i:
    print('Nice')
else:
    print('Sad')