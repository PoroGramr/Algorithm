T = int(input())

for t in range(1, T + 1):
    # N: 아이템 수, K: 배낭의 최대 무게
    N, K = map(int, input().split())
    items = []

    # 각 아이템의 무게와 가치를 입력받기
    for _ in range(N):
        weight, value = map(int, input().split())
        items.append((weight, value))

    # DP 배열 초기화
    dp = [0] * (K + 1)

    # 각 아이템에 대해 DP 갱신
    for weight, value in items:
        # 무게 제한을 초과하지 않도록 역순으로 DP 업데이트
        for w in range(K, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    # 배낭에 담을 수 있는 최대 가치 출력
    print(f"#{t} {dp[K]}")
