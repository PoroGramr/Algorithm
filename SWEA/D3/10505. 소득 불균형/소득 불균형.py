n = int(input())

for i in range(n):
  case = int(input())
  data = list(map(int, input().split()))
  cen = sum(data) // case
  answer = 0
  for c in range(len(data)):
    if data[c] <= cen:
      answer += 1

  print(f"#{i+1} {answer}")