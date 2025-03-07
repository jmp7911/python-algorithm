d = dict()
d['A+']=4.5
d['A0']=4.0
d['B+']=3.5
d['B0']=3.0
d['C+']=2.5
d['C0']=2.0
d['D+']=1.5
d['D0']=1.0
d['F']=0.0

score = 0.0
hakjum = 0.0
for _ in range(20):
    a,b,c = input().split()
    if c == 'P':
        continue
    score += float(b) * d[c]
    hakjum += float(b)
print(score / hakjum)