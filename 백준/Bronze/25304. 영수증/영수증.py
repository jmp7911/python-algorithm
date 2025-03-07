import sys
receipt = int(sys.stdin.readline())
N = int(sys.stdin.readline())
sum = 0
for i in range(N):
    price,quantity = map(int,sys.stdin.readline().split())
    sum += price*quantity
    
if sum == receipt:
    print('Yes')
else:
    print('No')