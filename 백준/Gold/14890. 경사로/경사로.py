def can_place_ramp(road, L):
    n = len(road)
    used = [False] * n  # 경사로 설치 여부를 기록

    for i in range(n - 1):
        # 높이 차이를 확인
        if abs(road[i] - road[i + 1]) > 1:  # 높이 차이가 1 초과면 불가능
            return False

        # 오르막 경사로 설치
        if road[i] < road[i + 1]:
            height = road[i]
            for j in range(i, i - L, -1):
                if j < 0 or road[j] != height or used[j]:
                    return False
                used[j] = True

        # 내리막 경사로 설치
        elif road[i] > road[i + 1]:
            height = road[i + 1]
            for j in range(i + 1, i + 1 + L):
                if j >= n or road[j] != height or used[j]:
                    return False
                used[j] = True

    return True


N, L = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
count = 0

# 가로 길 검사
for row in data:
    if can_place_ramp(row, L):
        count += 1

# 세로 길 검사
for col in zip(*data):  # 전치 행렬을 이용
    if can_place_ramp(col, L):
        count += 1

print(count)
