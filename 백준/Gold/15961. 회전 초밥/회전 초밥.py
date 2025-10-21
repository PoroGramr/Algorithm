import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]

count = [0] * (d + 1)   # 각 초밥 번호의 개수
unique = 0

# 쿠폰 초밥을 미리 먹었다고 가정(중복 허용) → 항상 쿠폰 고려
count[c] += 1
unique += 1

# 초기 윈도우 [0..k-1]
for i in range(k):
    if count[belt[i]] == 0:
        unique += 1
    count[belt[i]] += 1

answer = unique

# 슬라이딩: 시작 위치 1..n-1 (원형이므로 % n)
for i in range(1, n):
    # 왼쪽 제거
    left = belt[i - 1]
    count[left] -= 1
    if count[left] == 0:
        unique -= 1

    # 오른쪽 추가
    right = belt[(i + k - 1) % n]
    if count[right] == 0:
        unique += 1
    count[right] += 1

    if unique > answer:
        answer = unique

print(answer)
