import sys,math
input = sys.stdin.readline
N=int(input())
tree = {}
for i in range(N):
    x = int(input())
    tree[x] = 1
    if i == 0:
        a1 = x
    elif i == N-1:
        a2 = x
    
tree_keys = list(tree.keys())
gcd_dist = math.gcd(*map(lambda x,y: y-x, tree_keys[:-1], tree_keys[1:]))
    
new_tree_count = (a2 - a1) // gcd_dist + 1
    
print(new_tree_count - N)