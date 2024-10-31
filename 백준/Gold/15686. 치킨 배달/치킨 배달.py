"""
문제 이해
    - 입력 : 2차원 배열의 크기 N, 치킨집의 최대 개수 M
          : 2차원 배열의 마을 정수 리스트 ( 0 : 빈칸, 1: 집, 2: 치킨집)
    - 출력 : 폐업시키시 않을 치킨집을 최대 M개 골랐을 때, 도시의 치킨 거리의 최솟값
    치킨거리 = 집과 가장 가까운 치킨집과의 거리
    도시의 치킨 거리  = 모든 집의 치킨 거리의 합
    마을에 존재하는 치킨집중에 M개 만 남겨놓고 나머지 치킨집은 모두 폐업시켜야 한다.
    이때 도시의 치킨 거리의 최솟값을 구하여야 한다.
아이디어
    - 치킨집들의 좌표 리스트 생성, 집들의 좌표 리스트 생성
    - 폐업할 치킨집의 리스트들을 생성
        -> 치킨 집들의 좌표를 리스트로 받은 뒤 치킨집 수 C M (순열) 리스트 생성
        백트래킹으로 해야할 것 같음 -> 수가 정해져 있지 않기 떄문
        M개 고른 것이 아닌 치킨집들은 다 0으로 바꾸는 리스트
        추후 원상 복구
        - 리스트들을 바탕으로 치킨거리를 계산
        모든 치킨 집들과의 거리 비교 후 최솟 값이 해당 집의 치킨거리
        도시의 치킨 거리 업데이트
            - 도시의 치킨 거리 계산 - 최솟값 업데이트
"""
from itertools import combinations
def findChicken(tlst):

    # 이 좌표 치킨집 제거
    for i,j in tlst:
        data[i][j] = 0

    # 남아 있는 치킨집 리스트
    leftChi = list(sorted(set(chis) - set(tlst)))
    # 집들과 남은 치킨집들의 치킨거리 계산, 도시의 치킨 거리 계산
    ans = 0
    for hi,hj in homes:
        cRoute = float("inf")
        for ci, cj in leftChi:
            tmp = abs(hi - ci) + abs(hj- cj)
            cRoute = min(tmp, cRoute)
        ans += cRoute

    # 제거한 치킨집 원상복수
    for i,j in tlst:
        data[i][j] = 2

    # 도시의 치킨거리 리턴
    return ans

# def dfs(i, lst):
#     global ans
#     if i == leftM:
#         ans = min(ans, bfs(lst))
#         return
#
#     # 삭제할  치킨집을 고르는 경우의 수
#     for j in range(len(chis)):
#         # print(lst + [chis[j]])
#         if v[j] == 0:
#             v[j] = 1
#             dfs(i + 1, lst + [chis[j]])
#             v[j] = 0



N, M = map(int, input().split())
data = []

for _ in range(N):
    data.append(list(map(int, input().split())))

# 집들 좌표 리스트
homes = []

# 치킨집들 좌표 리스트
chis = []

ans = float("inf")

for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            homes.append((i,j))
        elif data[i][j] == 2:
            chis.append((i,j))


# 지워야 하는 치킨집 수
leftM = len(chis) - M
# v = [0] * len(chis)
# dfs(0,[]) # index, 삭제할 치킨집 리스트
ans = float("inf")
for clst in combinations(chis, leftM):
    ans = min(ans, findChicken(clst))


print(ans)

