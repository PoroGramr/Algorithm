"""
입력
    - 시험장의 개수 N
    - 각 시험장에 있는 응시자의 수 리스트
    - 촘 감독관이 한 시험장에서 감시할 수 있는 응시자의 수 B, 부 감독관이 한 시험장에서 감시할 수 있는 응시자수 C
출력
    - 각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수

아이디어
    감독관 카운트 = 0
    각 시험장마다 인원수 - B, 감독관 카운트 +1
    인원수 % C == 0
    감독관 카운트 + 인원수 // C
    else
    감독관 카운트 + 인원수 // C + 1 
    
"""

N = int(input())
data = list(map(int, input().split()))
B ,C = map(int, input().split())
ans = 0
for i in range(N):
    # 응시생
    tester = data[i]
    # 감독관
    cctv = 0

    # 총감독관 카운트
    tester -= B
    cctv += 1

    if tester >= 0:
        # 부감독관 카운트

        # 만약 C 로 나뉘어 진다면 그대로 더해줌
        if tester % C == 0:
            cctv += tester // C
        
        # 나뉘어 떨어지지 않는다면 +1 하여 더해줌
        # ex) 남음 학생은 3명, 부감독관이 감독 가능한 학생수 2명일경우
        #     3 / 2 + 1 = 2 해야 2명의 부감독관 카운트가 가능
        else:
            cctv += tester // C + 1
    
    ans += cctv
print(ans)
