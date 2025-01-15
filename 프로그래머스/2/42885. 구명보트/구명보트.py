def solution(people, limit):
    people.sort()  # 몸무게를 정렬
    left, right = 0, len(people) - 1  # 양 끝에서 시작하는 투 포인터
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 두 사람을 함께 태움
        right -= 1  # 무거운 사람은 항상 태움
        boats += 1  # 보트 사용 카운트 증가

    return boats
