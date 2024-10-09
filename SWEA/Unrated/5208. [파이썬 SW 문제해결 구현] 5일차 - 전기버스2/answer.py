"""
문제 이해
    - 입력 : 테스트 케이스 T
        테스트 케이스 별로 한 줄에 정류장 수 N개의 정류장 별 태러티 용량이 주어짐
        ex)
            3
            5 2 3 1 1
            10 2 1 3 2 2 5 4 2 1
            10 1 1 2 1 2 2 1 2 1

    - 출력 : 테스트 케이스 별 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력
!주의사항
1. 출발지에서의 배터리 장착은 교환횟수에서 제외

아이디어
dfs(idx, cnt, bat) # 정류장 인덱스, 교체 횟수 카운트, 현재 전지량

if idx > len(data) and bat >= 0:
    ans = min(ans, cnt)

# 해당 인덱스에서 배터리를 충전
dfs(idx+1, cnt + 1, bat - 1 + data[idx])

# 해당 인덱스에서 배터리를 충전하지 않음
dfs(idx + 1, cnt, bat - 1)
"""

def dfs(idx, cnt, bat):
    global ans
    if ans <= cnt:
        return
    
    if idx == N:
        ans = min(ans,cnt)
        return

    # 교체를 안할 수 있을 때만 안한다.
    if bat > 0:
        dfs(idx+1, cnt, bat - 1)

    # 교체는 언제든 가능하기에 항상 가능
    dfs(idx+1, cnt + 1, data[idx] - 1)

T = int(input())

for t in range(1, T+1):

    data = list(map(int, input().split()))
    N = data[0]

    # 카운트 저장을 위한 변수 생성
    ans = N # 가능한 카운트의 최대 값

    dfs(2,0,data[1] - 1) # 인덱스, 충전하는 카운트, 매터리의 양

    print(f"#{t} {ans}")
