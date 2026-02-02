from collections import deque

T = int(input())

for _ in range(T):
    V,E = map(int, input().split())
    
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    color = [0] * (V + 1)
    
    is_bipartite = True
    
    for start in range(1, V + 1):
        if color[start] != 0:
            continue
    
        queue = deque()
        queue.append(start)
        color[start] = 1
        
        while queue and is_bipartite:
            cur = queue.popleft()
            
            for nxt in graph[cur]:
                if color[nxt] == 0:
                    color[nxt] = -color[cur]
                    queue.append(nxt)
                elif color[nxt] == color[cur]:
                    is_bipartite = False
                    break
        
    
        if not is_bipartite:
                break
    
    
    if is_bipartite:
        print("YES")
    else:
        print("NO")