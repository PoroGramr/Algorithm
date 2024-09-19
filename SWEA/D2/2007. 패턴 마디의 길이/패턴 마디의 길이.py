
n = int(input())

for i in range(n):
  inputStr = input()
  # 마디의 최대 길이는 10이므로 1 ~ 10길이를 순회
  for k in range(1,11):
    sliceStr = ""

    # 1 ~ 10 씩 슬라이싱
    for a in range(k):
      sliceStr += inputStr[a]
    # k, KO, KOR...

    compareStr = ""
    for b in range(k,k+k):
      compareStr += inputStr[b]
    if compareStr == sliceStr:
      print(f"#{i+1} {k}")
      break
    