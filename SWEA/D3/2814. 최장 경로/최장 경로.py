def dfs(l, length):
    global maxLen
    v[l] = 1  # 현재 노드를 방문했다고 표시

    maxLen = max(maxLen, length)  # 현재까지 탐색한 경로의 길이를 갱신

    for a in data[l]:  # 현재 노드에서 연결된 모든 노드를 탐색
        if v[a] == 0:  # 아직 방문하지 않은 노드일 경우
            dfs(a, length + 1)  # 해당 노드를 탐색

    v[l] = 0  # 탐색이 끝났으면, 현재 노드를 다시 방문하지 않도록 초기화 (백트래킹)

T = int(input())  # 테스트 케이스 수

for t in range(1, T + 1):
    N, M = map(int, input().split())  # 노드 수(N), 간선 수(M)

    if N == 1:  # 노드가 하나만 있으면, 길이는 1
        print(f"#{t} 1")
    else:
        # 연결 정보를 저장할 리스트 생성
        data = [[] for _ in range(N + 1)]  # 1-based index
        for _ in range(M):
            s, e = map(int, input().split())
            data[s].append(e)
            data[e].append(s)

        ans = 0  # 최장 경로의 길이를 저장할 변수

        # 각 노드에서 DFS를 시작
        for i in range(1, N + 1):
            v = [0] * (N + 1)  # 방문 여부를 체크하는 리스트
            maxLen = 0  # 각 시작점에서의 최장 경로 길이
            dfs(i, 1)  # dfs 시작 (길이는 1부터 시작)
            ans = max(ans, maxLen)  # 최장 경로 길이 갱신

        print(f"#{t} {ans}")
