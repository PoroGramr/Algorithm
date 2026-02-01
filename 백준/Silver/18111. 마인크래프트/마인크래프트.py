import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

# 높이별 개수 카운트
cnt = [0] * 257

for _ in range(N):
    row = list(map(int, input().split()))
    for h in row:
        cnt[h] += 1

best_time = float('inf')
best_height = 0

# 목표 높이 0 ~ 256 전부 검사
for target in range(257):
    time = 0
    block = B

    for h in range(257):
        if cnt[h] == 0:
            continue

        diff = h - target

        if diff > 0:
            # 제거
            time += diff * 2 * cnt[h]
            block += diff * cnt[h]
        else:
            # 쌓기
            time += (-diff) * cnt[h]
            block -= (-diff) * cnt[h]

    if block >= 0:
        if time < best_time or (time == best_time and target > best_height):
            best_time = time
            best_height = target

print(best_time, best_height)
