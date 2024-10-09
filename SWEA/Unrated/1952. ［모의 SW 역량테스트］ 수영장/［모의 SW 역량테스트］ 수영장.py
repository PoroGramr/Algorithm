"""
문제 이해
    - 입력 : 
        테스트 케이스 개수 T
            첫번쨰 테스트 케이스 이용관 가격들 정수 리스트
            12 개월 이용 계획 정수 리스트
            두번떄 테스트 케이스 이용권 가격들 정수 리스트
            12 개월 이용 계획 정수 리스트
        ex)
            10      
            10 40 100 300               # 일간, 월간, 3개월, 년간 요금 가격
            0 0 2 9 1 5 0 0 0 0 0 0     # 각 월별 사용해야 하는  일수
            10 100 50 300   
            0 0 0 0 0 0 0 0 6 2 7 8
    - 출력:
        수영장을 이용할 수 있는 최소 비용


아이디어
dfs를 이용한 최소 비용 추출
"""

def dfs(n, sm):
    global ans

    if n > 12:
        ans = min(ans, sm)
        return

    # 해당 월을 일일권으로 결제한 경우
    dfs(n + 1 , sm + (data[n] * day))

    # 해당 월을 월간권으로 결제한 경우
    dfs(n + 1, sm + mon)

    # 해당 월을 3개월권으로 결제한 경우
    dfs(n + 3 , sm + mon3)

    # 해당월을 연간권으로 결제한 경우
    dfs(n + 12, sm + year)

T = int(input())
for t in range(1, T+1):
    day, mon, mon3 , year = map(int, input().split())
    data = [0] + list(map(int, input().split()))

    ans = 3000 * 12 # 나올 수 있는 최대 비용
    dfs(1, 0) # 1월 부터 탐색 시작, 현재 비용

    print(f"#{t} {ans}")