def solution(x):
    """
    입력 x를 각각 한 숫자씩 분리하여 계산한 후 나머지를 계산한다.
    """
    answer = True # 결과값의 기본값 설정
    sum = 0       # sum 변수 선언
    for i in list(str(x)):  # 입력 x를 i에 숫자 한개씩 넣어줌
        sum += int(i)
    if x % sum != 0:  # 각 숫자들의 합이 x로 나누어 떨어지는지 계산
        answer = False
    return answer