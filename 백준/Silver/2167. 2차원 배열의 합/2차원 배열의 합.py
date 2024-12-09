# 입력 받기
n, m = map(int, input().split())  # n: 행의 개수, m: 열의 개수
array = [list(map(int, input().split())) for _ in range(n)]  # 2차원 배열 입력 받기

# 누적 합 배열 만들기
prefix = [[0] * (m + 1) for _ in range(n + 1)]  # (n+1) x (m+1) 크기의 누적 합 배열

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = array[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

# 부분 합 구하기
k = int(input())  # 질의 개수
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())  # (x1, y1): 시작 좌표, (x2, y2): 끝 좌표
    # 누적 합을 이용해 부분 배열의 합 계산
    result = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    print(result)
