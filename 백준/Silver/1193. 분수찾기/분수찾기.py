def find_fraction(n):
    # 대각선 번호를 구하기 위해 n이 속한 대각선 번호를 찾는다.
    diagonal = 1
    while n > diagonal:
        n -= diagonal
        diagonal += 1
    
    # 대각선 번호를 찾았으면 해당 대각선에서 분수를 구한다.
    if diagonal % 2 == 0:  # 짝수 번째 대각선은 분자가 감소, 분모는 증가
        numerator = n
        denominator = diagonal - n + 1
    else:  # 홀수 번째 대각선은 분자가 증가, 분모는 감소
        numerator = diagonal - n + 1
        denominator = n
    
    return f"{numerator}/{denominator}"

# 입력 값
n = int(input())
print(find_fraction(n))
