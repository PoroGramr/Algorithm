
# Online Python - IDE, Editor, Compiler, Interpreter

N, M = map(int, input().split())

visited = [False] * (N + 1)
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs()
            result.pop()
            visited[i] = False

dfs()