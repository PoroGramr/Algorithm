T = int(input())
for t in range(1, T + 1):
    N, L = map(int, input().split())

    data = []
    for _ in range(N):
        # 맛, 칼로리
        s, c = map(int, input().split())
        data.append((s,c))
    # dp[i][j]  => 인덱스 i시에 칼로리 제한 j일 경우 최대값     
    dp = [[0] * (L + 1) for _ in range(N + 1)]
    
    # 음식 인덱스
    for i in range(1,N + 1):
        
        # 칼로리
        for j in range(1,L + 1):
            if data[i-1][1] <= j:
                # 이전 요소 그대로 가져오거나, dp[이전요소 - 현재 인덱스 무게][] + 현재 요소 점수
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-data[i-1][1]] + data[i-1][0])
            else:
                dp[i][j] = dp[i-1][j]

    print(f"#{t} {dp[N][L]}")
