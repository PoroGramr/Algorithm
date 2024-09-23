import math

n = int(input())

for i in range(n):
  a,b = map(int, input().split())
  answer = 0
  for k in range(a,b+1):
    oriK = list(str(k))
    revK = list(str(k))[::-1]
    if oriK == revK:
      ySqrt = math.sqrt(k)
      
      if ySqrt % 1 == 0:
        ySqrt = int(ySqrt)
        sqrtOriK = list(str(ySqrt))
        sqrtRevK = list(str(ySqrt))[::-1]
        if sqrtOriK == sqrtRevK:
          answer += 1

  print(f"#{i+1} {answer}")