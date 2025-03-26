import sys
input = sys.stdin.readline
N=int(input())
test_case = [int(input()) for _ in range(N)]
for x in test_case:
    if x == 0 or x == 1:
        print(2)
        continue
    y = x
    while True:
        for z in range(2, int(y**0.5)+1):
            is_prime = True
            if y % z == 0:
                is_prime = False
                break
        if is_prime:
            print(y)
            break
        y += 1