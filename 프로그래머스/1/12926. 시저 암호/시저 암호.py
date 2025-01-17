def solution(s, n):
    result = []
    for char in s:
        if char.islower():  # 소문자일 경우
            result.append(chr((ord(char) - ord('a') + n) % 26 + ord('a')))
        elif char.isupper():  # 대문자일 경우
            result.append(chr((ord(char) - ord('A') + n) % 26 + ord('A')))
        else:  # 알파벳이 아닌 경우
            result.append(char)
    return ''.join(result)
