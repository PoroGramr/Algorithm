for i in range(10):
  n, enc = map(str, input().split())
  enc = list(enc)
  n = int(n)
  
  while True:
    # 무한반복문 탈출을 위한 체크 시그널
    cha = 0

    # k와 k+1요소를 비교하기에 len(enc)- 1의 반복을 돌아야 한다
    for k in range(len(enc)-1):

      # 만약 연속된 2요소의 값이 같다면
      if enc[k] == enc[k + 1]:
        
        del enc[k]
        # 위에서 요소를 하나 지웠기에 k+1의 인덱스는 k+1이 아닌 k가 된다.
        # 따라서 enc[k]를 두번 del 하는 것이다.
        del enc[k]

        # 리스트에 변경이 있었다는 시그널을 설정
        cha = 1
        break

    # 만약 리스트에 변동이 없었다면 멈추고 결과 출력
    if cha == 0:
      break
  print(f"#{i+1} ", end="")
  for a in enc:
    print(a, end="")
  print("")
      