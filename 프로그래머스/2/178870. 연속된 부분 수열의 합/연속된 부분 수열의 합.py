def solution(sequence, target):
    left, current_sum = 0, 0
    min_length = float('inf')
    answer = [-1, -1]

    for right in range(len(sequence)):
        current_sum += sequence[right]

        # 현재 부분합이 target보다 크거나 같으면 left를 이동시켜 길이 최소화
        while current_sum >= target:
            if current_sum == target and (right - left < min_length):
                min_length = right - left
                answer = [left, right]

            current_sum -= sequence[left]
            left += 1

    return answer
