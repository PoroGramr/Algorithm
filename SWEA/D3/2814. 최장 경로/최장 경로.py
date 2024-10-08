def dfs(l, cnt):
    global max_length
    v[l] = 1  # 방문 표시

    # 현재까지의 경로 길이를 갱신
    max_length = max(max_length, cnt)

    for a in data[l]:
        if v[a] == 0:
            dfs(a, cnt + 1)

    v[l] = 0  # 백트래킹: 다른 경로를 위해 방문 기록 초기화

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    data = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        data[a].append(b)
        data[b].append(a)

    answer = 0

    for l in range(1, N + 1):
        v = [0 for _ in range(N + 1)]
        max_length = 0  # 경로 길이 초기화
        dfs(l, 1)  # 각 정점에서 DFS 실행 (경로 길이 1로 시작)
        answer = max(answer, max_length)

    print(f"#{t} {answer}")
