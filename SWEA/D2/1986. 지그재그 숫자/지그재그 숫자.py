n = int(input())

for i in range(n):
  answer = 0
  num = int(input())
  for k in range(1, num + 1):
    if k % 2 == 1:
      answer += k
    else:
      answer -= k
  print(f"#{i+1} {answer}")