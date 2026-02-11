import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = 10**15
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dist[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c

# Floyd-Warshall
for k in range(1, N + 1):
    for i in range(1, N + 1):
        # i -> k가 불가능하면 굳이 볼 필요 없음(약간 최적화)
        if dist[i][k] == INF:
            continue
        ik = dist[i][k]
        for j in range(1, N + 1):
            if ik + dist[k][j] < dist[i][j]:
                dist[i][j] = ik + dist[k][j]

# 출력: 갈 수 없으면 0
out_lines = []
for i in range(1, N + 1):
    row = []
    for j in range(1, N + 1):
        row.append("0" if dist[i][j] == INF else str(dist[i][j]))
    out_lines.append(" ".join(row))

print("\n".join(out_lines))
