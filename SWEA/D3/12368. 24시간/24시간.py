n = int(input())

for i in range(n):
  a,b = map(int, input().split())
  answer = a + b
  if answer >= 24:
    answer %= 24
  print(f"#{i+1} {answer}")