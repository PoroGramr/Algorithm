n = int(input())

for i in range(n):
  P, Q, R, S, W = map(int, input().split())

  aBill = W * P
  bBill = 0
  if W <= R:
    bBill += Q
  else:
    bBill += Q
    bBill = bBill + S*(W - R) 

  if aBill < bBill:
    print(f"#{i+1} {aBill}")
  else:
    print(f"#{i+1} {bBill}")