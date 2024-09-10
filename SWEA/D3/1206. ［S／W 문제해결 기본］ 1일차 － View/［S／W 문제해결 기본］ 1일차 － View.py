for i in range(10):
  n = int(input()) # 건물개수
  data = list(map(int, input().split()))
  result = 0
  for k in range(2, n - 2):
    left1 = data[k] - data[k-1]
    left2 = data[k] - data[k-2]
    right1 = data[k] - data[k+1]
    right2 = data[k] - data[k+2]
    if left1 > 0 and left2>0 and right1>0 and right2 > 0:
      result += min(left1,left2,right1,right2)
  print(f"#{i+1} {result}")