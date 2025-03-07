import sys
A,B,C = map(int, sys.stdin.readline().split())

if A==B==C:
    print(10000+1000*A)
elif A!=B and B!=C and A!=C:
    print(100*max(A,B,C))
elif A==B:
    print(1000+100*A)
elif B==C:
    print(1000+100*B)
elif A==C:
    print(1000+100*A)