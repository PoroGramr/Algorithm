from collections import deque

def bfs(s,e):
    q = deque()
    v = [0 for _ in range(n+1)]
    v[s] = 1
    q.append(s)
    while q:
        fa = q.popleft()
        if fa == e:
            return v[e] - 1
        for fam in data[fa]:# 가족의 멤버
            if v[fam] == 0:
                q.append(fam)
                v[fam] = v[fa] + 1
                
    return -1
            
    

n = int(input())
s,e = map(int,input().split())

c = int(input())
data = [[] for _ in range(n+1)]



for _ in range(c):
    a,b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
answer = bfs(s,e)
print(answer)