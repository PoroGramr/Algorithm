import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = [i for i in range(V + 1)]
size = [1] * (V + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path compression (halving)
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    return True

ans = 0
cnt = 0

for cost, a, b in edges:
    if union(a, b):
        ans += cost
        cnt += 1
        if cnt == V - 1:
            break

print(ans)
