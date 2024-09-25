n = int(input())

for i in range(n):
  n, k = map(int, input().split())
  data = list(map(int, input().split()))
  checkData = []
  answer = []
  for a in range(1,n+1):
    checkData.append(a)
  for b in checkData:
    if b in data:
      continue
    else:
      answer.append(b)
  
  answer.sort()

  print(f"#{i+1} ",end="")
  for an in answer:
    print(an, end=" ")
  print("")
  