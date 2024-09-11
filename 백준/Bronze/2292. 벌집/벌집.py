n = int(input())
# 해당 층의 마지막 숫자
floorLast = 1
# 층 = 이동횟수
floor = 1

if n == 1:
  print(1)
else:
  #입력받은 숫자가 해당층의 마지막 숫자보다 크다 -> 해당 층이 이동 횟수이다.
  while n > floorLast:
    # 해당 층의 마지막 숫자  floorLast += 6 * floor
    floorLast += 6 * floor
    floor += 1
  print(floor)
    