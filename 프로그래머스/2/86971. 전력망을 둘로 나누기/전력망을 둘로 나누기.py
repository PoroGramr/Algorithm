from collections import deque

def solution(n, wires):
    gr = [[] for _ in range(n + 1)]
    
    for a,b in wires:
        gr[a].append(b)
        gr[b].append(a)
        
    answer = n 
    
    def bfs(start,cutA,cutB):
        visited = [False]*(n + 1)
        q =deque()
        q.append(start)
        cnt = 1
        visited[start] = True
        while q:
            cur = q.popleft()
            for nxt in gr[cur]:
                if (cur == cutA and nxt == cutB) or (nxt == cutA and cur == cutB):
                    continue
                
                if not visited[nxt]:
                    visited[nxt] = True
                    cnt += 1
                    q.append(nxt)
        return cnt
        
    
    for a,b in wires:
        sizeA = bfs(a,a,b)
        
        diff = abs(sizeA- (n -sizeA))
        if diff < answer:
            answer = diff
        
        
    
    return answer