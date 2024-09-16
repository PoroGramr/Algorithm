n = int(input())

for i in range(n):
  N,M = map(int, input().split())
  
  data = []
  
  for j in range(N):
    data.append(list(map(int, input().split())))

  answer = 0
  
  for y in range(N - M + 1): # 총 탐색할 수 있는 y좌표
    for x in range(N - M + 1): # 총 탐색할 수 있는 x좌표

      # 루프를 돌면서 합을 초기화
      sum = 0

      # M*M의 크기의 합을 계산
      for addY in range(M):
        for addX in range(M):
          sum += data[y + addY][x + addX]

      # 최대값 업데이트
      answer = max(sum, answer)  
  print(f"#{i+1} {answer}")
      