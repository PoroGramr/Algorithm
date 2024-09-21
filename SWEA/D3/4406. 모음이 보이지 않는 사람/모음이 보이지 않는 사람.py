n = int(input())

aei = ["a", "e", "i", "o", "u"]

for i in range(n):
  inStr = input()
  answer = ""
  for k in inStr:
    if k in aei:
      continue
    else:
      answer += k
  print(f"#{i+1} {answer}")
  