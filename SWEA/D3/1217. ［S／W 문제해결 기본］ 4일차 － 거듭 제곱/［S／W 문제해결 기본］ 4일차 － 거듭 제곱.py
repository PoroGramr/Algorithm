def twice(m, n):
  if n == 0:
    return 1

  return m * twice(m,n - 1)

for k in range(10):
  i = int(input())
  a,b = map(int, input().split())
  print(f"#{i} {twice(a,b)}")