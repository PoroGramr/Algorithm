T = int(input())
ans = []
for t in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    
    # 0 ~ 100 초까지 초가 켜져 잇는 수를 저장할 리스트
    data = [0] * 102
    
    # 1번 초가 켜져있는 동안 리스트에 업데이트
    for i in range(A, B + 1):
        data[i] += 1
    
    # 2번 초가 켜져있는 동안 리스트에 업데이트
    for i in range(C, D + 1):
        data[i] += 1
    
    # 요구 사항에 맞게 계산하기 위해선 -1이 되어야 하기에 초기화를 -1로 해줌
    an = -1

    for j in data:
        if j == 2:
            an += 1
    
    # 만약 겹치는 시간이 없다면 0을 출력해야 하기에 0으로 업데이트
    if an == -1:
        an = 0
    
    # 제한시간 초과가 발생하기에 결과를 한번에 출력 하기 위해 리스트에 삽입
    ans.append(f"#{t} {an}")

# 결과를 모든 테스트케이스가 끝나고 한번에 출력 
for a in ans:
    print(a)