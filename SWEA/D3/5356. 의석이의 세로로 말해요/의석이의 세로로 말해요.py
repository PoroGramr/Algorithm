"""
가장 길이가 긴 문자 찾아서
그 문자 길이만큼 모든 문자에 "/"
삽입
그 후 결과 문자열 생성한 뒤 "/"를 제거
"""

T = int(input())

for t in range(1, T + 1):
    data = []

    for _ in range(5):
        data.append(list(map(str, input())))

    long = 0

    # 가장 긴 문자열의 길이 탐색
    for i in data:
        if len(i) > long:
            long = len(i)
    
    # 가장 긴 문자열의 길이에 맞게 문자열 리스트 생성
    for j in range(5):
        while len(data[j]) != long:
            data[j].append("/")
            
    
    # 결과 출력용 변수
    ans = ""
    
    
    # 인덱스에 맞게 결과 문자열 생성
    for k in range(long):
        for s in range(5):
            ans += data[s][k]
    
    # 불필요한 "/" 제거
    ans = ans.replace("/", "")

    print(f"#{t} {ans}")


