n = int(input())

for i in range(n):
  inputStr = input()
  reverseStr = ""
  for k in inputStr[::-1]:
    reverseStr += k
  if reverseStr == inputStr:
    print(f"#{i+1} 1")
  else:
    print(f"#{i+1} 0")