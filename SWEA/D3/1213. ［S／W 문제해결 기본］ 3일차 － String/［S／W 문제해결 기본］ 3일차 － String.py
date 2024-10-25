T = 10

for t in range(1, T+1):
    # 테스트 케이스 번호
    a = int(input())

    # 검색할 문자열
    ck = list(input())

    # 문자열의 길이(추후 연산에 필요)
    ckL = len(ck)

    # 총 문자열을 리스트로 입력받음
    data = list(map(str, input()))

    # 출현 횟수 카운트
    ans  = 0

    for i in range(len(data) - 1):

        # 검색할 문자열의 길이만큼 총 문자열을 처음부터 순회
        if data[i:i+ckL] == ck:
            ans += 1
    
    print(f"#{t} {ans}")



