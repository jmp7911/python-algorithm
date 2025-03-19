import sys, bisect
N=int(sys.stdin.readline())
A=[sys.stdin.readline().split() for _ in range(N)]
d = dict()
for x in A:
    name, type = x
    if type == 'enter':
        d[name] = 1
    else:
        d[name] = 0
dd = sorted(d.items(), key=lambda x: x[0], reverse=True)
for key, val in dd:
    if val == 1:
        print(key)
