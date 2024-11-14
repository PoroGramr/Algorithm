T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    
    # 점수를 높은 순으로 정렬
    scores.sort(key=lambda x: -x)
    
    # 상위 K개의 합을 출력
    ans = sum(scores[0:K])

    print(f"#{t} {ans}")
