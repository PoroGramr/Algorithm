n = int(input())

for i in range(n):
  cm = int(input())
  data = list(map(int, input().split()))
  data.sort()

  print(f"#{i+1}", end =" ")
  for k in data:
    print(k, end =" ")
  print("")