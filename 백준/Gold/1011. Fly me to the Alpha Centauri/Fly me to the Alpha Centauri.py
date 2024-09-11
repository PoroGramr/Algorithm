import math

def min_moves(x, y):
    d = y - x  # 이동해야 할 거리
    if d == 0:
        return 0

    # 가장 가까운 제곱근을 구합니다
    n = int(math.sqrt(d))  

    # 거리가 정확히 n^2일 때
    if d == n * n:
        return 2 * n - 1
    # 거리가 n^2보다 크고 n^2 + n보다 작을 때
    elif n * n < d <= n * n + n:
        return 2 * n
    # 거리가 n^2 + n보다 클 때
    else:
        return 2 * n + 1
    
n = int(input())

for i in range(n):
  x,y = map(int, input().split())
  print(min_moves(x, y))
  
    