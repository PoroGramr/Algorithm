
T = int(input())

for t in range(1, T+1):
    S, D, H, C = [[0] * 13 for _ in range(4)] # 각 마크 별로 리스트를 만들어줌
    cards = input() # 입력

    # 3글자 단위로 끊어서 연산
    for i in range(0,len(cards),3):
        data = cards[i:i+3]

        # 첫글자는 마크
        mark = data[0]
        # 2 ~ 3 번째 글자는 int형으로 변환
        num = int(data[1::])


        # 각 마크에 따라 카운트 해줌
        if mark == "S":
            S[num - 1] += 1
        elif mark == "D":
            D[num - 1] += 1
        elif mark == "H":
            H[num - 1] += 1
        elif mark == "C":
            C[num - 1] += 1

    # 부족한 카드를 찾기위해 카운트
    scount = 13
    dcount = 13
    hcount = 13
    ccount = 13

    # 해당 카드가 있다면 -1
    for s in S:
        if s == 1:
            scount -= 1
    
    for d in D:
        if d == 1:
            dcount -= 1
    
    for h in H:
        if h == 1:
            hcount -= 1
    for c in C:
        if c == 1:
            ccount -= 1
    
    # 2개 이상이면 중복이므로 에러처리
    if max(S) >= 2 or max(D) >= 2 or max(H) >= 2 or max(C) >= 2:
        print(f"#{t} ERROR")

    # 정답 출력
    else:
        print(f"#{t} {scount} {dcount} {hcount} {ccount}")

                  

