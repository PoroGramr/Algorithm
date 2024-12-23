# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

# 행렬 A 읽기
index = 0
N, M = map(int, data[index:index+2])
index += 2
A = []
for _ in range(N):
    A.append(list(map(int, data[index:index+M])))
    index += M

# 행렬 B 읽기
M, K = map(int, data[index:index+2])
index += 2
B = []
for _ in range(M):
    B.append(list(map(int, data[index:index+K])))
    index += K

# 행렬 곱셈 결과 계산
C = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

# 결과 출력
for row in C:
    print(*row)
