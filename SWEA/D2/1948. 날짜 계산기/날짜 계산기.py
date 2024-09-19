days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

n = int(input())

for i in range(n):
  answer = 0
  m1, d1, m2, d2 = map(int, input().split())

  day1 = 0
  for k in range(m1):
    day1 += days[k]
  day1 += d1

  day2 = 0
  for c in range(m2):
    day2 += days[c]
  day2 += d2

  answer = day2 - day1 + 1
  print(f"#{i+1} {answer}")