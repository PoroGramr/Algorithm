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
  
  floor = N % H
  room = N // H + 1

  if floor == 0:
    floor = str(H)
    room = N // H
  
 

  answer = ""
  answer += str(floor)
  
  if room < 10:
    answer += "0"
    answer += str(room)
  else:
    answer += str(room)
  print(answer)
  