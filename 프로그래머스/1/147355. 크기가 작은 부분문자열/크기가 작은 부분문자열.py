def split_string(input_string, length):
    return [input_string[i:i+length] for i in range(len(input_string) - length + 1)]


def solution(t, p):
    splitNum = split_string(t, len(p))
    print(splitNum)
    answer = 0
    for i in range(0, len(splitNum)):
        if splitNum[i] <= p:
            answer += 1
    return answer