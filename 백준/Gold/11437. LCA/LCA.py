import sys
sys.setrecursionlimit(100000)

n = int(input())
tree = [[]for _ in range(n + 1)]
depth = [0] * (n + 1)
parent = [0] * (n + 1)
visited = [False] * (n + 1)

for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def dfs(x, d):
    visited[x] = True
    depth[x] = d

    for node in tree[x]:
        if visited[node]:
            continue
        parent[node] = x
        dfs(node, d + 1)

def lca(a,b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

dfs(1,0)
# print(tree)
# print(parent)

m = int(input())
for _ in range(m):
    a, b= map(int, input().split())
    print(lca(a,b))


