import sys
from collections import deque
A, B = map(int, sys.stdin.readline().split())
q = deque()
q.append((A, 1))
answer = -1

while q:
    n, count = q.popleft()
    if n == B:
        answer = min(answer, count) if answer > 0 else count
    elif n > B:
        continue
    
    n_1 = n * 2
    n_2 = n * 10 + 1
    if n_1 <= B:
        q.append((n_1, count + 1))
    if n_2 <= B:
        q.append((n_2, count + 1))
    
print(answer)