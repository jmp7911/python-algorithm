a = list(map(int, input().split()))
max_v = max(a)
min_v = min(a)
a.remove(max_v)
a.remove(min_v)
mid_v = a[0]


print(min_v+mid_v+min(min_v+mid_v-1, max_v))
