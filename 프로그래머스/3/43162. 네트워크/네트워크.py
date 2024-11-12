from collections import deque

def bfs(i, computers):
    global v
    q = deque()
    q.append(computers[i])
    v[i] = 1
    
    while q:
        c = q.popleft()
        
        for n in range(len(c)):
            if c[n] == 1:
                if v[n] == 0:
                    v[n] = 1
                    q.append(computers[n])
        

def solution(n, computers):
    global v
    answer = 0
    v = [0] * n
    
    for i in range(n):
        if v[i] == 0:
            bfs(i, computers)
            answer += 1
    return answer
    