n = int(input())

for i in range(n):
  answer = 0
  l,u,x = map(int, input().split())
  if x > u:
    answer = -1
  elif x < l:
    answer = l - x

  print(f"#{i+1} {answer}")