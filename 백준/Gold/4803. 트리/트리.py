from collections import deque
import sys

input = sys.stdin.readline

caseNum = 1
while True:
    
    n,m = map(int, input().split())
    
    if n == m == 0:
        break
    
    graph = [[] for _ in range((n + 1))]
    

    for _ in range(m):
        a,b = map(int, input().split())
        
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False for _ in range(n + 1)] 
    
    q = deque()
    
    cnt = 0
    
    for i in range(1, n + 1):
        if visited[i] == False:
            q.append((i,0))
            visited[i] = True
            
            isTree = True
            
            while q:
                crt, parent = q.popleft()
                
                
                for nxt in graph[crt]:
                    if visited[nxt] == False:
                        q.append((nxt,crt))
                        visited[nxt] = True
                    else:
                        if nxt != parent:
                            isTree = False
            if isTree:
                cnt += 1



    if cnt == 0:
        print(f"Case {caseNum}: No trees.")
    elif cnt == 1:
        print(f"Case {caseNum}: There is one tree.")
    else:
        print(f"Case {caseNum}: A forest of {cnt} trees.")
    
    caseNum += 1