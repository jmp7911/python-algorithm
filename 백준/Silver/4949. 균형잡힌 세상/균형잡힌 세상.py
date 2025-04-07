import sys
input = sys.stdin.readline
while True:
    strings = input().rstrip()
    if strings == '.':
        break
    stack = []
    length = 0
    for s in strings:
        if s == '(':
            stack.append(0)
            length += 1
        elif s == '[':
            stack.append(1)
            length += 1
        elif s == ')':
            if length > 0 and stack[-1] == 0:
                stack.pop()
                length -= 1
            else:
                length = -1
                break
        elif s == ']':
            if length > 0 and stack[-1] == 1:
                stack.pop()
                length -= 1
            else:
                length = -1
                break
        elif s == '.':
            break
    if length == 0:
        print('yes')
    else:
        print('no')