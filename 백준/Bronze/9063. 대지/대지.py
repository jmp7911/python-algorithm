#(-x, -y), (x`, y`)
#x - (-x) * y - (-y)
T=int(input())
a = [list(map(int, input().split())) for _ in range(T)]
x_min = min(row[0] for row in a)
y_min = min(row[1] for row in a)
x_max = max(row[0] for row in a)
y_max = max(row[1] for row in a)

print((x_max - x_min) * (y_max - y_min))