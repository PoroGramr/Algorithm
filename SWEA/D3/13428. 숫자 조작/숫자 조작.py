T = int(input())

for t in range(1, T + 1):
    num = int(input())

    # 현재 가장 큰 숫자
    big = num

    # 현재 가장 작은 숫자
    small = num

    # 입력받은 숫자를 리스트로 변환
    num = list(map(int,str(num)))

    # 숫자쌍을 하나씩 바꿔보는 루프
    for i in range(len(num)):
        for j in range(i, len(num)):

            # 숫자 2개의 위치를 바꿈
            num[i],num[j]= num[j],num[i]

            # 첫숫자가 0이 아닐때
            if num[0] != 0:
                numtonum = ""
                for k in num:
                    numtonum = numtonum + str(k)
                numtonum = int(numtonum)

                # 숫자쌍을 바꾼 숫자가 지금까지의 최대 값보다 크면 big 업데이트
                big = max(numtonum, big)
                
                # 숫자쌍을 바꾼 숫자가 지금까지의 최소 값보다 크면 small 업데이트
                small = min(numtonum, small)

            # 위치를 바꾼 숫자를 다시 원래 위치로 되돌림
            num[i], num[j] = num[j], num[i]

    # 테스트 케이스 번호, 최솟값, 최댓값 출력
    print(f"#{t} {small} {big}")