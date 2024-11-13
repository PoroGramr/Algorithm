T = int(input())
for t in range(1, T + 1):
    N = int(input().strip())
    
    # 세제곱근을 계산하고 정수인지 확인
    root = round(N ** (1/3))
    
    # 확인된 세제곱근의 세제곱이 N과 일치하는지 검증
    if root ** 3 == N:
        print(f"#{t} {root}")
    else:
        print(f"#{t} -1")
