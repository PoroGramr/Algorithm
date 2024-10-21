t = int(input())

for T in range(1, t+1):
    N = int(input())
    data = []
    # 문자를 리스트로 입력받음
    for _ in range(N):
        data.append(input())
    
    # set을 활용하여 중복을 제거
    data = set(data)

    # 다시 리스트로 만들어 줌, 정렬을 위해 리스트로 바꾸어 주어야 함
    data = list(data)

    # 길이순으로 정렬 후, 사전순으로 정렬
    data.sort(key = lambda x : (len(x), x))

    # 요구사항에 맞게 출력
    print(f"#{T}")
    for p in data:
        print(p)