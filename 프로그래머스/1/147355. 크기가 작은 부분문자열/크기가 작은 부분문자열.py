def split_string(input_string, length):
    """
    입력 문자열을 지정된 길이만큼 잘라서 리스트로 반환합니다.

    Args:
        input_string (str): 잘라낼 원본 문자열.
        length (int): 각 부분 문자열의 길이.

    Returns:
        list: 원본 문자열을 부분 문자열로 잘라 만든 리스트.
    """
    # 부분 문자열을 저장할 리스트 초기화
    substrings = []

    # 문자열의 각 위치에서 시작하여 지정된 길이만큼 부분 문자열을 생성
    for i in range(len(input_string) - length + 1):
        substring = input_string[i:i + length]
        substrings.append(substring)

    return substrings


def solution(t, p):
    splitNum = split_string(t, len(p))
    print(splitNum)
    answer = 0
    for i in range(0, len(splitNum)):
        if splitNum[i] <= p:
            answer += 1
    return answer
