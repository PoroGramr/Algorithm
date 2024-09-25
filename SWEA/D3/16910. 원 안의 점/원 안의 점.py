n = int(input())

for i in range(n):
  answer = 0
  num = int(input())
  for x in range(-200,201):
    for y in range(-200, 201):
      if x ** 2 + y ** 2 <= num ** 2:
        answer += 1
  print(f"#{i+1} {answer}")
      