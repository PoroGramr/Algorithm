T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    # 10진수를 2진수로 변환
    binNum = bin(M)
    
    # 변환한 2진수의 길이 계싼
    binNumLen = len(binNum)
    
    
    # 만약 N보다 이진수의 길이가 짧을 경우
    while binNumLen < N:
        
        # out of range 방지를 위해 가비지 문자를 추가
        binNum = "x" + binNum
        binNumLen += 1
    
    # 마지막 N개의 비트가 1인지 체크해야 하므로 1이 N개인 문자열 생성
    check = "1"*N
    
    # 마지막 N개의 비트와 1이 N개인 문자열 비교
    if binNum[-N:] == check:
        print(f"#{t} ON")
    else:
        print(f"#{t} OFF")
