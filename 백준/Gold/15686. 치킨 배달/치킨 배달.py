from itertools import combinations

def get_chicken_distance(chicken_comb):
    total_distance = 0
    for hx, hy in homes:
        min_distance = float("inf")
        for cx, cy in chicken_comb:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []

# 집과 치킨집 좌표 저장
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            homes.append((i, j))
        elif data[i][j] == 2:
            chickens.append((i, j))

# 치킨집 중 M개를 선택하는 모든 조합 생성 후 최소 치킨 거리 계산
min_city_chicken_distance = float("inf")
for chicken_comb in combinations(chickens, M):
    city_chicken_distance = get_chicken_distance(chicken_comb)
    min_city_chicken_distance = min(min_city_chicken_distance, city_chicken_distance)

print(min_city_chicken_distance)
