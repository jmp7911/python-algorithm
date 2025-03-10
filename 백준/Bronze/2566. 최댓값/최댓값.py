maximum = 0
max_index = (1, 1)
for i in enumerate(range(9), 1):
    line = list(map(int, input().split()))
    if maximum < max(line):
        max_index = (i[0], line.index(max(line))+1)
        maximum = max(line)
print(maximum)
print(max_index[0], max_index[1])