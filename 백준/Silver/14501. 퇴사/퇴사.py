
def bfs(i,sm):
    global ans

    if i >= N:
        ans = max(ans, sm)
        return
    
    bfs(i+1, sm)
    if i + data[i][0] <= N:

        bfs(i+data[i][0], sm +data[i][1] )

N = int(input())

data = []

for _ in range(N):
    a,b = map(int, input().split())
    data.append([a,b])


ans = 0

bfs(0,0)

print(ans)