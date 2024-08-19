def solution(numbers):
    # 문제이해
    # - 입력 : 정수 배열
    # - 출력 : 정수 배열의 평균
    # 제한사항
    # 아이디어
    # - 리스트의 총합을 구한다.
    # - 리스트의 총합을 리스트의 길이로 나눈다.
    numberSum = 0
    for i in numbers:
        numberSum += i
    answer = numberSum / len(numbers)
    return answer