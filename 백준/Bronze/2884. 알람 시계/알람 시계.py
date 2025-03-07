import sys

H,M = map(int, sys.stdin.readline().split())

minutes = H*60 + M
if minutes < 45:
    minutes += 1440
    
minutes -= 45

print(minutes//60, minutes%60)