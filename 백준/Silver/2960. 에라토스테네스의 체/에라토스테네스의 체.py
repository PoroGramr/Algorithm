# 입력 받기: n과 k
n, k = map(int, input().split())

# 카운트 변수: K번째로 지워지는 수를 찾기 위해 소수를 지울 때마다 카운트를 올린다
cnt = 0

# 소수 판별 리스트
# 처음에는 모든 수를 소수(True)로 가정한다
prime = [True] * (n + 1)

# 2부터 n까지 모든 숫자에 대해 반복
for i in range(2, n + 1):

    # 만약 i가 소수라면
    if prime[i]:
        # i의 배수를 지운다
        for j in range(i, n + 1, i):
            # j가 아직 지워지지 않은 수라면
            if prime[j] == True:
                prime[j] = False  # 소수의 배수는 소수가 아니므로 False로 변경
                cnt += 1  # 소수를 지울 때마다 카운트 증가

                # 만약 카운트가 k와 같다면, K번째로 지워진 수를 출력
                if cnt == k:
                    print(j)
                    exit()  # 출력 후 프로그램 종료
