"""
문제 이해
- 입력:
  - n : 케이스의 횟수
  - H, W, N : 층수(세로),호수(가로), N번째 들어온손님
- 출력:
  - answer : 입실하는 호수

손님은 엘리베이터를 타고 이동하는 거리는 신경쓰지 않음
다만, 걷는 거리가 같을 떄에는 아래층의 방을 더 선호
102호 보다는 301호를 더 선호
"""

n = int(input())
for _ in range(n):
  H, W, N = map(int, input().split())
  # 손님 객실의 층은 손님입장번호 % 층 
  floor = N % H

  # 손님 객실의 방번호는 손님입장번호 // 층 + 1
  room = N // H + 1

  # 하지만 층이 0이 나오는경우가 있는데 손님입장번호 % 층 == 0 일 경우에는 예외 케이스
  if floor == 0:
    floor = str(H)
    room = N // H
  
  answer = ""
  answer += str(floor)

  # 호실이 한자릿수면 0을 추가
  if room < 10:
    answer += "0"
    answer += str(room)
  else:
    answer += str(room)

  print(answer)
  