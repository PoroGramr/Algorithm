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

  # 판매 가격
  sellPrice = 0

  for val in data[::-1]: # 배열 거꾸로 순회
    if val >= sellPrice: #현재 값이 최댓값보다 크거나 같다면
        sellPrice = val #최댓값 업데이트
        #print("sellPrice", sellPrice)
    else:
        answer += sellPrice - val #아니라면 정답값에 가격차이를 더한다.
        #print("answer", answer)
      
  print("#", i + 1, " ", answer, sep="") #출력 양식에 맞춰서 출력
  