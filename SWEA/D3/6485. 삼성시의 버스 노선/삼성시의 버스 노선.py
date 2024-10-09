"""
문제 이해
    - 입력 : 테스트 케이스 수 T
                버스 노선의 수 N
                번호 Ai, Bi -> N번 입력받음
                버스정류장의 수 P
                정류장의 번호 C -> P번 입력받음
            ex) 
                    1               //테스트 케이스 개수
                    2               //첫 번째 테스트 케이스, N=2
                    1 3             // A1 = 1, B1 = 3
                    2 5             // A2 = 2, B2 = 5
                    5               // P = 5
                    1               // 이하 C1 = 1, C2 = 2, C3 = 3, C4 = 4, C5 = 5
                    2
                    3
                    4
                    5	
                    
    - 출력 : 테스트 케이스, 정류장별 지나는 버스 노선의 개수
            ex) #1 1 2 2 1 1 

    삼성시의 5,000개의 버스 정류장은 관리의 편의를 위해 1 ~ 5,000번 까지 번호가 붙어있음
    그리고 버스노선은 N개가 있는데, i번째 버스노선은 번호가 Ai <=     <= Bi인 모든 정류장만을 다니는 버스 노선임
    이 떄, P개의 버스정류장에 대해 각가 몇개의 버스 노선이 다니는 지 구하시오

아이디어
1. 0 을 5,000개 가진 리스트를 stop 생성 (버스 정류장 별 지나는 버스의 수)
2. N 만큼 반복
    a,b 입력받음
        stop에서 a ~ b 요소를 +1
3. P 만큼 반복
    입력받은 c를 answer에 삽입
4. 출력
"""
T = int(input())
for t in range(1, T+1):
    stop = [0] * 5001
    N = int(input())
    
    for _ in range(N):
        a, b = map(int, input().split())
        for s in range(a, b+1):
            stop[s] += 1
    
    
    answer = []
    P = int(input())

    for _ in range(P):
        ind = int(input())
        answer.append(stop[ind])
    
    print(f"#{t}", end=" ")

    for b in answer:
        print(b,end =" ")
    print("")
