def checkUp(check): # Ai * Aj를 저장한 리스트를 입력으로 받음
    
    # 단조 증가하는 수를 저장하기 위한 리스트
    checkCount = []

    # 먼저 Ai * Aj를 저장한 리스트의 요소들을 다 문자열로 형변환
    for s in range(len(check)):
        check[s] = str(check[s])

    # 리스트의 요소 하나씩 모두탐색
    for c in check:
        if len(c) == 1:
            checkCount.append(int(c))
            continue

        # 리스트요소의 1 ~ 마지막 요소까지
        for d in range(1,len(c)):

            # 이전요소 < 현재요소 일 경우에만 반복문 진행
            if int(c[d - 1]) <= int(c[d]):

                # 만약 마지막 요소까지 통과했을 경우 checkCount에 append
                if d == len(c) - 1:
                    checkCount.append(int(c))
            
            # 이전요소 < 현재요소가 아닐경우 반복문 중단(해당 요소 검사 중단)
            else:
                break

    # 만약 checkCount내에 요소가 있다면 최대값 리턴
    if checkCount:
        return max(checkCount)
    
    # 아무런 요소도 들어있지 않다면
    else:
        return -1

T = int(input())

for i in range(1, T+1):

    N = int(input()) # N개의 정수를 받기 위한 정수 N

    data = list(map(int, input().split())) # N개의 정수 리스트

    # Ai * Aj를 저장하기 위한 리스트
    sumData = []

    # 모든 Ai * Aj를 저장
    for a in range(N):
        for b in range(a+1,N):
            sumData.append(data[a] * data[b])

    # checkUP 리턴 값으로는 단조 증가하는 수의 최댓값을 리턴
    answer = checkUp(sumData)
    print(f"#{i} {answer}")