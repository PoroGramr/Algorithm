for i in range(10):
  n, enc = map(str, input().split())
  enc = list(enc)
  n = int(n)
  
  while True:
    cha = 0
    for k in range(len(enc)-1):
      if enc[k] == enc[k + 1]:
        del enc[k]
        del enc[k]
        cha = 1
        break

    if cha == 0:
      break
  print(f"#{i+1} ", end="")
  for a in enc:
    print(a, end="")
  print("")
      