import sys

N = int(sys.stdin.readline())
node = list(map(int, sys.stdin.readline().split()))
graph = dict()

root = None
for i, n in enumerate(node):
    if n != -1:
        try:
            graph[n].add(i)
        except KeyError:
            graph[n] = {i}
    else:
        root = i
target = int(sys.stdin.readline())
targets = {target}

tree = [root]
leaf = []
while tree:
    parent = tree.pop()
    node = graph.get(parent)
    if node:
        if node <= targets:
            leaf.append(parent)
        elif parent not in targets:
            tree.extend(node)
        else:
            targets.add(parent)
    elif parent not in targets:
        leaf.append(parent)      
        
print(len(leaf))
