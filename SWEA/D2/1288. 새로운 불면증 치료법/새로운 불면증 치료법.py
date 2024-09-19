n = int(input())

for i in range(n):
  # 입력받은 값
  inputNum = int(input())

  # 값을 연산하기 위해 입력받은 값을 복사
  cacNum = inputNum
  
  # 0~9 까지 몇 번 등장했나 카운트
  countNum = [0,0,0,0,0,0,0,0,0,0]

  
  while True:
    sliceNum = []

    # 입력받은 숫자를 하나씩 리스트에 넣기(문자열로 변환 후 다시 정수로 변환해주어야 함)
    for k in str(cacNum):
      sliceNum.append(int(k))

    # 하나씩 리스트에 넣은 후 카운트
    for a in sliceNum:
      countNum[a] += 1
      
    # countNum의 최소 값이 0이 아니라면 0~9 모든 수를 거쳤다고 볼 수 있음
    if min(countNum) != 0:
      break
    
    cacNum = cacNum + inputNum

  print(f"#{i+1} {cacNum}")
      
    

  