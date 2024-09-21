n = int(input())

for i in range(n):
  # 원래 메모라 값을 입력받음
  inNum = input()

  # 변경해야하는 횟수 카운트용 변수
  answer = 0

  # 입력받은 원해 메모리 값을 리스트로 변환
  inData = []
  for k in inNum:
    inData.append(k)

  # 루프를 돌며 횟수를 체크할때 필요한 문자 리스트 생성
  answerData = ["0"] * len(inData)

  # 입력받은 원래 메모리 값의 길이만큼 순회
  for a in range(len(inData)):

    # 만약 해당 인덱스의 리스트 값이 같다면 패스
    if inData[a] == answerData[a]:
      continue

    # 리스트 값이 다르다면
    else:
      # 해당 인덱스에 0 이 입력되어야 하는 경우 나머지 요소를 모두 0으로 변경
      if inData[a] == "0":
        for b in range(a,len(inData)):
          answerData[b] = "0"
      # 해당 인덱스에 1 이 입력되어야 하는 경우 나머지 요소를 모두 1으로 변경
      else:
        for c in range(a,len(inData)):
          answerData[c] = "1"
      # 변경되었다는 횟수 카운트 +1
      answer += 1
      
  print(f"#{i+1} {answer}")
  