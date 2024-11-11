T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # DP 테이블 초기화 (각 원소별로 길이 최소 1)
    dp = [1] * N
    
    # LIS 길이 계산
    for i in range(1, N):
        for j in range(i):
            if arr[j] < arr[i]:  # 증가하는 관계일 경우
                dp[i] = max(dp[i], dp[j] + 1)
    
    # dp 배열에서 최댓값 찾기
    answer = max(dp)
    print(f"#{t} {answer}")
