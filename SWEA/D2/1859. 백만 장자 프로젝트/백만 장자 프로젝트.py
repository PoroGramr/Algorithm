"""
문제이해
- 입력 :
  - 테스트 케이스 수
  - 정수 N(연속된 N일의 N)
  - 정수 리스트 (각 날의 매매가를 나타내는 N개의 자연수)
- 출력 :
  - 각 테스트 케이스마다 최대 이익 #1 0\n #2 10
아이디어
  리스트를 역으로 순회하며 뒤에서 부터 최대값을 순회하며 최대 값 - 해당 순회 날짜의 차이를 계산
"""

n = int(input())

for i in range(n):
  day = int(input())
  data = list(map(int, input().split()))

  answer = 0

  sellPrice = 0 # 역으로 순회하며 리스트에서 해당 루프까지의  최대 값
  
  for curPri in data[::-1]: # 역으로 순회
    
    if sellPrice < curPri: # 현재 가격이 지금까지의 최대 값보다 비쌀 경우
      sellPrice = curPri
      
    else: # 지금까지의 최대값 - 현재값
      answer += sellPrice - curPri
       
  print(f"#{i+1} {answer}")
    
  